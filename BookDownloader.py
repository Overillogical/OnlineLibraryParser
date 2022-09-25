import requests
from pathlib import Path
import logging
from pathvalidate import sanitize_filename
from bs4 import BeautifulSoup

Path('books').mkdir(parents=True, exist_ok=True)

def check_for_redirect(response, url):
    if response.history:
        raise requests.exceptions.HTTPError
    return

def download_txt(id, filename, folder="books/"):
    filename = f'{id}. {sanitize_filename(filename).strip()}.txt'
    filepath = f'{folder}{filename}'
    with open(filepath, 'w') as file:
            file.write(response.text) 
    return filepath

def parse_book_name(id):
    url = "https://tululu.org/b{}/".format(id)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    title_tag = soup.find('h1')
    book_name = title_tag.text.split('::', maxsplit=1)[0]
    return book_name


if __name__ == "__main__":
    for id in range(1, 11):
        url = "https://tululu.org/txt.php?id={}".format(id)
        response = requests.get(url)
        response.raise_for_status()
        try:
            check_for_redirect(response, url)
            filename = parse_book_name(id)
            download_txt(id, filename, folder="books/")
        except requests.exceptions.HTTPError as err:
            logging.exception('Book is not downloaded, redirect found')  
