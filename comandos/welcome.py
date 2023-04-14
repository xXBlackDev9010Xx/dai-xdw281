import discord
import json
from discord import app_commands
from discord.ext import commands

class Welcome(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="setwelcome", description="Establecer bienvenidas")
  @commands.has_permissions(administrator=True)
  async def embed(self, interaction: discord.Interaction, *, channel: discord.TextChannel, msg: str):
    member = interaction.user
    if not member.guild_permissions.administrator:
      return

    with open("data.json", "r") as f:
      data = json.load(f)

    data = {
    "channel": str(channel.id),
    "msg": msg
    }

    with open("data.json", "w") as f:
      json.dump(data, f)

    replace_dict = {
      "[member.name]": member.name,
      "[member.mention]": member.mention,
      "[member.id]": str(member.id),
      "[member]": str(member),
      "[guild.name]": str(member.guild.name),
      "[guild.id]": str(member.guild.id),
      "[guild.count]": str(member.guild.member_count)
    }
    
    for key, value in replace_dict.items():
      msg = msg.replace(key, value)
    await interaction.response.send_message(f"Quedo de la siguiente manera:\n {msg}")

async def setup(bot):
  await bot.add_cog(Welcome(bot))