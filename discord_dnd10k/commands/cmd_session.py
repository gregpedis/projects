import discord.ext.commands as commands
import storage.database as db


@commands.command()
async def session_start(ctx):
    """starts a session on this server's channel."""
    if ctx.guild is None or ctx.channel is None:
        await ctx.send(f"This command only works in a server channel.")
        return

    g = ctx.guild.id
    c = ctx.channel.id
    u = ctx.author.id

    running_session = db.get_session(g,c)
    if running_session:
        await ctx.send(f"Session `{running_session.id}` is already in progress.\n Finish it with `session_end` to start a new one.")
    else:
        session = db.start_session(g,c,u)
        await ctx.send(f"Session `{session.id}` has been started! GameMaster is {ctx.author.mention}.")


@commands.command()
async def session_end(ctx):
    """ends the running session of this server's channel."""
    g = ctx.guild.id
    c = ctx.channel.id
    u = ctx.author.id

    running_session = db.get_session(g,c)
    if not running_session:
        await ctx.send(f"No session is currently running on this channel.")
    else:
        gm = running_session.gm_user_id
        if str(u) != gm:
            await ctx.send(f"Only the GM can finish a session.")
        else:
            db.end_session(g, c)
            await ctx.send(f"Session `{running_session.id}` has ended.")
