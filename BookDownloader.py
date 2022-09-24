import requests
from pathlib import Path


Path('books').mkdir(parents=True, exist_ok=True)



for id in range(1, 11):
    url = "https://tululu.org/txt.php?id={}".format(id)
    response = requests.get(url)
    response.raise_for_status() 

    filename = 'books/book{}.txt'.format(id)
    with open(filename, 'w') as file:
        file.write(response.text)