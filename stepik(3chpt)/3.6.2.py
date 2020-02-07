import requests
with open('dataset_3378_3.txt', 'r') as rfile:
    url = rfile.readline().strip()
response = requests.get(url)
while response.text[0] != "W":
    response = requests.get("https://stepic.org/media/attachments/course67/3.6.3/"+response.text)
    print(response.text)
response = requests.get(url)
print(response.text)