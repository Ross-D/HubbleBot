import Scrapers				#.py containing functions
import matplotlib.pyplot as plt		#for plt.ion

plt.ion()	#allows update of fig
while True:				#infinite loop
	Scrapers.Text_Scrape()		#scapes message, run first as plt.pause in Image_scrape
	Scrapers.Image_Scrape()		#scrapes image

