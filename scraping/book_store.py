import requests
import bs4

base_url='https://books.toscrape.com/catalogue/page-{}.html'


# print(example.select('.star-rating.Three'))
two_star_titles=[]
for n in range(1,10):
    scrape_url=base_url.format(n)
    res=res=requests.get(scrape_url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    books=soup.select('.product_pod')
    for book in books:
        if len(book.select('.star-rating.Two'))!=0:
            book_title=book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)
            
    
    



