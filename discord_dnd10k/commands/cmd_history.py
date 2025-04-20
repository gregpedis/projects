import discord.ext.commands as commands
import storage.database as db


@commands.command()
async def history(ctx, *args):
    """{number=10 between 1 and 100} - shows the last [number] casts of the user."""
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
        spellcasts = db.get_spellcasts(running_session.id, u,howmany)
        formatted = format_spellcasts(spellcasts)
        await ctx.send(f"Showing the last `{howmany}` spellcasts for player {m}:")
        await ctx.send(formatted)
    else:
        await ctx.send(f"No session is currently running on this channel.")


@commands.command()
async def reveal_history(ctx, arg):
    """{number} - reveals the cast with id=[number]."""
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
        elif session.gm_user_id != str(u):
            await ctx.send(f"Only the Game Master can reveal a spicy spell.")
        else:
            spellcast.hidden = False
            db.mark_spellcast_visible(spellcast_id)
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
    