import os
import cmd.operations as ops
import configparser as cp

cfg = cp.ConfigParser()
cfg.read("config.ini")

FILES_DIRECTORY = cfg["DEFAULT"]["files_directory"]

def item_command(args):
    if len(args) < 1:
        result = "Please specify an item as follows, you degenerate buffoon:\n"
        result += "# ^item [name]"
        return ops.fix_output(result)

    filepath = os.path.join(FILES_DIRECTORY, "items.json")
    data = ops.get_data(filepath)

    lookups = [(k, v["name"]) for k, v in data.items()]
    key = ops.find_match(" ".join(args), lookups)
    item = data[key]
    
    item["from"] = [] if item["from"] is None else item["from"]
    item["into"] = [] if item["into"] is None else item["into"]
    from_items = [v["name"]
                  for k, v in data.items()
                  if k in item["from"]]
    into_items = [v["name"]
                  for k, v in data.items()
                  if k in item["into"]]

    total_gold = str(item['gold']['total'])
    base_gold = str(item['gold']['base'])

    result = f"# {item['name']} < {total_gold}({base_gold}) >\n"
    result += f"> {item['tags']}\n"
    result += f"*{item['description'].strip()}*\n\n"
    result += f"* From: {from_items}\n"
    result += f"* Into: {into_items}\n"
    return ops.fix_output(result)
