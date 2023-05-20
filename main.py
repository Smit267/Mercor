import json
import numpy as np
import torch
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertTokenizer, BertModel
from flask import Flask, request, jsonify

app = Flask(__name__)

# Step 1: Collect and preprocess data (sample dataset for demonstration)
dataset = [
    {
        "description": "This is a red t-shirt with a logo.",
        "url": "https://www.tatacliq.com/puma-red-active-small-logo-mens-t-shirt/p-mp000000009785560"
    },
    {
        "description": "A blue denim jacket for casual wear.",
        "url": "https://www.jackjones.in/287152503-dark-denim?gclid=Cj0KCQjwmZejBhC_ARIsAGhCqndjK7BpQ0YiErmpqyPORqUgA44j9cc2wcskzMrgGGKaEAoy4y2UXnoaAoZ4EALw_wcB"
    },
    {
        "description": "Black solid opaque Casual shirt ,has a spread collar, button placket, na pocket, short regular sleeves, straight hem",
        "url": "https://www.myntra.com/shirts/herenow/herenow-men-black-slim-fit-casual-shirt/19818628/buy"
    },
    {
        "description": "Blue solid opaque casual shirt ,has a spread collar, button placket, long regular sleeves, curved hem",
        "url": "https://www.myntra.com/shirts/fubar/fubar-slim-fit-spread-collar-casual-shirt/22988248/buy"
    },
    {
        "description": "Red T-shirt for men, Typography printed, Regular length, Round neck, Short, regular sleeves, Knitted cotton fabric",
        "url": "https://www.myntra.com/tshirts/allen-solly-tribe/allen-solly-tribe-men-typography-printed-slim-fit-t-shirt/18327258/buy"
    },
    {
        "description": "Maroon and black checked casual shirt, has a mandarin collar, long sleeves, curved hem",
        "url": "https://www.myntra.com/shirts/roadster/roadster-men-maroon--black-checked-casual-sustainable-shirt/6696340/buy"
    },
    {
        "description": "Red Tshirt for men ,Solid, Regular length, Polo collar, Short, regular sleeves, Knitted pure cotton fabric, Button closure",
        "url": "https://www.myntra.com/tshirts/united-colors-of-benetton/united-colors-of-benetton-polo-collar-pure-cotton-t-shirt/22175982/buy"
    },
    {
        "description": "Grey melange Tshirt for men, Typography printed, Regular length, Round neck, Short, regular sleeves, Knitted pure cotton fabric",
        "url": "https://www.myntra.com/tshirts/roadster/roadster-men-grey-melange-typography-printed-pure-cotton-graphic-t-shirt/8938267/buy"
    }
]

# Preprocess the data
corpus = [item['description'] for item in dataset]

# Step 2: Measure similarity
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')


def extract_bert_features(text):
    encoded_input = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        output = model(**encoded_input)
    features = output.last_hidden_state.mean(dim=1).squeeze().numpy()
    return features


# Compute BERT features for the dataset
dataset_features = []
for description in corpus:
    features = extract_bert_features(description)
    dataset_features.append(features)


# Step 3: Return ranked results
def get_similar_items(input_text, n=5):
    input_features = extract_bert_features(input_text)

    # Compute cosine similarity between the input and dataset items
    similarity_scores = cosine_similarity([input_features], dataset_features).flatten()

    # Sort the items based on similarity scores
    sorted_indices = np.argsort(similarity_scores)[::-1][:n]

    # Return the top-N most similar item URLs
    results = []
    for index in sorted_indices:
        item = dataset[index]
        results.append(item['url'])

    return results


@app.route('/', methods=['GET', 'POST'])
def clothing_similarity_search():
    try:
        data = request.get_json()
        input_text = data['text']

        similar_items = get_similar_items(input_text)

        response = {'similar_items': similar_items}
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
