import cmd.operations as ops


def help_command(args):
    helptext = "# Here are the available commands.\n\n"
    helptext+="[Prefix](^)\n\n"

    helptext+= "* champions [tag1 tag2 tag3...]\n"
    helptext+= "> lists the champions matching each tag and the subset matching all of them.\n"

    helptext+= "* champion [name]\n"
    helptext+= "> shows some generic information about a champion.\n"

    helptext+= "* items [tag1 tag2 tag3...]\n"
    helptext+= "> lists the items matching each tag and the subset matching all of them.\n"

    helptext+= "* item [name]\n"
    helptext+= "> shows some generic information about an item.\n"

    helptext+= "* tags [champ/item]\n"
    helptext+= "> shows the category tags for the champions/items.\n"

    helptext+= "* spell [champion] [name]\n"
    helptext+= "> shows some generic information about a spell of a champion.\n"

    helptext+= "* kraken\n"
    helptext+= "> shows the truth.\n"

    helptext+= "* help\n"
    helptext+= "> shows this help message.\n"

    return ops.fix_output(helptext)
