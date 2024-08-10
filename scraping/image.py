import requests
import bs4

result=requests.get('https://en.wikipedia.org/wiki/Deep_Blue_versus_Garry_Kasparov')
soup=bs4.BeautifulSoup(result.text,'lxml')

site_p=soup.select('.mw-file-element')
computer=site_p[0]
imageLink=requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/160px-Deep_Blue.jpg')
print(imageLink.content)
f=open('computer.jpeg','wb')
f.write(imageLink.content)
f.close()
