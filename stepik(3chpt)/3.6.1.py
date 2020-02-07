import requests
with open('dataset_3378_2.txt', 'r') as rfile:
    url = rfile.readline().strip()
response = requests.get(url)
print(len(response.text.splitlines()))