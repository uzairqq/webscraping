from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    all_course_cards = soup.find_all('div', class_='card')
    for course_card in all_course_cards:
        print(course_card)
