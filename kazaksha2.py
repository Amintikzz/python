import requests

f=open('kazaksha.txt', 'w')
API_KEY = ""
url = f"https://texttospeech.googleapis.com/v1/voices?key={API_KEY}"

response = requests.get(url)
f.write(str(response.json()))
f.close()

