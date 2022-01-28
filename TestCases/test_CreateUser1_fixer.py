## convert test case in pytest format
import requests
import json
import jsonpath
import pytest
## API URL
url = "https://reqres.in/api/users"

@pytest.fixture
def fixer_code():
    global file
    file = open(r"C:\Users\bhatp\Desktop\createPOST.json", 'r')
    print("___________________________________")
    
@pytest.mark.Smoke
def test_create_new_user(fixer_code):
    json_input = file.read()
    request_json = json.loads(json_input)
    #print(request_json)
    # Make POST request with json body
    response = requests.post(url,request_json)
    # print(response.content)
    # print(response)
    #
    # #Validating Response code
    assert response.status_code == 201
    
    #  Fetch header response
    print(response.headers.get("Content-Length"))
    
    #Parse response to json format
    response_json = json.loads(response.text)
    print(response_json)
    id = jsonpath.jsonpath(response_json,"id")
    print(id)

@pytest.mark.Sanity
def test_create_second_user(fixer_code):
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    # Make POST request with json body
    response = requests.post(url, request_json)
    # print(response.content)
    # print(response)
    #
    # #Validating Response code
    assert response.status_code == 201

    #  Fetch header response
    print(response.headers.get("Content-Length"))
    # Parse response to json format
    response_json = json.loads(response.text)
    print(response_json)
    id = jsonpath.jsonpath(response_json, "id")
    print(id)