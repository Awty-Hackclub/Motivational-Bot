from discord.ext import commands
import discord
import yaml
import random

with open('config.yaml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

bot = commands.Bot(command_prefix='!')


@bot.command()
async def motivation(ctx):
    embed = discord.Embed(
        title='Motivational Quote',
        description=random.choice(open('quotes.txt').readlines()),
        colour=discord.Colour.red()
    )
    
    await ctx.send(embed=embed)

bot.run(data['token'])