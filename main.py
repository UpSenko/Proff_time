# Imports  Here :)

import discord 
from discord import discord.commands.ext

intent =  discord.Intent.all()

bot=discord.commands(command_prefix="w", Intents=Intents)

@bot.event
def on_ready():
  print(bot.user)

if __main__== "__main__":
  bot.run('MTAyOTk0NDQ2MzA1OTA3NTE2Mg.GT03Y3.SriTYAboQXuevfTxWQgKTklKJ_FmhqwtFHfrH4')
