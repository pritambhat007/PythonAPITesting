## Taking responce of one test and use that response as request in another test case
import json
import jsonpath
import requests

def test_user_details():
    global id
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/Users/bhatp/Desktop/API-PYTEST/Add_User.json", 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL,json_request)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])
    print(response.text)

def get_details():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails" + str(id[0])
    response = requests.get(API_URL)
    print(response.text)

