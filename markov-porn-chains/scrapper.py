from bs4 import BeautifulSoup
import requests as req
import configparser 
import os

config = configparser.ConfigParser()
config.read('config.ini')

asdf = config['COUNT']['Page']

BASE_FOLDER = "results"
DATASET_FOLDER = "dataset"
GENERATED_TITLES_FILE = "generated_titles.txt"

PAGES_COUNT = 2273
WORD_COUNT = 5
TITLES_GENERATED = 10

INITIAL_URL = "https://www.pornhub.com/video?page="

ROOT_FOLDER = os.getcwd()


def set_folder_hierarchy():
    os.chdir(ROOT_FOLDER)

    os.makedirs(config['FOLDERS']['Base'], exist_ok=True)
    os.chdir(config['FOLDERS']['Base'])

    os.makedirs(DATASET_FOLDER, exist_ok=True)
    os.chdir(DATASET_FOLDER)


def soup_scraping(page_idx):
    url = INITIAL_URL + str(page_idx)
    try:
        response = req.get(url, timeout=3)
    except:
        print("Request to " + url + " timed out.\n")
        return

    if not response:
        print("Response status code was " + str(response.status_code) +
              "\nTerminating extraction...\n")
        return

    soup = BeautifulSoup(response.content, "html.parser")

    ul_tag = soup.find('ul', {"id": "videoCategory"})
    li_list = ul_tag.find_all('li')

    with open('page_' + str(page_idx) + '.txt', 'wb+') as f:
        for title in [li.find('a').get('title') for li in li_list]:
            if title:
                f.write((title + '\n').encode())

        # for title in [li.find('a').get('title') for li in li_list]:
        #     pass


if __name__ == "__main__":

    print("\nPages to be harvested: [" + str(PAGES_COUNT) + "]")
    print("Titles generated word length: [" + str(WORD_COUNT) + "]")
    print("Titles generated count: [" + str(TITLES_GENERATED) + "]")

    set_folder_hierarchy()

    for idx in range(PAGES_COUNT):
        soup_scraping(idx + 1)
