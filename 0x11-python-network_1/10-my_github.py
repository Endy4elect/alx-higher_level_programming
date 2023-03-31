#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python github_id.py <username> <personal_access_token>')
        sys.exit(1)

    username = sys.argv[1]
    access_token = sys.argv[2]

    url = f'https://api.github.com/users/{username}'
    headers = {'Authorization': f'Basic {access_token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        print(f"User ID: {user_info['id']}")
    else:
        print(f"Error: {response.status_code}")
