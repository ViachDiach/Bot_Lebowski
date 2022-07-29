import discord
from discord.ext import commands
import random


async def style(name, report):

    embed=discord.Embed(title=(f'{name}'),
                        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                        description=(f'{report}'),
                        color=0xFF5733)

    return (embed)

