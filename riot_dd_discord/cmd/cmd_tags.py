import os
import configparser as cp
import cmd.operations as ops

cfg = cp.ConfigParser()
cfg.read("config.ini")

FILES_DIRECTORY = cfg["DEFAULT"]["files_directory"]


def tags_command(args):
    if len(args) < 1:
        result = "Please specify type of tag as follows, you lvl2 lee sin tower diver:\n"
        result += "# ^tags [champ/item]"
        return ops.fix_output(result)

    if args[0].lower().startswith("champ"):
        filepath = os.path.join(FILES_DIRECTORY, "champion_tags.json")
    elif args[0].lower().startswith("item"):
        filepath = os.path.join(FILES_DIRECTORY, "item_tags.json")
    else:
        return "Invalid tag type. Please search by `[champ]` or `[item]`."

    data = ops.get_data(filepath)
    results = [f"* {tag}" for tag in data["tags"]]
    result = "\n".join(results)
    
    result = ops.fix_output(result)
    return result
    