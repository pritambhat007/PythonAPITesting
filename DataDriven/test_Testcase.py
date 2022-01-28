import json
import jsonpath
import requests
import openpyxl
from DataDriven import Library


def test_add_new_student():
    ## API_URL code
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/Users/bhatp/Desktop/API-PYTEST/add_new_student.json",'r')
    json_requests = json.loads(f.read())
    ## Excel code

    obj = Library.Common("C:/Users/bhatp/Desktop/API-PYTEST/testdata.xlsx",'Sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keylist = obj.fetch_key_names()

    for i in range(2,row+1):
        updated_json_request = obj.update_request_with_data(i,json_requests,keylist)
        response = requests.post(api_url,updated_json_request)
        print(response)