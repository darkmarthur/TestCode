import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
my_url = "https://www.newegg.com/global/mx/Gaming-Laptops/SubCategory/ID-3365?Tid=899891"
uClient = ureq(my_url)
pageHtml = uClient.read()
uClient.close()
ps = soup(pageHtml, "html.parser")
# print(ps.body.prettify())
#  ps.h1

# class="item-container  "
# class="items-view is-grid"
# class="item-title"
# price-currency-label strong sup
# item-brand a


containers = ps.findAll("div", {"class" : "item-container"})
# len(containers)
# item = containers[0]
    # itemShipping = item.findAll("li", {"class":"price-ship"})[0].text.strip()
    # print("itemShipping: " + itemShipping)


fileName = "products.csv"
f = open(fileName, "w")
headers = "brand, price, title\n"
f.write(headers)

for item in containers:
    itemBrand = item.div.a.img["title"]
    itemPrice = item.findAll("li", {"class":"price-current"})[0].strong.text
    itemTitle = item.findAll("a", {"class":"item-title"})[0].text
    # print("itemBrand: " + itemBrand)
    # print("itemPrice: " + itemPrice)
    # print("itemTitle: " + itemTitle)
    f.write(itemBrand + ", " + itemPrice + ", " + itemTitle.replace(",", "|") + "\n")

f.close()