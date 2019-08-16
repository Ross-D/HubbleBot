#Scrapes image from web
import requests # pip install requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

url = 'http://spacetelescopelive.org/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html5lib")
images = soup.findAll('img')
for image in images:
    s = str(image)
    if s.find(".jpg") == -1:
        continue
    else:
        #print image source
        src=image['src']
        print(src)

img_url = str(url+src)
response = requests.get(img_url, stream=True)
img = Image.open(response.raw)
print(img)
plt.imshow(img)
img.show()
