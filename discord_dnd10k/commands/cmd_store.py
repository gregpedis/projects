import random as rnd
import storage.database as db
import discord.ext.commands as commands


@commands.command()
async def store(ctx, arg):
    """{number} - stores the cast with id=[number]."""
    if ctx.guild is None or ctx.channel is None:
        await ctx.send(f"This command only works in a server channel.")
        return
    
    g = ctx.guild.id
    c = ctx.channel.id
    u = ctx.author.id

    try:
        spellcast_id = int(arg)
        session = db.get_session(g,c)
        spellcast = db.get_spellcast(spellcast_id)
        if session is None:
            await ctx.send(f"No session is currently running on this channel.")
        elif spellcast is None or session.id != spellcast.session_id:
            await ctx.send(f"No spellcast with id=`{spellcast_id}` was found for session `{session.id}`.")
        elif spellcast.user_id!= str(u):
            await ctx.send(f"Only the Player can store a spicy spell they have casted.")
        else:
            db.insert_stored_spellcast(spellcast.effect, spellcast.user_id, spellcast.session_id, spellcast.hidden)
            await ctx.send(f"A spell cast has been stored for player {ctx.author.mention}.")
            formatted = format_spellcasts([spellcast])
            await ctx.send(formatted)
    except:
        await ctx.send(f"`{arg}` is not a valid spellcast id. Please use a valid number.")


@commands.command()
async def use(ctx, arg):
    """{number} - uses the stored cast the cast with id=[number]."""
    if ctx.guild is None or ctx.channel is None:
        await ctx.send(f"This command only works in a server channel.")
        return
    
    g = ctx.guild.id
    c = ctx.channel.id
    u = ctx.author.id

    try:
        stored_spellcast_id = int(arg)
        session = db.get_session(g,c)
        stored_sc = db.get_stored_spellcast(stored_spellcast_id)
        if session is None:
            await ctx.send(f"No session is currently running on this channel.")
        elif stored_sc is None or session.id != stored_sc.session_id:
            await ctx.send(f"No stored spellcast with id=`{stored_sc.id}` was found for session `{session.id}`.")
        elif stored_sc.user_id!= str(u):
            await ctx.send(f"Only the Player can use a spicy spell they have stored.")
        else:
            db.insert_spellcast(stored_sc.effect + " (stored)", stored_sc.user_id, stored_sc.session_id, stored_sc.hidden)
            db.delete_stored_spellcast(stored_sc.id)
            await ctx.send(f"A stored spell cast has been used for player {ctx.author.mention}.")
            formatted = format_spellcasts([stored_sc])
            await ctx.send(formatted)

    except:
        await ctx.send(f"`{arg}` is not a valid spellcast id. Please use a valid number.")


@commands.command()
async def stored(ctx, *args):
    """{number=10 between 1 and 100} - shows the last [number] stored casts of the user."""
    if ctx.guild is None or ctx.channel is None:
        await ctx.send(f"This command only works in a server channel.")
        return
    
    howmany = 10
    try:
        howmany = int(args[0])
    except:
        pass

    g = ctx.guild.id
    c = ctx.channel.id
    u = ctx.author.id
    m = ctx.author.mention

    running_session = db.get_session(g,c)
    if running_session:
        spellcasts = db.get_stored_spellcasts(running_session.id, u,howmany)
        formatted = format_spellcasts(spellcasts)
        await ctx.send(f"Showing the last `{howmany}` stored spellcasts for player {m}:")
        await ctx.send(formatted)
    else:
        await ctx.send(f"No session is currently running on this channel.")


@commands.command()
async def reveal_stored(ctx, arg):
    """{number} - reveals the stored cast with id=[number]."""
    if ctx.guild is None or ctx.channel is None:
        await ctx.send(f"This command only works in a server channel.")
        return
    
    g = ctx.guild.id
    c = ctx.channel.id
    u = ctx.author.id

    try:
        spellcast_id = int(arg)
        session = db.get_session(g,c)
        spellcast = db.get_stored_spellcast(spellcast_id)
        if session is None:
            await ctx.send(f"No session is currently running on this channel.")
        elif spellcast is None or session.id != spellcast.session_id:
            await ctx.send(f"No stored spellcast with id=`{spellcast_id}` was found for session `{session.id}`.")
        elif session.gm_user_id != str(u):
            await ctx.send(f"Only the Game Master can reveal a spicy stored spell.")
        else:
            spellcast.hidden = False
            db.mark_stored_spellcast_visible(spellcast_id)
            formatted = format_spellcasts([spellcast])
            await ctx.send(formatted)
    except:
        await ctx.send(f"`{arg}` is not a valid spellcast id. Please use a valid number.")


def format_spellcasts(spellcasts):
    if len(spellcasts) == 0:
        return "```md\n EMPTY\n```"
    res = "```md\n"
    for sc in spellcasts:
        res+= f"#Id = {sc.id}\n"
        res+= "(???)\n\n" if sc.hidden else f"{sc.effect}\n\n"
    res += "```"
    return res
