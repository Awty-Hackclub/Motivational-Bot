from discord.ext import commands
import yaml

with open('config.yaml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    token = data['token']

bot = commands.Bot(command_prefix='!')

@bot.command()
async def motivation(ctx):
    ...

bot.run(token)


