import requests

resp = requests.post("https://getprediction-rkac76by4a-ue.a.run.app", files={'file': open('test_data.csv', 'rb')})
#resp = requests.post("http://127.0.0.1:5000", files={'file': open('test_data.csv', 'rb')})

print(resp.json())
