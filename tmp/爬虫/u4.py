import requests
from requests import ReadTimeout, HTTPError,RequestException

for a in range(500):
    try:
        response = requests.get('https://www.bilibili.com',timeout=0.5)
        print(a,response.status_code)
    except ReadTimeout as rto:
        print("timeout",rto)
    except HTTPError as he:
        print("http error",he)
    except RequestException as re:
        print("reqerror",re)
