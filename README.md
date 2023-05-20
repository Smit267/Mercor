# Mercor
Assignment 

## To run the project using Docker and interact with it using cURL, follow these steps:

1. Install Docker: Ensure that Docker is installed on your computer. You can download and install Docker from the official Docker website (https://www.docker.com/get-started).

2. Download the project files: Download all the project files and save them in a single folder on your computer.

3. Open a command prompt or terminal: Open a command prompt or terminal window on your computer.

4. Navigate to the project folder: Use the `cd` command to navigate to the folder where you saved the project files. For example:

   ```shell
   cd path/to/project/folder
   ```

5. Build the Docker image: Run the following command to build the Docker image for the project:

   ```shell
   docker build -t clothing-similarity-search .
   ```

   This command builds the Docker image using the provided Dockerfile.

6. Run the Docker container: Execute the following command to run the Docker container and start the application:

   ```shell
   docker run -p 8080:8080 clothing-similarity-search
   ```
   
   This command starts the Docker container and maps port 8080 of the container to port 8080 on your local machine.

7. Open another command prompt or terminal: Open a new command prompt or terminal window while keeping the Docker container running.

8. Navigate to the project folder: Use the `cd` command to navigate to the folder where you saved the project files (same as step 4).

9. Send a request to the application: Use the following `curl` command to send a POST request to the running application and obtain the output. You can modify the text to your desired input:

   ```shell
   curl -X POST -H "Content-Type: application/json" -d "{\"text\": \"A red shirt with a logo\"}" http://localhost:8080/
   ```

   This command sends a POST request with the specified JSON payload to the application and retrieves the output.

By following these steps, you should be able to run the project and obtain the output using Docker. 

Note: Make sure to have Docker running on your computer before executing the commands.

