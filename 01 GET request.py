''' Simple GET() method '''
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")       # url of a website
print(response.status_code)     # it tells the status of the request made
print(response.json())          # parse the JSON response from the 'url' and prints the result in the form of python 'dictionary'

################################################################################################################################

''' Beginner friendly GET() method with function '''
import requests
import json

def pretty(response):
    print(f"Status Code : {response.status_code}")
    print(json.dumps(response.json(), indent=4))

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
pretty(response)

#################################################################################################################################

''' Intermediate GET() methods '''
# 1.Fetch a list
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

print(f"Total posts received : {len(data)}")
print(f"First post title: {data[0]['title']}")


# 2.Using Query parameters (Filtering)
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts" , params = {"userId" : 1})    # params = {"userId" : 1} -> fetching only the userId = 1 from the whole data

data = response.json()
print(f"Posts by user 1: {len(data)}")        # how many userId = 1 are present
for post in data:
    print(f"  - {post['title'][:40]}...")     # printing only 40 character for every 'title' of each "userId = 1"


#################################################################################################################################

''' Advanced GET() '''
# 1.Extracting specific fields from response
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
all_posts = response.json()                             # dictionary of all posts with each and every data

# Extract only titles and IDs from each and every 'post'
titles_and_IDs = [{"id": post["id"], "title": post["title"]} for post in all_posts]      # fetching 'IDs and titles' in a list using list comprehension

for item in titles_and_IDs[:5]:                         # Fetching first 5 titles only
    print(f"ID {item['id']}: {item['title'][:50]}")


# 2.Headers - Sending metadata with request
# Some APIs require you to identify yourself via headers before any action
# This is like showing your ID card before entering a library
import requests
headers = {
    "User-Agent": "MyPythonApp/1.0",     # Who is making this request -> 'MyPythonApp/1.0' is used to tell server that i'm not a bot and making a genuine request to you
    "Accept": "application/json"         # What format do I want back -> tells in which format i want results
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    headers=headers
)

print(response.status_code)   # 200 -> means OK
print(response.headers)       # See what headers the SERVER sent back -> sent the overall  summary of the communication happened

##################################################################################################################################