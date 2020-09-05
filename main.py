from discord.ext import commands
import discord
import yaml
import random
import time

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
    time.sleep(0.001)
    await ctx.send(random.choice(open('gifs.txt').readlines()))

bot.run(data['token'])
