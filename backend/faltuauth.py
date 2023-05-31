import requests

url = "http://172.18.0.86/fibonacci/1_1_2_3"
response = requests.get(url)
response_json = response.json()
print(response_json["value"])