import requests
import json
import jsonpath
import pytest

# API URL
@pytest.mark.Smoke
def test_fetch_user_details():
    url = "https://reqres.in/api/users?page=2"
    #
    # # send get request
    response = requests.get(url)
    #print(response)

    # Display Response content

    #print(response.content)
    #print(response.headers)
    ## Validate response code
    #print(response.status_code)
    #assert response.status_code == 200 ## to compare code value

    # Fletch header content
    #print(response.headers)

    ##Fetch specific fields in header
    #print(response.headers.get("Date"))
    #print(response.headers.get("Server"))

    ## Fetch cookies
    #print(response.cookies)

    ##Fetch Encoding
    #print(response.encoding)

    ##Fetch elapsed time(It is like RTT (round trip time)
    #print(response.elapsed)

    ## Parse responce to json format

    json_response = json.loads(response.text)
    # #pages = jsonpath(json_response,"total_pages") # Jsonpath always retuen as a list
    # #print(pages[0])
    # #assert pages[0] == 2
    #
    for i in range(0,4):
         first_name = jsonpath.jsonpath(json_response, "data[(i)].first_name")
         print(first_name)

    ## Delete Request

    # url = "https://reqres.in/api/users/2"
    # response = requests.delete(url)
    # print(response.status_code)
    # assert response.status_code == 204
