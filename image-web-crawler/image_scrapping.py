from bs4 import BeautifulSoup
import requests as req
import uuid
import sys
import os
import re

IMAGE_FILE_FORMATS = {'.jpg', '.jpeg', '.jif', '.jpe',
                      '.png', '.bpm', '.gif', '.svg',
                      '.heif', '.heic'}

ROOT_FOLDER = "harvested_websites"
RELATIVE_FOLDER_PATH = "soup_folder"
IMAGES_FOLDER = "images"

SOUP_FILE = "pretty_soup.txt"
IMAGES_FILE = "soup_imgs.txt"
LINKS_FILE = "soup_links.txt"
LINKS_FILE_SEARCHABLE = "soup_links_searchable.txt"

URL_PREFIX_UNTRUSTED = "http://"
URL_PREFIX_1 = "https://"
URL_PREFIX_2 = "www."


def set_folder_hierarchy(folder_path):
    os.makedirs(ROOT_FOLDER, exist_ok=True)
    os.chdir(ROOT_FOLDER)

    os.makedirs(folder_path, exist_ok=True)
    os.chdir(folder_path)

    os.makedirs(IMAGES_FOLDER, exist_ok=True)


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
            if href:
                links_f.write((href + '\n').encode())

    with open(IMAGES_FILE, 'wb+') as imgs_f:
        for img_tag in b_soup.find_all('img'):
            img_src = img_tag.get('src')
            if img_src:
                imgs_f.write((img_src + '\n').encode())


def extract_soup_links(b_soup, url_parts):

    base_url = ''.join(url_parts[:-1])
    full_url = base_url + url_parts[-1]
    a_tags = b_soup.find_all('a')
    links = []

    for href in [a_tag.get('href').lower() for a_tag in a_tags if a_tag.get('href')]:
        if not href:
            continue
        elif href[0] == '#':
            continue
        elif URL_PREFIX_UNTRUSTED in href:
            continue
        elif URL_PREFIX_1 in href:
            links.append(href)
        elif href[0] == '/':
            links.append(base_url + href)
        else:
            links.append(full_url + href)

    with open(LINKS_FILE_SEARCHABLE, 'wb+') as links_f:
        for link in links:
            links_f.write((link + '\n').encode())


def extract_soup_images(b_soup, url_parts):
    base_url = ''.join(url_parts[:-1])
    full_url = base_url + url_parts[-1]
    img_tags = b_soup.find_all('img')

    for img_src in [img_tag.get('src').lower() for img_tag in img_tags if img_tag.get('src')]:
        if not img_src:
            continue
        elif URL_PREFIX_UNTRUSTED in img_src:
            continue
        elif URL_PREFIX_1 in img_src:
            image_url = img_src
        elif img_src[0] == '/':
            image_url = base_url + img_src
        else:
            image_url = full_url + img_src

        extract_image(image_url)


def extract_image(image_url):
    ext_idx = image_url.rfind('.')
    extension = image_url[ext_idx:]

    if extension not in IMAGE_FILE_FORMATS:
        return

    response = req.get(image_url)

    if response.status_code != 200:
        return

    img_name = str(uuid.uuid4())[:18]
    image_filename = img_name + extension

    image_path = os.path.join(IMAGES_FOLDER, image_filename)
    with open(image_path, "wb+") as f:
        f.write(response.content)


def soup_scraping(url, depth):
    url_parts = get_url_parts(url)

    folder_path = url_parts[1] + url_parts[3]
    folder_path = re.sub('[\/*:#-?"<>]','_',folder_path)   
    set_folder_hierarchy(folder_path)

    valid_url = ''.join(url_parts)

    response = req.get(valid_url)
    soup = BeautifulSoup(response.content, "html.parser")

    extract_soup_info(soup)
    extract_soup_links(soup, url_parts)
    extract_soup_images(soup, url_parts)

    with open(LINKS_FILE_SEARCHABLE, 'rt') as links_f:
        os.chdir('..')
        os.chdir('..')
        if depth > 0:
            url_childs = links_f.read().splitlines()
            for url_child in url_childs:
                soup_scraping(url_child, depth-1)


def parse_arguments(args):
    if len(args) < 1:
        return (None, 0)
    else:
        url = args[0]
        depth = int(args[1]) if len(args) >= 2 and int(args[1]) > 0 else 0
        return (url, depth)


if __name__ == "__main__":
    # Excluding the first argument,
    # since it's always the script's name.
    args = sys.argv[1:]
    (url, depth) = parse_arguments(args)

    if url:
        soup_scraping(url, depth)
    else:
        message = "\nWrong Arguments.\n"
        message += "Usage: [url] [depth (optional, defaults to 0)]\n"
        print(message)
