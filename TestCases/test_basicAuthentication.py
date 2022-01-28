import requests
from requests.auth import HTTPBasicAuth

def test_with_Authentication():
    response = requests.get("https://github.com/user",auth=HTTPBasicAuth('pritambhat007','Sarthak@121bhat'))
    print(response.text)