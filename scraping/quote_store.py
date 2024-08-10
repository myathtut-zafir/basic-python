import requests
import bs4

base_url='https://quotes.toscrape.com/page/{}/'

authorsFinal=set()
for n in range(1,10):
    scrape_url=base_url.format(n)
    res=res=requests.get(scrape_url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    authors=soup.select('.author')

    for author in authors:
        if len(author)!=0:
            authorsFinal.add(author.text)

print(authorsFinal)
            
    
    



