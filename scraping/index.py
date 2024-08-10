import requests
import bs4

result=requests.get('https://example.com')
soup=bs4.BeautifulSoup(result.text,'lxml')
# print(soup.select('p'))
print(soup.select('title')[0].getText())
site_p=soup.select('p')[0].getText()
print(site_p)