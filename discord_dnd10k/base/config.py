import configparser as cp

_cfg = cp.ConfigParser()
_cfg.read("config.ini")


TOKEN = _cfg["CLIENT"]["TOKEN"]
PREFIX = _cfg["CLIENT"]["PREFIX"]

DATABASE_NAME = _cfg["DATABASE"]["DATABASE_NAME"]

