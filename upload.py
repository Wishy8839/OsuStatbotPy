import discord
from time import sleep
from ossapi import Ossapi,UserLookupKey, GameMode, RankingType
from discord.ext import commands
from discord import app_commands
import os
intents = discord.Intents.all()
bot_id = ('YOUR BOT ID')
bot_secret = 'OSU SECRET TOKEN HERE'
api = Ossapi(bot_id, bot_secret)
token = 'TOKEN HERE'
Standardprefix = "!" #prefix in which the bot uses

bot = commands.Bot(command_prefix=Standardprefix, intents=intents, case_insensitive=True)
bot.remove_command('help') #removes the default help command


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



@bot.command() # Handles discord infomation
async def Osu(ctx, arg1):
    await ctx.send('Your requst for: {}  '.format(arg1))
    Player_Name = arg1
    Player_Rank = (api.user(arg1).statistics.global_rank)
    Player_PP = (api.user(arg1).statistics.pp)
    Player_PlayCount = (api.user(arg1).statistics.play_count)
    Player_Level = (api.user(arg1).statistics.level.current)
    Player_Avatar = (api.user(arg1).avatar_url)
    embedVar = discord.Embed(title="Osu Stats", description="their stats or smth", color=0x00ff00)
    embedVar.set_thumbnail(url=Player_Avatar)
    embedVar.add_field(name= "Name", value=Player_Name, inline=True)
    embedVar.add_field(name="Rank", value= Player_Rank, inline=True)
    embedVar.add_field(name="PP", value= Player_PP, inline=True)
    embedVar.add_field(name="Playercount", value= Player_PlayCount, inline=True)
    embedVar.add_field(name="Level", value= Player_Level, inline=True)
    await ctx.send(embed=embedVar)




bot.run(token)