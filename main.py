import requests
from bs4 import BeautifulSoup
# import csv


url_main = 'https://www.lego.com'
url_theme = 'https://www.lego.com/en-us/themes'


def get_soup(url):
    r = requests.get(url=url)
    return BeautifulSoup(r.text, 'html.parser')


def get_themes(soup):
    """Извлекать данные из набора"""
    themes = soup.find('section').ul  # ищем обращаемся к тегу
    themes = themes.find_all('li')    # собираем все теги li из тега ul

    themes_list = []

    for theme in themes:
        themes_dict = {
            'name': theme.h2.span.text,
            'url': f'{url_main}{theme.a.get("href")}'
        }

        themes_list.append(themes_dict)

    # Сохранение информации в csv файл
    # keys = themes_list[0].keys()
    # with open('themes.csv', 'w') as file:
    #     dict_writer = csv.DictWriter(file, keys)
    #     dict_writer.writeheader()
    #     dict_writer.writerows(themes_list)

    return themes_list


def main():
    soup = get_soup(url=url_theme)
    themes = get_themes(soup=soup)
    print(themes)


if __name__ == '__main__':
    main()
