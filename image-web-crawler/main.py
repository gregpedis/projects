from bs4 import BeautifulSoup
from datetime import datetime
import requests as req
import os
import shutil
import uuid
import re


ROOT_FOLDER = "harvested_websites"
RELATIVE_FOLDER_PATH = "soup_folder"
IMAGES_FOLDER = "images"

SOUP_FILE = "pretty_soup.txt"
LINKS_FILE = "soup_links.txt"
IMAGES_FILE = "soup_imgs.txt"

URL_PREFIX_1 = 'https://'
URL_PREFIX_2 = 'www.'


# Remove the entire subpath
# shutil.rmtree(A_DIRECTORY)


def set_folder_hierarchy(folder_path):
    os.makedirs(ROOT_FOLDER, exist_ok=True)
    os.chdir(ROOT_FOLDER)

    if folder_path is None:
        folder_path = RELATIVE_FOLDER_PATH

    full_path = os.path.join(folder_path, IMAGES_FOLDER)
    os.makedirs(full_path, exist_ok=True)
    os.chdir(folder_path)


def get_url_parts(url):
    prefix = URL_PREFIX_1 + URL_PREFIX_2
    stripped_url = url.replace(URL_PREFIX_1, '').replace(URL_PREFIX_2, '')

    sep = stripped_url.find('/')
    path = stripped_url[sep:]
    base_url = stripped_url[:sep]

    dot = base_url.rfind('.')
    suffix = base_url[dot:]
    name = base_url[:dot]
    return (prefix, name, suffix, path)


def extract_soup_info(b_soup):
    with open(SOUP_FILE, "wb+") as soup_f:
        pretty_soup = b_soup.prettify()
        soup_f.write(pretty_soup.encode())

    with open(LINKS_FILE, 'wb+') as links_f:
        for a_tag in b_soup.find_all('a'):
            href = a_tag.get('href')
            if href is not None:
                links_f.write((href + '\n').encode())

    with open(IMAGES_FILE, 'wb+') as imgs_f:
        for img_tag in b_soup.find_all('img'):
            img_src = img_tag.get('src')
            if img_src is not None:
                imgs_f.write((img_src + '\n').encode())


def extract_soup_images(b_soup, url_parts):
    os.chdir(IMAGES_FOLDER)

    base_url = ''.join(url_parts[:-1])
    full_url = base_url + url_parts[-1]
    img_tags = b_soup.find_all('img')

    for img_src in [img_tag.get('src') for img_tag in img_tags]:
        if img_src is None:
            continue
        # elif:
            # pass
        elif URL_PREFIX_1 in img_src:
            image_url = img_src
        elif img_src[0] == '/':
            image_url = base_url + img_src
        else:
            image_url = full_url + img_src

        extract_image(image_url)


def extract_image(image_url):
    response = req.get(image_url)

    img_name = str(uuid.uuid4())[:18]
    ext_idx = image_url.rfind('.')
    extension = image_url[ext_idx:]
    image_filename = img_name + extension

    with open(image_filename, "wb+") as f:
        f.write(response.content)


def soup_scraping(url):
    url_parts = get_url_parts(url)

    set_folder_hierarchy(url_parts[1])
    valid_url = ''.join(url_parts)

    response = req.get(valid_url)
    soup = BeautifulSoup(response.content, "html.parser")

    extract_soup_info(soup)
    extract_soup_images(soup, url_parts)


if __name__ == "__main__":

    url = "https://realpython.com/python-requests/"
    soup_scraping(url)
