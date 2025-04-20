import os
import configparser as cp
import cmd.operations as ops

cfg = cp.ConfigParser()
cfg.read("config.ini")

FILES_DIRECTORY = cfg["DEFAULT"]["files_directory"]
CHAMPIONS_DIRECTORY = os.path.join(FILES_DIRECTORY, "champions")


def champions_command(args):
    if len(args) < 1:
        result = "Please specify champion tag(s) as follows, you omega feeder:\n"
        result += "# ^champions [tag1 tag2 tag3...]"
        return ops.fix_output(result)

    filepath = os.path.join(FILES_DIRECTORY, "champions.json")
    names = [k for k, v in ops.get_data(filepath).items()]

    champions = {name: ops.get_data(os.path.join(CHAMPIONS_DIRECTORY, f"{name}.json"))
                 for name in names}

    entries = []

    for tag in args:
        entry = tag, get_champion_names_by_tag(champions, tag)
        entries.append(entry)

    if len(args) > 1:
        entry = args, get_champion_names_by_tags(champions, args)
        entries.append(entry)

    results = []

    for key, champions in entries:
        result = f"# {key}\n"
        for champion in champions:
            result += f"* {champion}\n"
        result = ops.fix_output(result)
        results.append(result)
    return results


def get_champion_names_by_tag(data, tag):
    items = [v for v in data.values()
             if is_subset([tag], v["tags"])]
    result = set([v["name"] for v in items])
    return list(result)


def get_champion_names_by_tags(data, tags):
    items = [v for v in data.values()
             if is_subset(tags, v["tags"])]
    result = set([v["name"] for v in items])
    return list(result)


def is_subset(small, big):
    return ops.is_subset(small, big)
