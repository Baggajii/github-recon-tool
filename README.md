# GitHub Recon Automation Tool

This project is a Python-based tool that scans public GitHub repositories for exposed sensitive information related to a given keyword or domain name. It uses the GitHub Code Search API to identify files where the keyword appears, such as configuration files, environment files, or code snippets.

The tool is designed for learning and cybersecurity training, focusing on OSINT and automation.

---

## Features

- Searches across public GitHub repositories using the Code Search API  
- Detects appearances inside:
  - `.env`
  - `.json`
  - `.yml`
  - `.config`
  - `.py`
  - and other text-based files  
- Extracts key details:
  - Repository name  
  - File path  
  - File extension  
  - Direct GitHub file URL  
  - Snippet of the matched line  
  - Timestamp of the scan  
- Saves results in a structured `results.json` file  
- Masks potentially sensitive values  
- Includes basic error and rate-limit handling  
- Beginner-friendly and easy to extend  

---

## Installation

Install the required Python modules:


---

## How to Run

Run the script:


Provide the following when asked:

1. **Target keyword or domain name**  
   Example: `cashify`, `example.com`, `linkedin`, etc.

2. **GitHub Personal Access Token (PAT)**  
   A classic token with `code:read` permission works.

Once completed, the script generates a `results.json` file containing all findings.

---

## Sample Output (results.json)

```json
[
  {
    "repo_full_name": "acme/example-repo",
    "file_path": "config/.env",
    "file_type": ".env",
    "html_url": "https://github.com/acme/example-repo/blob/main/config/.env",
    "match_snippet": "API_KEY=********abcd",
    "searched_keyword": "example.com",
    "timestamp": "2025-05-22T18:00:00Z"
  }
]
Author

Ramandeep Bagga
Cybersecurity Enthusiast

