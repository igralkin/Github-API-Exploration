# Troubleshooting Guide

This guide addresses common issues encountered while working with the GitHub API.

## 1. Authentication Issues
### Problem: 401 Unauthorized
- **Cause**: Invalid or missing token.
- **Solution**:
  - Verify `{{token}}` environment variable is set correctly.
  - Ensure the token has the correct permissions (e.g., `repo` scope).
  - Use `Authorization: Bearer {{token}}` in the header.

### Problem: 403 Forbidden
- **Cause**: Rate limit exceeded.
- **Solution**:
  - Check response headers: `X-RateLimit-Remaining` and `X-RateLimit-Reset`.
  - Wait until the reset time or reduce request frequency.


## 2. Pagination Issues
### Problem: Missing Results
- **Cause**: Default results limited to 10 per page.
- **Solution**:
  - Use `per_page` (max 100) and `page` parameters to fetch additional results.


## 3. Missing or Unexpected Data
### Problem: Fields not in Response
- **Cause**: API endpoint may return varying structures.
- **Solution**:
  - Verify endpoint response with the API documentation.
  - Inspect raw responses in Postman.


## 4. Rate Limits
### Problem: Too Many Requests
- **Cause**: Exceeding API rate limits (403 or 429 errors).
- **Solution**:
  - Monitor `X-RateLimit-Remaining` and delay requests if needed.
  - Authenticate with a token for increased limits (5,000 requests/hour).


## 5. Miscellaneous Errors
### Problem: 404 Not Found
- **Cause**: Incorrect `repo_owner`, `repo_name`, or `path`.
- **Solution**:
  - Double-check the repository or file path.

### Problem: 422 Unprocessable Entity
- **Cause**: Incorrect query parameters.
- **Solution**:
  - Validate parameters with API documentation.


## Best Practices
1. Use a valid Personal Access Token (PAT) for authentication.
2. Handle pagination and rate limits gracefully.
3. Test endpoints and save responses for debugging.
