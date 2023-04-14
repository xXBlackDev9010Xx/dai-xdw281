import discord
from discord.ext import commands

class Say(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def say(self, ctx, *, msg=None):
    if msg == None:
      embed_error = discord.Embed(title="Error", description="Debes de agregar un mensaje", color=discord.Color.red())
      return await ctx.send(embed=embed_error)
    await ctx.message.delete()
    await ctx.send(msg)

async def setup(bot):
  await bot.add_cog(Say(bot))