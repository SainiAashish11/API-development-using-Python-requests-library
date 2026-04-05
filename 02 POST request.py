''' Basic Post - Create a New post '''
import requests
import json

def pretty(response):
    print(f"Status Code : {response.status_code}")
    print(json.dumps(response.json() , indent = 4))

# The Data we want to send
new_post = {
    "title" : "My First API post",
    "body"  : "I am learning requests library",
    "userId" : 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts",   # URL and location where we want to add our data
                      json = new_post)                                   # 'json=' automatically converts dict to JSON

pretty(response)

#############################################################################################################################

''' Intermediate POST '''
# Sending with explicit headers
import requests
import json

def pretty(response):                                                    # function body
    print(f"Status Code : {response.status_code}")
    print(json.dumps(response.json() , indent = 4))                      # json.dumps = pack Python dict into JSON string | response.json() = unpack JSON string back to Python dict

data = {                                                                 # 'data(body)' in dictionary form
    "title" : "Manual Header Post",
    "body"  : "Sending with explicit content type",
    "userId" : 2
}

headers = {                                                              # 'headers' tells the extra instructions for the server from user/client side
    "Content-Type" : "application/json"
}

response = requests.post("https://jsonplaceholder.typicode.com/posts",
                         data = json.dumps(data),                        # converting data dictionary -> JSON format
                         headers = headers                               # passing 'headers'
                         )

pretty(response)                                                         # passing 'response' parameter into 'pretty' function

