import requests

response = requests.get('https://www.baidu.com')

print(response.status_code)
print(response.url)
print(response.headers)
print(response.cookies)
print(response.text)
print(response.content)
