import discord
import os
import googleapiclient.discovery
import asyncio
from discord.ext import commands, tasks
from discord.ext.tasks import loop


class Prueba(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=os.environ["API_TOKEN"])
        self.last_video_id = None
        self.anuncio = None
        self.general = None
        self.check_for_new_videos.start()

    async def get_latest_video(self):
        channel_id = "UCH5itcOcRpJCNjKeKzOdyFA"
        request = self.youtube.search().list(
            part="id",
            q="",
            channelId=channel_id,
            type="video,short",
            order="date"
        )
        response = request.execute()
        if "items" in response:
            video_id = response["items"][0]["id"]["videoId"]
            if video_id != self.last_video_id:
                self.last_video_id = video_id
                self.anuncio = f"<@703411168064176142> ¡Nuevo video de Daios! https://www.youtube.com/watch?v={video_id}"

    @tasks.loop(minutes=1)
    async def check_for_new_videos(self):
        await self.get_latest_video()
        if self.anuncio is not None and self.general is not None:
            await self.general.send(self.anuncio)

    @commands.command()
    async def prueba(self, ctx):
        await ctx.send("Este comando ya no se utiliza.")

    def cog_unload(self):
        self.check_for_new_videos.cancel()


async def setup(bot):
    prueba_cog = Prueba(bot)
    prueba_cog.general = bot.get_channel(1082495760886677525)
    await bot.add_cog(prueba_cog)
