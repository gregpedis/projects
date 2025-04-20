import sqlite3
import storage.schema as schema
import storage.queries as queries
from base.config import DATABASE_NAME


# sessions

def start_session(guild_id, channel_id, user_id) -> schema.Session:
    q = queries.START_SESSION
    args = (guild_id, channel_id, user_id)
    _execute(q, args)

    session = get_session(guild_id, channel_id)
    return session


def end_session(guild_id, channel_id) -> None:
    q = queries.END_SESSION
    args = (guild_id, channel_id)
    _execute(q, args)


def get_session(guild_id, channel_id) -> schema.Session:
    q = queries.GET_SESSION
    args = (guild_id, channel_id)
    res = _fetch(q, args)

    if not res:
        return None

    row = res[0]
    session = schema.Session(row[0], row[1], row[2], row[3], row[4])
    return session


# spell_casts

def get_spellcast(spellcast_id) -> schema.SpellCast:
    q = queries.GET_SPELLCAST
    args = (spellcast_id,)
    res = _fetch(q, args)

    if not res:
        return None

    row = res[0]
    sc = schema.SpellCast(row[0], row[1], row[2], row[3], row[4])
    return sc


def get_spellcasts(session_id, user_id, howmany=10) -> list:
    q = queries.GET_SPELLCASTS
    args = (session_id, user_id, howmany)
    res = _fetch(q, args)

    spellcasts = []
    for row in res:
        sc = schema.SpellCast(row[0], row[1], row[2], row[3], row[4])
        spellcasts.append(sc)
    return spellcasts


def insert_spellcast(effect, user_id, session_id, hidden=True) -> schema.SpellCast:
    q = queries.INSERT_SPELLCAST
    args = (effect, user_id, session_id, hidden)
    _execute(q, args)

    rows = get_spellcasts(session_id, user_id, 1)
    return rows[0]


def mark_spellcast_visible(spellcast_id) -> None:
    q = queries.MARK_SPELLCAST_AS_VISIBLE
    args = (spellcast_id,)
    _execute(q, args)


# stored spell_casts

def get_stored_spellcast(spellcast_id) -> schema.StoredSpellCast:
    q = queries.GET_STORED_SPELLCAST
    args = (spellcast_id,)
    res = _fetch(q, args)

    if not res:
        return None

    row = res[0]
    sc = schema.SpellCast(row[0], row[1], row[2], row[3], row[4])
    return sc


def get_stored_spellcasts(session_id, user_id, howmany=10) -> list:
    q = queries.GET_STORED_SPELLCASTS
    args = (session_id, user_id, howmany)
    res = _fetch(q, args)

    spellcasts = []
    for row in res:
        sc = schema.StoredSpellCast(row[0], row[1], row[2], row[3], row[4])
        spellcasts.append(sc)
    return spellcasts


def insert_stored_spellcast(effect, user_id, session_id, hidden) -> None:
    q = queries.INSERT_STORED_SPELLCAST
    args = (effect, user_id, session_id, hidden)
    _execute(q, args)


def mark_stored_spellcast_visible(spellcast_id) -> None:
    q = queries.MARK_STORED_SPELLCAST_AS_VISIBLE
    args = (spellcast_id,)
    _execute(q, args)

def delete_stored_spellcast(spellcast_id) -> None:
    q = queries.DELETE_STORED_SPELLCAST
    args = (spellcast_id,)
    _execute(q, args)


# internal

def _execute(query: str, parameters) -> None:
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    cur.execute(query, parameters)
    conn.commit()
    conn.close()


def _fetch(query: str, parameters):
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    cur.execute(query, parameters)
    res = cur.fetchall()
    conn.close()
    return res
