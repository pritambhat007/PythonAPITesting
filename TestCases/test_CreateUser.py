## convert test case in pytest format
import requests
import json
import jsonpath
import pytest
## API URL
url = "https://reqres.in/api/users"
a=10
#@pytest.mark.skip("This is not available with current build") ## OR
@pytest.mark.skipif(a>10,reason="Condition not meet")
def test_create_new_user():
    read_file = open(r"C:\Users\bhatp\Desktop\createPOST.json",'r')
    json_input = read_file.read()
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


def test_create_second_user():
    read_file = open(r"C:\Users\bhatp\Desktop\createPOST.json", 'r')
    json_input = read_file.read()
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