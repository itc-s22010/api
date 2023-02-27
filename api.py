from PIL import Image
import io
import requests
 
url = "https://dog.ceo/api/breeds/image/random"

responce = requests.get(url)

jsj= responce.json()
imageurl= jsj['message']
img = str(imageurl)

file =io.BytesIO(requests.get(img).content)
img = Image.open(file)
img.show()
print(responce)
