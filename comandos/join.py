import discord
import json
import easy_pil

from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
from unidecode import unidecode

class join(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
    with open("data.json", "r") as f:
      data = json.load(f)
    channel_id = int(data["channel"])
    msg = data["msg"]
    canal = self.bot.get_channel(channel_id)
    background = Editor("fondo.png")
    name = str(member)
    name_normal = unidecode(name)
    profile_image = None
    if member.avatar:
      profile_image = await load_image_async(str(member.avatar))
    else:
      profile_image = await load_image_async(str(member.default_avatar))
    profile = Editor(profile_image).resize((200,200)).circle_image()
    font = Font("Minecrafter.Alt.ttf",size=60)
    font2 = Font("Minecrafter.Alt.ttf",size=45)
  
    background.paste(profile, (440,150))
    background.ellipse((440, 150), 200, 200, outline="white",stroke_width=5)
    background.text((550,400), f"Bienvenido a Daios", color="white", font=font, align="center")
    background.text((550,465), f"{name_normal}", color="white", font=font2, align="center")
    file = File(fp=background.image_bytes, filename="fondo.png")

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
    await canal.send(f"{msg}",file=file)
    

async def setup(bot):
  await bot.add_cog(join(bot))