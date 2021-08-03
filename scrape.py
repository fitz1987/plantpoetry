# web scraper python script
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# configure scraper to use Chrome browser
browser = webdriver.safari.webdriver.WebDriver(quiet=False)

# open the URL
browser.get("https://www.burpee.com/flowers/full-sun-flowers/")

# get the data i want from the pages
flowers = []
nlist = []
content = browser.page_source
soup = BeautifulSoup(content, features="html.parser")
for a in soup.findAll('div', attrs={'class' : 'product-item-details'}):
    desc = a.find('div', attrs={'class' : 'product-item-short-description'})
    flowers.append(desc.text)
    names = a.find('a', attrs={'class' : 'product-item-link'})
    nlist.append(names.text)
browser.close()

res = []
for ele in flowers:
    res.append(ele.strip())
print("res is:", res)

with open('flowers.txt', 'w') as f:
    for item in res:
        f.write("%s\n" % item)

res2 = []
for ele in nlist:
    res2.append(ele.strip())
print("res2 is: ", res2)
with open('flowers.txt', 'a') as f:
    for item in res2:
        f.write("%s\n" % item)
