import requests
import json
import base64

sonar_url = '{Your URL}'
auth_token = '{Your Token}'
project_key = 'swprase'
api_endpoint = f'{sonar_url}/api/issues/search'

auth_string = f'{auth_token}:'
encoded_auth = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
headers = {
    'Authorization': f'Basic {encoded_auth}'
}

def fetch_all_issues(url, headers, project_key):
    all_issues = []
    page = 1
    page_size = 100

    while True:
        params = {
            'componentKeys': project_key,
            'p': page,
            'ps': page_size
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            issues = data.get('issues', [])
            all_issues.extend(issues)
            if len(issues) < page_size:
                break
            page += 1
        else:
            print(f"Failed to fetch issues: {response.status_code}")
            break

    return all_issues

issues = fetch_all_issues(api_endpoint, headers, project_key)

if issues:
    with open('all_project_issues.json', 'w') as file:
        json.dump(issues, file, indent=4)
    print(f"Successfully retrieved and saved all issues for project {project_key}.")
else:
    print("No issues found or error in fetching issues.")

# curl -u {Your Token}: '{Your URL}/api/issues/search?componentKeys=swprase'
