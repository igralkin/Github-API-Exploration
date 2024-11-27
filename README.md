# Github API Exploration

The repository contains the API analysis and test results for the GitHub API/

## Contents
- `/Content`: Documentation and troubleshooting guides.
- `/Postman_Collection`: Postman collection used for testing the GitHub API.

## **Purpose of the test**

The goal of this assignment was to:
1. Demonstrate proficiency in working with APIs by researching the GitHub API.
2. Extract data using the GitHub API for specific requirements such as repositories, commits, and file contents.
3. Troubleshoot common API-related issues such as authentication, pagination, and rate limits.
4. Document the process and results in a clear and organized manner.

## **Client Requirements**

The following requirements were assumed to address the needs of the client for analyzing GitHub repositories and their data:

1. **Search for Public Repositories**
   - The client requires a way to search GitHub for public repositories based on keywords.
   - Results should include:
     - Repository name.
     - Number of stars.
     - Repository URL.
   - Support sorting by stars, forks, or update time.
   - Allow pagination and limit the total number of results fetched.

2. **Retrieve Commits for a Specific Repository**
   - The client requires a method to fetch commit history for any given repository.
   - Results should include:
     - Commit SHA.
     - Commit message.
     - Commit author and timestamp.
   - Support pagination to handle repositories with long commit histories.

3. **Access File or Folder Contents**
   - The client requires functionality to fetch metadata or contents of a specific file or folder within a repository.
   - Results should include:
     - File name, path, and type (`file` or `dir`).
     - Base64-encoded content for files.

4. **Handle API Rate Limits**
   - The client needs robust error handling for GitHub API rate limits.
   - The solution should:
     - Pause execution when rate limits are exceeded.
     - Automatically retry the request once limits are reset.

5. **Documentation and Reproducibility**
   - The client expects comprehensive documentation for:
     - API endpoints used.
     - Error handling strategies.
     - Steps to reproduce the project in Postman, Python, or Colab.


## **Repository structure**
- README.md
- /Content
    - API_Documentation.md
    - troubleshooting_guide.md
    - Github_API_usage.py
    - Github_API_usage.ipynb
- /Postman_Collection
    - GitHub API Test.postman_collection.json
  
## **Steps to complete the assignment**
- Research GitHub API
- Test endpoints in Postman
- Document results and troubleshooting

## **How to use the exported Postman collection**
1. Create a Postman environment and add the following variable:
   - Variable Name: token
   - Value: Your GitHub Personal Access Token (PAT)
2. Select the environment before running requests.

## **Google Colab Integration**
The repository includes a Colab notebook (`Github_API_usage.ipynb`) demonstrating the GitHub API interactions. To use:
1. Open the notebook in [Google Colab](https://colab.research.google.com/).
2. Enter your Personal Access Token (PAT) when prompted.
3. Run the provided examples to test the functionality.
