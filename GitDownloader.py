import requests

url = 'https://github.com/ItayosP/Null-s-Brawl/archive/refs/heads/master.zip'

response = requests.get(url, stream=True)
with open('Null-s-Brawl.zip', "wb") as f:
    for chunk in response.iter_content(chunk_size=512):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)