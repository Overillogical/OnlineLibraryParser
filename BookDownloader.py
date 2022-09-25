import requests
from pathlib import Path
import logging
from pathvalidate import sanitize_filename
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse, urlsplit, unquote_plus



def check_for_redirect(response, url):
    if response.history:
        raise requests.exceptions.HTTPError
    return

def download_txt(id, response, url, folder="books/"):
    Path('books').mkdir(parents=True, exist_ok=True)
    check_for_redirect(response, url)
    filename = parse_book_name(id)
    filename = f'{id}. {sanitize_filename(filename).strip()}.txt'
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w') as file:
        file.write(response.text) 
    return filepath

def download_img(id, book_img_link, folder="images/"):
    response = requests.get(book_img_link)
    Path('images').mkdir(parents=True, exist_ok=True)
    filename = urlsplit(book_img_link).path.split('/')[-1]
    filepath = os.path.join(folder, filename)
    print(response.url)
    with open(filepath, 'wb') as file:
        file.write(response.content) 
    return


def parse_book_name(id):
    url = "https://tululu.org/b{}/".format(id)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    title_tag = soup.find('h1')
    book_name = title_tag.text.split('::', maxsplit=1)[0]
    print('Заголовок: {}'.format(book_name))
    return book_name

def parse_book_img(id):
    url = "https://tululu.org/b{}/".format(id)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    book_img = urljoin('https://tululu.org/', soup.find(class_='bookimage').find('img')['src'])
    return book_img

def main():
    for id in range(1, 11):
        url = "https://tululu.org/txt.php?id={}".format(id)
        response = requests.get(url)
        response.raise_for_status()
        try:
            download_txt(id, response, url, folder="books/")
            book_img_link = parse_book_img(id)    
            download_img(id, book_img_link, folder="images/")
        except requests.exceptions.HTTPError as err:
            logging.exception('Book is not downloaded, redirect found')  
        


if __name__ == "__main__":
    main()
    