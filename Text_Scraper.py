import requests # pip install requests
from bs4 import BeautifulSoup
import numpy as np
import re

url = 'http://spacetelescopelive.org/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html5lib")
div = soup.findAll('div', {"class": "message_content"})
Div_str=str(div)
sub1=re.sub('<.+?>', '', Div_str)
sub2=re.sub('\n', '', sub1)
sub3=re.sub('   ', '', sub2)
message=re.sub('  ', ' ', sub3)
print(message[1:(len(message)-1)])

