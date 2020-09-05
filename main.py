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

    message = await client.say(embed=embed)

    await bot.add_reaction(message, '\U+1F44D')
    await bot.add_reaction(message, '\U+1F49D')
    await bot.add_reaction(message, '\U+1F917')

bot.run(data['token'])
