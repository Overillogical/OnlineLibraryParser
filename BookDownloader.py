import requests
from pathlib import Path
import logging

Path('books').mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename='log.log', format = '%(asctime)s %(message)s', encoding = 'utf-8', level = logging.WARNING)

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
        logging.warning(f'{repr(err)} Book id {id} is missing')
      