#!/usr/bin/python

import requests
import json
import sys

with open("hl.json") as file:
    data = json.load(file)
    hl_data = {'highlights': []}

    for hl in data['highlights']:
        if hl['text'] != '':
            hl_data['highlights'].append({
                 'text': hl['text'],
                 'title': next(item['name'] for item in data['documents'] if item['id'] == hl['document_id']),
                'source_type': 'rextract',
                 'category': 'books',
                 'location_type': 'page',
                 'location': hl['page_number']
            })

    cont = input(f"Found {len(hl_data['highlights'])} new highlights. Upload to Readwise? Y/N:  ")
    if cont.lower() == 'n':
        exit()
    
    json_str = json.dumps(hl_data)

    r = requests.post(
        url="https://readwise.io/api/v2/highlights/",
        headers={"Authorization": "Token XXXX"},
        json=json_str
    )

    if r.status_code == 200:
        print(f"Successfully uploaded {len(hl_data['highlights'])} to Readwise!")
    else:
        print(r.json())
