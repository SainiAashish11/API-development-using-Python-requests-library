import requests
import json

def pretty(label , response):
    print(f"{'='*10} {label} {'='*10}")
    print(f"status : {response.status_code}")
    print(json.dumps(response.json() , indent = 4))


# ------------- CREATE (POST) ----------------
new_post = {'title' : 'CRUD' , 'body' : 'Learning APIs' , 'userId' : 1}
create_response = requests.post("https://jsonplaceholder.typicode.com/posts" , json = new_post )
pretty("Create" , create_response)
created_id = create_response.json()['id']
print(created_id)


# ------------- READ (GET) -------------------
read_response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{created_id}")
pretty("READ" , read_response)


# ------------- UPDATE (PATCH) ---------------
patch_response = requests.patch(f"https://jsonplaceholder.typicode.com/posts/{created_id}",
                                json = {'title' : 'Updated CRUD Demo'})
pretty("UPDATE" , patch_response)


# ------------- DELETE -----------------------
delete_response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{created_id}")
pretty("DELETE" , delete_response)
