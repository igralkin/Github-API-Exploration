# API Documentation

Overview of the GitHub API tested endpoints.

## Tested endpoints

### 1. Search Repositories
**Purpose**: Search public repositories based on keywords and sort criteria.

**Endpoint**: `GET /search/repositories`

**Parameters**:
- `q` (required): Search query (e.g., `machine learning`).
- `sort` (optional): Sort field (e.g., `stars`, `forks`).
- `order` (optional): Sort order (`asc` or `desc`).
- `per_page` (optional): Results per page (default: 10, max: 100).
- `page` (optional): Page number (default: 1).

**Example Request**:
### GET https://api.github.com/search/repositories?q=machine+learning&sort=stars&order=desc&per_page=10&page=1

**Key response fields**:
- `total_count`: Total repositories matching the query.
- `items`: Array of repository objects containing:
  - `name`: Repository name.
  - `html_url`: Repository URL.
  - `stargazers_count`: Star count.


### 2. List Commits
**Purpose**: Retrieve commits from a specific repository.

**Endpoint**: `GET /repos/{owner}/{repo}/commits`

**Parameters**:
- `owner` (required): Repository owner (e.g., `octocat`).
- `repo` (required): Repository name (e.g., `hello-world`).
- `per_page` (optional): Results per page (default: 10).
- `page` (optional): Page number (default: 1).

**Example Request**:
### GET https://api.github.com/repos/octocat/hello-world/commits?per_page=10&page=1

**Key response fields**:
- `sha`: Commit hash.
- `commit.message`: Commit message.
- `commit.author.name`: Author name.
- `commit.author.date`: Commit date.


### 3. Get Content
**Purpose**: Retrieve metadata or content of a file/folder in a repository.

**Endpoint**: `GET /repos/{owner}/{repo}/contents/{path}`

**Parameters**:
- `owner` (required): Repository owner (e.g., `octocat`).
- `repo` (required): Repository name (e.g., `hello-world`).
- `path` (required): Path to the file/folder (e.g., `README`).

**Example Request**:
### GET https://api.github.com/repos/octocat/hello-world/contents/README

**Key response fields**:
- **File**:
  - `name`: File name.
  - `content`: Base64-encoded file content.
- **Folder**:
  - Array of files and subfolders:
    - `name`: Name of each file/folder.
    - `type`: Type (`file` or `dir`).

## Notes
1. **Authentication**:
   - Use a Personal Access Token (PAT) in the `Authorization` header:
     ```
     Authorization: Bearer {{token}}
     ```
2. **Pagination**:
   - Use `per_page` and `page` to navigate large datasets.
3. **Rate Limits**:
   - Authenticated requests allow up to 5,000 requests per hour.
   - Check headers like `X-RateLimit-Remaining` for rate limit usage.
