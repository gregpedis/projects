import os
import json
import shutil
from bs4 import BeautifulSoup
import requests
import configparser as cp


cfg = cp.ConfigParser()
cfg.read("config.ini")


FILES_DIRECTORY = cfg["DEFAULT"]["files_directory"]
CHAMPION_DIRECTORY = "champions"

REGION = cfg["DEFAULT"]["region"]
LANGUAGE = cfg["DEFAULT"]["language"]

REGION_EP = f"https://ddragon.leagueoflegends.com/realms/{REGION}.json"
VERSIONS_EP = "https://ddragon.leagueoflegends.com/api/versions.json"


response = requests.get(REGION_EP)
json_thing= response.json()
value = json_thing['v']

VERSION = requests.get(REGION_EP).json()['v']

CHAMPIONS_EP = f"http://ddragon.leagueoflegends.com/cdn/{VERSION}/data/{LANGUAGE}/champion.json"
CHAMPION_EP = f"http://ddragon.leagueoflegends.com/cdn/{VERSION}/data/{LANGUAGE}/champion"

ITEMS_EP = f"http://ddragon.leagueoflegends.com/cdn/{VERSION}/data/{LANGUAGE}/item.json"

CHAMPIONS_KEYS = ["key", "name", "title"]
CHAMPION_KEYS = ["name", "title", "lore", "allytips",
                 "enemytips", "tags", "partype", "stats", "spells", "passive"]

ITEM_KEYS = ["depth", "description", "from", "into",
             "gold", "name", "plaintext", "stats", "tags"]


def clean_files(folder):
    for f in os.listdir(folder):
        fp = os.path.join(folder, f)
        if os.path.isfile(fp) or os.path.islink(fp):
            os.remove(fp)


def initialize_repository():
    root_fullpath = FILES_DIRECTORY
    champions_fullpath = os.path.join(FILES_DIRECTORY, CHAMPION_DIRECTORY)
    try:
        os.mkdir(root_fullpath)
        os.mkdir(champions_fullpath)
    except FileExistsError as fee:
        pass

    clean_files(champions_fullpath)
    clean_files(root_fullpath)


def get_data(endpoint):
    res = requests.get(endpoint).json()["data"]
    res = remove_html(res)
    return res


def persist_data(data, filename):
    fullpath = os.path.join(FILES_DIRECTORY, filename)
    with open(fullpath, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)


def remove_keys(obj, rubbish):
    if isinstance(obj, dict):
        obj = {k: remove_keys(v, rubbish)
               for k, v in obj.items() if k not in rubbish}
    elif isinstance(obj, list):
        obj = [remove_keys(e, rubbish) for e in obj]
    return obj


def remove_html(thing):
    if isinstance(thing, str):
        soup = BeautifulSoup(thing, "html.parser")
        return soup.get_text(separator=" ")
    elif isinstance(thing, dict):
        res = {k: remove_html(v) for k,v in thing.items()}
        return res
    elif isinstance(thing, list):
        res = [remove_html(i) for i in thing]
        return res
    else:
        return thing


def get_champion_tags(champions):
    tags = [x["tags"] for x in champions.values()]
    distinct_tags = set([t for ts in tags for t in ts])
    persist_data({"tags": list(distinct_tags)},"champion_tags.json")


def get_champions():
    data = get_data(CHAMPIONS_EP)
    champions = {}
    for ckey, entry in data.items():
        champion = {}
        for key in CHAMPIONS_KEYS:
            champion[key] = entry.get(key, None)
        champions[ckey] = champion
    persist_data(champions, "champions.json")
    get_champion_tags(data)
    return data.keys()


def get_champion(champion_id):
    endpoint = f"{CHAMPION_EP}/{champion_id}.json"
    data = get_data(endpoint)[champion_id]
    champion = {}
    for key in CHAMPION_KEYS:
        champion[key] = data[key]
    champion = remove_keys(champion, ["image"])
    relative_path = os.path.join(CHAMPION_DIRECTORY, f"{champion_id}.json")
    persist_data(champion, relative_path)


def get_item_tags(items):
    tags = [x["tags"] for x in items.values()]
    distinct_tags = set([t for ts in tags for t in ts])
    persist_data({"tags": list(distinct_tags)},"item_tags.json")


def get_items():
    data = get_data(ITEMS_EP)
    items = {}
    for ikey, entry in data.items():
        item = {}
        for key in ITEM_KEYS:
            item[key] = entry.get(key, None)
        items[ikey] = item
    persist_data(items, "items.json")
    get_item_tags(items)


def main():
    initialize_repository()
    champion_ids = get_champions()
    for champion_id in champion_ids:
        get_champion(champion_id)
    get_items()


if __name__ == "__main__":
    main()
