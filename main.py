from discord.ext import commands
import discord
import yaml
import random

with open('config.yaml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

bot = commands.Bot(command_prefix='!')


@bot.command()
async def motivation(ctx):
    await ctx.send(random.choice(open('quotes.txt').readlines()))

bot.run(data['token'])
