import requests 			#for retrieving data
from bs4 import BeautifulSoup 		#for reading/searching html file
import re				#for editing text
from PIL import Image			#for opening image
import matplotlib.pyplot as plt		#for showing image

def Image_Scrape(): 	#function to scrap image from site
    url = 'http://spacetelescopelive.org/'	#url of website to scrape
    r = requests.get(url)			#retrieving html file
    soup = BeautifulSoup(r.text, "html5lib")	#reading html file in beautiful soup, html5lib is parsing package used
    images = soup.findAll('img')		#creating a list of all lines with img tag
    for image in images:		#loop that sorts through images to
        s = str(image)			#find the .jpg file extension as
        if s.find(".jpg") == -1:	#hubble's view is the only .jpg used
            continue
        else:
            src=image['src']

    img_url = str(url+src)				#creating url to image
    response = requests.get(img_url, stream=True)	#getting image from url
    img = Image.open(response.raw)			#opening raw image data
    plt.imshow(img)					#creating image with plt
    plt.show()						#showing image
    plt.pause(60)					#pausing 1 minute
    plt.clf()						#clearing figure

def Text_Scrape():	#function to scrape text from site
    url = 'http://spacetelescopelive.org/'			#url of site to scrape
    r = requests.get(url)					#getting html file
    soup = BeautifulSoup(r.text, "html5lib")			#reading html into beautifulsoup, html5lib is parsing package
    div = soup.findAll('div', {"class": "message_content"})	#finding all divs with class "message_content"
    Div_str=str(div)				#turning line into string
    sub1=re.sub('<.+?>', '', Div_str)		#removing html element script
    sub2=re.sub('\n', '', sub1)			#removing line breaks
    message=re.sub('   ', '', sub2)		#removing white space
    print(message[1:(len(message)-1)])		#printing message
