import configparser as cp
import cmd.levenshtein as lstein
import sys
import os
import json

this = sys.modules[__name__]

cfg = cp.ConfigParser()
cfg.read("config.ini")

PREFIX = cfg["client"]["prefix"]
FILES_DIRECTORY = cfg["DEFAULT"]["files_directory"]
CHAMPION_DIRECTORY = "champions"


def get_data(file_path):
    f = open(file_path)
    data = json.load(f)
    f.close()
    return data


def has_intersection(a, b):
    set1 = set([x.lower() for x in a])
    set2 = set([x.lower() for x in b])
    if set1 & set2:
        return True
    else:
        return False


def is_subset(small, big):
    sset = set([x.lower() for x in small])
    bset = set([x.lower() for x in big])
    if sset.issubset(bset):
        return True
    else:
        return False


def find_match(target, candidates):
    levens = [(k, lstein.get_distance(target, v))
              for k, v in candidates]

    key, distance = min(levens, key=lambda l: l[1])
    return key


def parse_input(message):
    msg = message.lower().split()
    if msg[0].startswith(PREFIX):
        cmd = msg[0].replace(PREFIX, "", 1)
        args = msg[1:]
        return (cmd, args)
    return ("", [])


def fix_output(message):
    result = "```md\n"
    result += message
    result += "```"
    return result
