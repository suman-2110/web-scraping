import bs4
import requests


url = "https://www.mycodingzone.net/blog/english"
data= requests.get(url)
soup =bs4.BeautifulSoup(data.text,'html.parser')
#print(soup.prettify)

for para in soup.find_all('p'):
    print(para.text)
