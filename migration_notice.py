#!/usr/bin/env python3
import sys, os, requests

page_id = int(sys.argv[1])
github_name = sys.argv[2]
auth = (os.environ['API_USER'], os.environ['API_TOKEN'])

api_url = "https://webarchive.jira.com/wiki/rest/api/content/" + str(page_id)
github_url = "https://github.com/internetarchive/heritrix3/wiki/" + github_name

text = "<p>This page has moved to <a href='" + github_url + "'>" + github_name + "</a> on the Github wiki.</p>"

old = requests.get(api_url).json()

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

response = requests.put(api_url, json=update, auth=auth)

print(response.status_code)
print(response.text)
