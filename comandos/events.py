import discord
import random
from discord import app_commands
from discord.ext import commands, tasks


class events(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.bot.user} esta encendido")
    await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"@Daios7234"))
    await self.bot.tree.sync()

    


async def setup(bot):
  await bot.add_cog(events(bot))