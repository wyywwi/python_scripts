import requests
import random
import json

rand_num = int(random.random()*10**5)

def get_waifu(num):
    url = "https://www.thiswaifudoesnotexist.net/example-" + str(num) + ".jpg"
    img = requests.get(url).content
    img_name = "example_" + str(num) + ".jpg"
    with open(img_name, "wb") as fp:
        fp.write(img)
    print(type(img))

get_waifu(rand_num)
