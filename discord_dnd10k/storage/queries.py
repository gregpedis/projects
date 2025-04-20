
# sessions

START_SESSION = """
    insert into Session(GuildId, ChannelId, GameMasterUserId)
    values
    (?,?,?);
"""

END_SESSION = """
    update Session
    set Finished = 1
    where GuildId = ? and ChannelId = ?
"""

GET_SESSION = """
    select 
        s.Id,
        s.GuildId, 
        s.ChannelId,
        s.GameMasterUserId,
        s.Finished
    from Session as s
    where s.GuildId = ? and s.ChannelId = ?
    and s.Finished = 0
"""

# spell_casts

INSERT_SPELLCAST = """
    insert into SpellCast(Effect, UserId, SessionId, Hidden)
    values
    (?,?,?,?);
"""

GET_SPELLCASTS = """
    select sc.Id,
        sc.Effect,
        sc.Hidden,
        sc.UserId,
        sc.SessionId
    from SpellCast as sc
    where sc.SessionId = ? and sc.UserId = ?
    order by sc.Id desc
    limit ?
"""

GET_SPELLCAST = """
    select 
        sc.Id,
        sc.Effect,
        sc.Hidden,
        sc.UserId,
        sc.SessionId
    from SpellCast as sc
    where sc.Id = ?
"""

MARK_SPELLCAST_AS_VISIBLE = """
update SpellCast
set Hidden = 0
where Id = ?
"""

# stored_spellcasts

INSERT_STORED_SPELLCAST = """
    insert into StoredSpellCast(Effect, UserId, SessionId, Hidden)
    values
    (?,?,?,?);
"""

GET_STORED_SPELLCAST = """
    select 
        sc.Id,
        sc.Effect,
        sc.Hidden,
        sc.UserId,
        sc.SessionId
    from StoredSpellCast as sc
    where sc.Id = ?
"""

GET_STORED_SPELLCASTS = """
    select 
        sc.Id,
        sc.Effect,
        sc.Hidden,
        sc.UserId,
        sc.SessionId
    from StoredSpellCast as sc
    where sc.SessionId = ? and sc.UserId = ?
    order by sc.Id desc
    limit ?
"""

MARK_STORED_SPELLCAST_AS_VISIBLE = """
    update StoredSpellCast
    set Hidden = 0
    where Id = ?
"""

DELETE_STORED_SPELLCAST = """
    delete from StoredSpellCast
    where Id = ?
"""
