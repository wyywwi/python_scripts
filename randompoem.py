import requests
import json

def get_random_poem():
    return json.loads(requests.get("https://v1.jinrishici.com/all.json").content)

rand_poem = get_random_poem()
print(rand_poem)