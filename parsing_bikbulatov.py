import requests
from bs4 import BeautifulSoup as bs

URL_DEPARTMENTS = "http://www.apmath.spbu.ru/ru/structure/depts/"
URL_TEACHERS = "http://www.apmath.spbu.ru/ru/staff/"


def find_depts():
    r = requests.get(URL_DEPARTMENTS)
    soup = bs(r.text, "html.parser")
    departments_names = soup.find_all('li')
    for name in departments_names:
        print('Кафедра {0}'.format(name.text))
        print('http://www.apmath.spbu.ru/ru/structure/depts/' + name.a['href'])


def find_teachers():
    r = requests.get(URL_TEACHERS)
    soup = bs(r.text, "html.parser")
    teacher_soups = soup.find_all('tr')
    for teacher_soup in teacher_soups:
        teacher_name = teacher_soup.find('td')
        if teacher_name:
            if teacher_name.find('a') is not None:
                print(teacher_name.text)
                print('http://www.apmath.spbu.ru/ru/staff/' + teacher_name.a['href'])
                print()
            else:
                print(teacher_name.text)
                print()


cmd = -1
while cmd != 0 and cmd != 1:
    print("Для получения списка кафедр введите 0, для получения списка преподователей введите 1")
    cmd = int(input())
    if not cmd:
        find_depts()
    elif cmd == 1:
        find_teachers()
    else:
        print("Команда не найдена")
