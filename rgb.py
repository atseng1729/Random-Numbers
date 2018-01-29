from PIL import Image
import requests
import numpy as np

def rgbImage():
    pixels = []

    #gets 50,000 random numbers from random.org and adds them to pixels
    for i in range(0, 5):
        parameters = {"num": 10000, "min": 0, "max": 256, "col": 1, "base": 10, "format": "plain", "rnd": "new"}
        response = requests.get("https://www.random.org/integers/", parameters)
        text = res.text
        temp = text.split('\n')
        pixels += [int(i) for i in temp]

    array = np.array(pixels[0:49152]).reshape(128, 128, 3).astype('uint8')
    image = Image.fromarray(array,"RGB")
    image.save('RGB.bmp')

if __name__ = "__main__":
    rgbImage()
