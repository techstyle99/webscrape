
import random
import urllib.request

def download_web_image(url): 
	name = random.randrange(1, 1000)
	full_name = str(name) + ".jpg"
	urllib.request.urlretrieve(url, full_name)



download_web_image("https://media.truefacet.com/guide/wp-content/uploads/2017/06/ROLEX-DATE-JUST.jpg")
download_web_image("https://www.bizmove.com/_images/wise-quotes.jpg")
download_web_image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREaydjBxZ4gLOd-A3qRnrOt4GAbVaWx0VINw&usqp=CAU")