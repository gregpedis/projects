import random as rnd
import storage.database as db
from effects import NET_LIBRAM
import discord.ext.commands as commands


@commands.command()
async def roll_dimis(ctx):
    """hehehe"""
    choices = ["xontrelos", "mpiftekelos", "peroukelos", "skatelos"]
    msg = rnd.choice(choices)
    await ctx.send(msg)


@commands.command()
async def roll_dice(ctx, arg):
    """{number between 1 and 1000} - rolls a [number]-sized dice."""
    mention = ctx.author.mention
    try:
        dice_size = int(arg)
        if dice_size < 0:
            await ctx.send(f"Negative dies do not exist, _at least on this reality..._")
            return
        if dice_size > 1000:
            await ctx.send(f"That dice is way to phat for me.")
            return

        res = rnd.randint(1, dice_size)
        await ctx.send(f"{mention} is rolling a `d{dice_size}`...")
        await ctx.send(f"{mention} rolled a `{res}`!")
    except:
        await ctx.send(f"Hey, {mention}, come on dude. `{arg}` is not a valid dice.")


@commands.command()
async def roll_spicy(ctx):
    """rolls a net libram effect and DMs it to the Game Master."""
    if ctx.guild is None or ctx.channel is None:
        await roll_spicy_dm(ctx)
    else:
        await roll_spicy_server(ctx)


async def roll_spicy_server(ctx):
    g = ctx.guild.id
    c = ctx.channel.id
    u = ctx.author.id
    mention = ctx.author.mention

    running_session = db.get_session(g, c)
    if not running_session:
        await ctx.send(f"A session has not been started. Please start one with `session_start`.")
    else:
        effect = rnd.choice(NET_LIBRAM)
        spellcast = db.insert_spellcast(effect, u, running_session.id)
        gm = ctx.bot.get_user(int(running_session.gm_user_id))
        gm_msg = f"{mention} has rolled the following:\n Id: `{spellcast.id}`\nEffect: `{effect}`"
        await ctx.send(f"{mention} is rolling a spicy effect...")
        await gm.send(content=gm_msg)
        await ctx.send(f"The GM  has been notified. Keep going.")


async def roll_spicy_dm(ctx):
    effect = rnd.choice(NET_LIBRAM)
    await ctx.send(effect)
