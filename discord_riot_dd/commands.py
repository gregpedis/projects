import configparser as cp
import sys
import os
import cmd

this= sys.modules[__name__]
cmd_module = sys.modules["cmd"]

cfg = cp.ConfigParser()
cfg.read("config.ini")

PREFIX = cfg["client"]["prefix"]


def parse_input(message):
    msg = message.lower().split()
    if msg[0].startswith(PREFIX):
        cmd = msg[0].replace(PREFIX, "", 1)
        args = msg[1:]
        return (cmd, args)
    return ("", [])


def execute_command(message):
    cmd, args = parse_input(message)
    command = getattr(cmd_module, f"{cmd}_command")
    result = command(args)
    return result
