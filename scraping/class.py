import requests
import bs4

result=requests.get('https://en.wikipedia.org/wiki/Jonas_Salk')
soup=bs4.BeautifulSoup(result.text,'lxml')

site_p=soup.select('.mw-jump-link')
for item in site_p:
    print(item.text)