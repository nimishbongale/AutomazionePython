from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Enter the full url of the website to get its HTML code: ");
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)
h1 = soup.html
print(h1)



