from dataclasses import dataclass


@dataclass
class Session:
    id: int
    guild_id: str
    channel_id: str
    gm_user_id: str
    finished: bool


@dataclass
class SpellCast:
    id: int
    effect: str
    hidden: bool
    user_id: str
    session_id: int


@dataclass
class StoredSpellCast:
    id: int
    effect: str
    hidden: bool
    user_id: str
    session_id: int
