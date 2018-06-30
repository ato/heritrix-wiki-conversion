#!/usr/bin/env python3
import sys, os, requests, re
from glob import glob
from urllib.parse import quote

if 'API_USER' in os.environ:
    api_auth = (os.environ['API_USER'], os.environ['API_TOKEN'])
else:
    print('API_USER and API_TOKEN not set, doing dry run.')
    api_auth = None # dry run

def migrate(page_id):
    api_url = "https://webarchive.jira.com/wiki/rest/api/content/" + str(page_id)
    old = requests.get(api_url).json()

    github_name = old['title']
    #github_url = "https://github.com/internetarchive/heritrix3/wiki/" + quote(github_name)
    github_url = "https://github.com/ato/heritrix-wiki-conversion/wiki/" + quote(github_name)
    text = "<p>This page has moved to <a href='" + github_url + "'>" + github_name + "</a> on the Github wiki.</p>"

    update = {
        "type": "page",
        "title": old['title'],
        "body": {"storage": {"value": text, "representation": "storage"}},
        "version": {
            "number": old['version']['number'] + 1,
            "minorEdit": True,
            "message": "Migrated to Github wiki"
        }
    }

    # check that the github URL is correct
    if requests.head(github_url).status_code != 200:
        print(page_id, github_url, 'does not exist')
        return

    if api_auth is None:
        print(page_id, 'OK. But dry run.')
        return

    response = requests.put(api_url, json=update, auth=api_auth)
    if response.status_code != 200:
        print('Failed:', page_id, response.status_code, response.text)

def main():
    if len(sys.argv) < 2:
        print('Usage:', sys.argv[0], 'path-to-confluence-html-export')
        sys.exit(1)

    export_path = sys.argv[1]
    for file in glob(export_path + '/*.html'):
        filename = os.path.basename(file)
        if filename == 'index.html':
            continue
        if '_' in filename: # e.g. Avoiding-Too-Much-Dynamic-Content_5735747.html
            filename = filename.split('_')[-1]
        page_id = filename.split('.')[0]
        migrate(page_id)

if __name__ == '__main__': main()
