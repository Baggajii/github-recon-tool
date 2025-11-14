import requests
import json
import datetime
import re

def mask_sensitive(value):
    if not value or len(value) < 8:
        return value
    return value[:4] + "****" + value[-4:]

def search_github(keyword, token):
    url = "https://api.github.com/search/code"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.text-match+json"
    }
    params = {"q": keyword}

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 403:
            print("Rate limit hit. Try again after some time.")
            return []

        if response.status_code != 200:
            print("GitHub API error:", response.status_code)
            return []

        data = response.json()
        return data.get("items", [])

    except Exception as e:
        print("Error:", str(e))
        return []

def extract_snippet(text_matches):
    try:
        for match in text_matches:
            frag = match.get("fragment", "")
            lines = frag.split("\n")
            for line in lines:
                if "=" in line or ":" in line:
                    clean = re.sub(r'[A-Za-z0-9]{12,}', mask_sensitive, line)
                    return clean.strip()
            return lines[0].strip()
    except:
        return None

def save_results(results):
    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)
    print("Saved as results.json")

def main():
    print("GitHub Recon Tool")
    keyword = input("Enter keyword or domain: ").strip()
    token = input("Enter GitHub API Token: ").strip()

    print("Scanning...")

    items = search_github(keyword, token)
    output = []

    for item in items:
        repo_name = item.get("repository", {}).get("full_name", "")
        file_path = item.get("path", "")
        html_url = item.get("html_url", "")
        file_type = "." + file_path.split(".")[-1] if "." in file_path else "unknown"

        snippet = None
        if "text_matches" in item:
            snippet = extract_snippet(item["text_matches"])

        timestamp = datetime.datetime.utcnow().isoformat() + "Z"

        output.append({
            "repo_full_name": repo_name,
            "file_path": file_path,
            "file_type": file_type,
            "html_url": html_url,
            "match_snippet": snippet,
            "searched_keyword": keyword,
            "timestamp": timestamp
        })

    save_results(output)
    print("Scan complete.")

if __name__ == "__main__":
    main()
