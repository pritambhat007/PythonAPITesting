import requests
import json
import jsonpath

def test_add_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/Users/bhatp/Desktop/API-PYTEST/Add_User.json",'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL,json_request)
    print(response.text)

def test_update_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/545991"
    f = open("C:/Users/bhatp/Desktop/API-PYTEST/Add_User.json",'r')
    json_response = json.loads(f.read())
    response = requests.put(API_URL,json_response)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/545991"
    response = requests.get(API_URL)
    #json_response = json.loads(response.text) ## OR
    json_response = response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response,'data.id')
    print(id)
    assert id[0] == 545991

def test_delete_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/545991"
    response = requests.delete(API_URL)
    print(response.text)


