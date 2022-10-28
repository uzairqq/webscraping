from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    all_course_cards = soup.find_all('div', class_='card')
    for course_card in all_course_cards:
        course_name = course_card.h5.text
        course_price = course_card.a.text.split()[-1]

        print(f'{course_name} cost {course_price}')
