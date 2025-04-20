import os
import configparser as cp
import cmd.operations as ops

cfg = cp.ConfigParser()
cfg.read("config.ini")

FILES_DIRECTORY = cfg["DEFAULT"]["files_directory"]


def items_command(args):
    if len(args) < 1:
        result = "Please specify item tag(s) as follows, you uncultured swine:\n"
        result += "# ^items [tag1 tag2 tag3...]"
        return ops.fix_output(result)

    filepath = os.path.join(FILES_DIRECTORY, "items.json")
    data = ops.get_data(filepath)

    entries = []

    for tag in args:
        entry = tag, get_item_names_by_tag(data, tag)
        entries.append(entry)

    if len(args) > 1:
        entry = args, get_item_names_by_tags(data, args)
        entries.append(entry)

    results = []

    for entry in entries:
        key, items = entry
        result = f"# {key}\n"
        for item in items:
            result += f"* {item}\n"
        result = ops.fix_output(result)
        results.append(result)
    return results


def get_item_names_by_tag(data, tag):
    items = [v for v in data.values()
             if is_subset([tag], v["tags"])]
    result = set([v["name"] for v in items])
    return list(result)


def get_item_names_by_tags(data, tags):
    items = [v for v in data.values()
             if is_subset(tags, v["tags"])]
    result = set([v["name"] for v in items])
    return list(result)


def is_subset(small, big):
    return ops.is_subset(small, big)
