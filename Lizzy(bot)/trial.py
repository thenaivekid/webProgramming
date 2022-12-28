#final code has not been tested
# It listens to sad messages and sends encouragements
# It responds to "$inspire" text with encouraging quotes

import discord,random

from decouple import config

from discord.ext import commands


bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    print(', '.join(dice))
    await ctx.send(', '.join(dice))


@bot.command(name='newchannel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


bot.run(config('TOKEN'))