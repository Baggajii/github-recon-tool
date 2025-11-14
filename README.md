# GitHub Recon Automation Script

This project is a simple Python tool that scans public GitHub repositories for sensitive information related to a given keyword or domain name. It uses the GitHub Code Search API to identify files that may contain secrets, configuration data, or exposed credentials.

The script was created as part of a cybersecurity training assignment and focuses on automation, OSINT, and secure coding practices.

---

## Features

- Search for sensitive code exposures across public GitHub repositories
- Detect matches inside files (.env, .config, .json, .yml, .py, etc.)
- Extract:
  - Repository name
  - File path
  - File type
  - Direct GitHub file URL
  - Snippet of the matched line
  - Timestamp of scan
- Mask sensitive values in the output
- Save results in a structured `results.json` file
- Handles rate limits and API errors
- Beginner-friendly and modular script design

---

## Requirements

Install dependencies using:

pip install -r requirements.txt

markdown
Copy code

Dependencies include:
- `requests`
- `json`
- `argparse`
- `datetime`

## How to Run

1. Clone or download the project.
2. Open a terminal in the project folder.
3. Run the script:

python main.py

yaml
Copy code

4. Enter the following when prompted:
   - Target keyword (example: `cashify`, `linkedin`, `example.com`)
   - GitHub Personal Access Token (PAT)

The script will generate a `results.json` file with all findings.

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
    "searched_keyword": "cashify.in",
    "timestamp": "2025-05-22T18:00:00Z"
  }
]
Notes
Always use a valid GitHub Personal Access Token.

This tool is for educational OSINT and security research purposes.

Do not misuse the script or target unauthorized systems.

Author
Ramandeep Bagga
Cybersecurity Student 





