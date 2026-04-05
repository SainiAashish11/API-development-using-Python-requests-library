''' PATCH - Change Just One Thing 

Rule:

1.Send only the fields you want to change
2.Other fields stay untouched
3.More efficient than PUT for small changes
'''

import requests
import json

def pretty(response):
    print(f"Status code : {response.status_code}")
    print(json.dumps(response.json() , indent = 4))

partial_update = {
    "title" : "Only the title changed"               # only 'title' changed not any other components
}

response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json = partial_update                            # converting 'partial_update' dictionary into JSON format
)

pretty(response)
