import discord
import os
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="d-", intents=discord.Intents.all())
bot.remove_command("help")

discord.utils.setup_logging()

async def load():
  for filename in os.listdir("./comandos"):
    if filename.endswith(".py"):
      await bot.load_extension(f"comandos.{filename[:-3]}")
      print(f"Cargando comando {filename}")



async def main():
  await load()
  await bot.start(os.environ["DISCORD_TOKEN"])

asyncio.run(main())