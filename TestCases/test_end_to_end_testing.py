import requests
import json
import jsonpath


def test_new_user_data():
    App_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/Users/bhatp/Desktop/API-PYTEST/Add_User.json",'r')
    json_request = json.loads(f.read())
    response = requests.post(App_URL,json_request)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])
    print(response.text)

    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    f = open("C:/Users/bhatp/Desktop/API-PYTEST/Technical_details.json",'r')
    json_request = json.loads(f.read())
    json_request['id']=int(id[0])
    json_request['st_id']=id[0]
    response = requests.post(tech_api_url,json_request)
    print(response.text)

    add_api_url = "http://thetestingworldapi.com/api/addresses"
    f = open("C:/Users/bhatp/Desktop/API-PYTEST/Address.json", 'r')
    json_request = json.loads(f.read())
    json_request['stId']=id[0]
    response = requests.post(add_api_url,json_request)
    print(response.text)

    final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/546000" + str(id[0])
    response = requests.get(final_details)
    print(response.text)


