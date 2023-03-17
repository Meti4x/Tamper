import os
import requests


# Start Code 
os.system("cat banner.txt")

get_Url = input()

print("Target is:       ", get_Url)
print("")
print("")

def get_request():
    req = requests.get(get_Url)
    print("GET method:      ", req.status_code)
    
def post_request():
    req = requests.post(get_Url)
    print("POST method:     ", req.status_code)

def put_request():
    req = requests.put(get_Url)
    print("PUT method:      ", req.status_code)

def delete_request():
    req = requests.delete(get_Url)
    print("DELETE method:   ", req.status_code)

def patch_request():
    req = requests.patch(get_Url)
    print("PATCH method:    ", req.status_code)

def head_request():
    req = requests.head(get_Url)
    print("HEAD method:     ", req.status_code)

def option_request():
    req = requests.options(get_Url)
    print("OPTION method:   ", req.status_code)

def run_function():
    get_request()
    post_request()
    put_request()
    delete_request()
    patch_request()
    head_request()
    option_request()

run_function()