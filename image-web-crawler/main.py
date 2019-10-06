from bs4 import BeautifulSoup
from datetime import datetime
import requests as req
import os
import shutil

RELATIVE_PATH = "images_folder_2"

os.makedirs(RELATIVE_PATH, exist_ok=True)
os.chdir(RELATIVE_PATH)
cwd = os.getcwd()

# Remove the entire subpath
# shutil.rmtree(RELATIVE_PATH)


url = "https://realpython.com/python-requests/"
response = req.get(url)
soup = BeautifulSoup(response.content, "html.parser")

with open("pretty_soup.txt", "wb+") as soup_f:
    pretty_soup = soup.prettify()
    soup_f.write(pretty_soup.encode())

with open("soup_links.txt", 'wb+') as links_f:
    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        if href is not None:
            links_f.write((href + '\n').encode())

with open("soup_imgs.txt", 'wb+') as imgs_f:
    for img_tag in soup.find_all('img'):
        img_src = img_tag.get('src')
        if img_src is not None:
            imgs_f.write((img_src + '\n').encode())

# f = open("something.txt","wb")
# f.write(response.content)
# f.close()

# url = "https://cdn4.buysellads.net/uu/1/49556/1566934724-graphics-04.jpg"
# response = req.get(url)

# ff = open('pic1.jpg', 'wb')
# ff.write(response.content)
# ff.close()

x = 1

if __name__ == "__main__":
    pass
