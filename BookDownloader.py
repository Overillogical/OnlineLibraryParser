import requests
from pathlib import Path
import logging

Path('books').mkdir(parents=True, exist_ok=True)


def check_for_redirect(response, url):
    if response.url != url:
        raise requests.exceptions.HTTPError
    return




for id in range(1, 11):
    url = "https://tululu.org/txt.php?id={}".format(id)
    response = requests.get(url)
    response.raise_for_status() 
    filename = 'books/book{}.txt'.format(id)
    try:
        check_for_redirect(response, url)
        with open(filename, 'w') as file:
            file.write(response.text)  
    except requests.exceptions.HTTPError as err:
        logging.error(err, exc_info=True)