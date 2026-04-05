'''  DELETE — Remove This 

Rule:

1.You send the ID in the URL, not in the body
2.Successful delete returns 200 or 204 (204 = No Content — nothing to return, it's deleted)
3.Most dangerous method — no undo

'''

''' Basic DELETE '''
import requests
import json

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")    # id = 1 is explicitely passed

print(f"Status Code : {response.status_code}")
print(f"Response body : {response.json()}")         # returns empty dictionary after deletion of post

################################################################################################################

''' Intermediate DELETE '''
# 1.With safety check

import requests
import json

post_id_to_delete = 5

response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id_to_delete}")

if response.status_code == 200:
    print(f"Post {post_id_to_delete} successfully deleted")
elif response.status_code == 404:
    print(f"Post {post_id_to_delete} not found. Maybe already deleted.")
else:
    print(f"Unexpected Error : {response.status_code}")