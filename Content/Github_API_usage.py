import requests
import time
import math
from typing import List, Dict, Optional, Any, NoReturn

class GitHubAPI:
    """Class for interacting with the GitHub API."""

    def __init__(self, token: str) -> None:
        """
        Initialize the GitHubAPI instance with a Personal Access Token.

        :param token: GitHub Personal Access Token for authentication.
        """
        self.base_url: str = "https://api.github.com"
        self.headers: Dict[str, str] = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }

    def _handle_rate_limit(self, response: requests.Response) -> requests.Response:
        """
        Handle rate limits by waiting until the reset time if exceeded.

        :param response: The response object from the API call.
        :return: The response object after handling rate limits.
        """
        if response.status_code == 403 and "X-RateLimit-Remaining" in response.headers:
            remaining_requests = int(response.headers.get("X-RateLimit-Remaining", 0))
            reset_time = int(response.headers.get("X-RateLimit-Reset", time.time()))
            wait_time = reset_time - int(time.time())
            if remaining_requests == 0:
                print(f"Rate limit exceeded. Waiting for {wait_time} seconds...")
                time.sleep(wait_time + 1)
        return response

    def search_repositories(
        self, query: str, sort: str = "stars", order: str = "desc",
        per_page: int = 10, max_repos: int = 100, delay: float = 1.0
    ) -> List[Dict[str, Any]]:
        """
        Search for public repositories with pagination, limiting results and adding delays.

        :param query: Search query string.
        :param sort: Sort by (e.g., "stars", "forks", "updated").
        :param order: Order of results ("asc" or "desc").
        :param per_page: Number of results per page.
        :param max_repos: Maximum number of repositories to retrieve.
        :param delay: Time in seconds to wait between page queries.
        :return: List of repository data.
        """
        all_results: List[Dict[str, Any]] = []
        page: int = 1

        # Calculate total pages to query
        url = f"{self.base_url}/search/repositories"
        params = {"q": query, "sort": sort, "order": order, "per_page": per_page, "page": page}
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code != 200:
            if response.status_code == 403:
                print("Rate limit exceeded. Retrying after a delay...")
                self._handle_rate_limit(response)
            else:
                print(f"Error: {response.status_code}, {response.text}")
            return []

        data = response.json()
        total_count: int = data.get("total_count", 0)
        total_pages: int = math.ceil(min(total_count, max_repos) / per_page)

        # Process first page
        all_results.extend(data.get("items", []))

        # Process remaining pages
        for page in range(2, total_pages + 1):
            if len(all_results) >= max_repos:
                break

            params["page"] = page
            response = requests.get(url, headers=self.headers, params=params)

            if response.status_code != 200:
                if response.status_code == 403:
                    print("Rate limit exceeded. Retrying after a delay...")
                    self._handle_rate_limit(response)
                    continue
                else:
                    print(f"Error: {response.status_code}, {response.text}")
                    break

            data = response.json()
            items = data.get("items", [])
            all_results.extend(items)

            time.sleep(delay)

        return all_results[:max_repos]

    def list_commits(self, repo_owner: str, repo_name: str, per_page: int = 10) -> List[Dict[str, Any]]:
        """
        List commits for a specific repository with pagination.

        :param repo_owner: Owner of the repository.
        :param repo_name: Name of the repository.
        :param per_page: Number of commits to fetch per page.
        :return: List of commits.
        """
        all_results: List[Dict[str, Any]] = []
        page: int = 1

        while True:
            url = f"{self.base_url}/repos/{repo_owner}/{repo_name}/commits"
            params = {
                "per_page": per_page,
                "page": page
            }
            response = requests.get(url, headers=self.headers, params=params)
            response = self._handle_rate_limit(response)

            if response.status_code == 200:
                data = response.json()
                all_results.extend(data)
                if len(data) < per_page:  # No more pages
                    break
                page += 1
            else:
                print(f"Error: {response.status_code}, {response.text}")
                break

        return all_results

    def get_content(self, repo_owner: str, repo_name: str, path: str) -> Optional[Dict[str, Any]]:
        """
        Get metadata or content of a file or folder in a repository.

        :param repo_owner: Owner of the repository.
        :param repo_name: Name of the repository.
        :param path: Path to the file or folder.
        :return: Dictionary containing file/folder metadata, or None if an error occurs.
        """
        url = f"{self.base_url}/repos/{repo_owner}/{repo_name}/contents/{path}"
        response = requests.get(url, headers=self.headers)
        response = self._handle_rate_limit(response)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

    @staticmethod
    def exit_with_error(message: str) -> NoReturn:
        """
        Exit the program with an error message.

        :param message: The error message to display.
        """
        print(f"Error: {message}")
        exit(1)


def main():
    # Initialize token
    token: str = "token_placeholder"

    if token == "token_placeholder":
        token = input("Enter your GitHub Personal Access Token (PAT): ").strip()
        if not token:
            GitHubAPI.exit_with_error("Personal Access Token is required.")

    print('INITIALIZING GITHUB API CLIENT')
    # Initialize GitHub API client
    github_api = GitHubAPI(token)

    # Example: Search for repositories
    print('SEARCHING FOR REPOS')
    query = "machine learning"
    per_page = 10
    max_repos = 30
    delay_time = 1

    repos = github_api.search_repositories(query=query, per_page=per_page, max_repos=max_repos, delay=delay_time)
    print(f"Total repositories fetched: {len(repos)}")
    for repo in repos:
        print(f"Repo Name: {repo['name']}, Stars: {repo['stargazers_count']}, Url: {repo['html_url']}")
    print("-"*20)
    print()

    # Example: List commits
    print('LISTING COMMITS')
    repo_owner = "octocat"
    repo_name = "hello-world"
    per_page = 5

    commits = github_api.list_commits(repo_owner=repo_owner, repo_name=repo_name, per_page=per_page)
    if commits:
        for commit in commits:
            print(f"Commit SHA: {commit['sha']},\n Commit message: {commit['commit']['message']}")
    print("-"*20)
    print()

    # Example: Get content
    print('GETTING CONTENT')
    repo_owner = "octocat"
    repo_name = "hello-world"
    path = "README"

    content = github_api.get_content(repo_owner=repo_owner, repo_name=repo_name, path=path)
    if content:
        print(content)


if __name__ == '__main__':
    main()
