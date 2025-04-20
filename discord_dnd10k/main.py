from base.config import TOKEN
from base.bot import BOT as bot 
from commands import *

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print("Ready for some rolls.")

# sessions
bot.add_command(session_start)
bot.add_command(session_end)

# rolls
bot.add_command(roll_dice)
bot.add_command(roll_spicy)
bot.add_command(roll_dimis)

# store
bot.add_command(store)
bot.add_command(use)
bot.add_command(stored)
bot.add_command(reveal_stored)

# history
bot.add_command(history)
bot.add_command(reveal_history)


bot.run(TOKEN)
