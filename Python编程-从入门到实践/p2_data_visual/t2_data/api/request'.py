import requests

a = requests.request("get","https://api.github.com/search/repositories?q=language:python&sort=stars")
print(a.text)