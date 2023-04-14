import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional

class Embed(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def sync(self, ctx):
    await ctx.send("Se han actualizado los slash")
    synced = await self.bot.tree.sync(guild=ctx.guild)
    print(f"Slash synced {str(len(synced))} commands")

  @app_commands.command(name="embed", description="Para crear embeds")
  @commands.has_permissions(administrator=True)
  async def embed(self, interaction: discord.Interaction, *, title: str, author: str = None, author_url: str = None, description: str, image: str = None, thumbnail: str = None, footer: str = None,channel: discord.TextChannel, color: str = None):
    member = interaction.user
    if not member.guild_permissions.administrator:
      return
    if color == None:
      color = discord.Color.random()
    else:
      if not color.startswith("#"):
        color = "#" + color
        color = discord.Color.from_rgb(*(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)))
      else:
        color = discord.Color.from_rgb(*(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)))
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_author(name=f"{author}", icon_url=author_url)
    embed.set_footer(text=footer)
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    if image:
        embed.set_image(url=image)
    await channel.send(embed=embed)
    await interaction.response.send_message(f"Se ha enviado a {channel.mention}")



async def setup(bot):
  await bot.add_cog(Embed(bot))