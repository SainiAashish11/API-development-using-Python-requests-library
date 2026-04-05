'''PUT — "Replace Everything"
Analogy:
    - You submitted a job application form 3 days ago. Today you want to change it — but the office says "We don't accept corrections — you must submit a completely new form to replace the old one."
    - That's PUT — you replace the ENTIRE record with a new one.'''

import requests
import json

def pretty(response):
    print(f"Status Code : {response.status_code}")
    print(json.dumps(response.json() , indent = 4))

updated_post = {                         # updated body
    "id" : 1,
    "title" : "Updated title",           # changed title
    "body"  : "Completely new body",     # changed body
    "userId" : 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1" ,
    json = updated_post )

pretty(response)