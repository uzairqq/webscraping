from asyncore import read
from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find('h5')
    tagsWithText = soup.find('h5').text
    print(tags)
    print(tagsWithText)
