import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
my_url = "https://www.newegg.com/global/mx/Gaming-Laptops/SubCategory/ID-3365?Tid=899891"
uClient = ureq(my_url)
pageHtml = uClient.read()
uClient.close()
pageSoup = soup(pageHtml, "html.parser")
pageSoup.h1
