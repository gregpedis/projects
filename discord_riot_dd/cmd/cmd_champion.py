import os
import cmd.operations as ops
import configparser as cp

cfg = cp.ConfigParser()
cfg.read("config.ini")

FILES_DIRECTORY = cfg["DEFAULT"]["files_directory"]
CHAMPIONS_DIRECTORY = os.path.join(FILES_DIRECTORY, "champions")


def champion_command(args):
    if len(args) < 1:
        result = "Please specify a champion as follows, you subhuman ape:\n"
        result += "# ^champion [name]"
        return ops.fix_output(result)

    filepath = os.path.join(FILES_DIRECTORY, "champions.json")
    champions = ops.get_data(filepath)

    lookups = [(k, v["name"]) for k, v in champions.items()]
    key = ops.find_match(" ".join(args), lookups)
    champion_file = os.path.join(CHAMPIONS_DIRECTORY, f"{key}.json")
    champion = ops.get_data(champion_file)

    results = []
    general_data = f"# {champion['name']}\n"
    general_data += f"## {champion['title']}\n"
    general_data += f"> {champion['tags']}\n\n"

    general_data += f"<Spells>\n"
    for spell in champion["spells"]:
        general_data += f"* {spell['name']}\n"
    general_data += "\n"

    general_data += f"<Stats>\n"
    for k, v in champion["stats"].items():
        general_data += f"* {k.ljust(25)} {'->'.ljust(5)} {str(v)}\n"
    general_data += "\n"

    results.append(ops.fix_output(general_data))

    random_stuff = f"# {champion['name']}\n"
    random_stuff += f"<Lore>\n"
    random_stuff += f"* {champion['lore']}\n\n"

    random_stuff += "<Ally Tips>\n"
    for tip in champion['allytips']:
        random_stuff += f"* {tip}\n"
    random_stuff += "\n"

    random_stuff += "<Enemy Tips>\n"
    for tip in champion['enemytips']:
        random_stuff += f"* {tip}\n"
    random_stuff += "\n"

    results.append(ops.fix_output(random_stuff))

    return results
