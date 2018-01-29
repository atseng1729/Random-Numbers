import requests

def random(low,high):
    param = {"num": 1, "min": low, "max": high, "col": 1, "base": 10, "format": "plain", "rnd": "new"}
    response = requests.get("https://www.random.org/integers/", param)
    return int(response.content)
