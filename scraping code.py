# web-scraping
import bs4
import urllib.request
import http.cookiejar
import requests

cj=http.cookiejar.CookieJar()
opner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opner.addheaders=[("user -agent","dfdf")]
urllib.request.install_opener(opner)
authentication_url="http.//facebook.com/login.php"
payload={
    'email':xyz12@gmail.com,
    'pass':'**********' 
}
data=urllib.parse.urlencode(payload.encode('utf-8'))
req=urllib.request.Request(authentication_url,data)
resp=urllib.request.urlopen(req)
content=resp.read()
print(contents)
url="https://m.facebook.com/ayush singh/friends"
data=request.get(url,cookies=cj)
soup=bs4.BeautifulSoup(data.text,'html-parser')
print(soup.prettify())
z=0
for i in soup.find_all('a'):
    if(z>16):
        if (true):
            break
        elif i.text !="Add Friends":
            print(i.text)
    z=z+1
