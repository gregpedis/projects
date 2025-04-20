from bs4 import BeautifulSoup as bsoup
import requests as req
import multiprocessing as mp
import configparser
import shutil
import os

config = configparser.ConfigParser()
config.read('config.ini')

ROOT_FOLDER = os.getcwd()
INITIAL_URL = config['DEFAULT']['InitialUrl']


def set_folder_hierarchy():
    os.chdir(ROOT_FOLDER)
    #shutil.rmtree(config['FOLDERS']['Base'], True)

    os.makedirs(config['FOLDERS']['Base'], exist_ok=True)
    os.chdir(config['FOLDERS']['Base'])

    os.makedirs(config['FOLDERS']['Dataset'], exist_ok=True)
    os.chdir(config['FOLDERS']['Dataset'])


def is_valid_title(title):
    for ch in title:
        if ord(ch) > 126:
            return False
    return True


def soup_scraping(idx):
    url = INITIAL_URL + str(idx)

    try:
        print(f"PID {os.getpid()} - Initiating for page: {idx}")
        response = req.get(url, timeout=3)
    except:
        print(f"Request to {url} timed out.\n")
        return

    if not response:
        print(f"Response status code was {response.status_code}\n"
              + "Terminating extraction...\n")
        return

    soup = bsoup(response.content, "html.parser")

    ul_tag = soup.find('ul', {"id": "videoCategory"})
    if not ul_tag:
        print(f"Didn't find any videos on page {idx}. Exiting...\n")
        return

    li_list = ul_tag.find_all('li')

    with open(f'page_{idx}.txt', 'wb+') as f:
        for title in [li.find('a').get('title') for li in li_list]:
            if title and is_valid_title(title):
                f.write((title + '\n').encode())

    print(f'Finished for {idx}\n')


if __name__ == "__main__":

    pages = config['COUNT']['Page']
    print(f"\nPages to be harvested: [{pages}]\n")

    set_folder_hierarchy()
    idxs = range(1, int(pages)+1)

    # pool = mp.Pool(int(config['COUNT']['Core']))
    # pool.map(soup_scraping, idxs)

    for idx in idxs:
        soup_scraping(idx)

    print(f'\nDONE SCRAPPING THE LATIN-SPECIFIC TITLES FOR {pages} pages.\n\n')
