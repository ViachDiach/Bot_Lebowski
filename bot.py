import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
import asyncio
import time
import os

from discord_try import try_bot
from sinoptik import pogoda, lazyjob
from discord_try import mat, codwars, dushnila, total, check
from embeds import style

bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print('Hi, Lebowski')


@bot.command(name='help', hepl='узнать все команды')
async def use(ctx):     # список всех команд
    name = 'Мои команды:'
    report = '\n$weather ⛅ - погода в любом городе\n$money 💸 - курс ценных бумаг\n$skills 🖥️ - boss of the CodeWars' \
             '\n$puke 💨👃 - Слава не рыгун\n$zamat 🔞 - хто ты сьогоднi\n$stuffy 🤓 - На сколько % ты душный' \
             '\n$swap 🔄  - обменяться % душноты'

    type = await style(name, report)
    await ctx.send(embed=type)


@bot.command( pass_context=True)
async def money(ctx):       # курс валют
    dzen = await try_bot()
    author = ctx.message.author

    name = '💰 Сегодня курс:'
    report = (f'1 Доллар **$** = {dzen[0]} рубль ₽\n1 Евро € = {dzen[1]} рубль ₽\n1 Грывня ₴ = {dzen[2]} рубль ₽\n1 Тэнгэ ₸ = {dzen[3]} рубль ₽')

    type = await style(name, report)
    await ctx.send(author.mention, embed=type)


@bot.command()
async def zamat(ctx, victim=''):       # обзывалка
    author = ctx.message.author

    if len(victim) != 0:
        teg = victim
    else:
        teg = author.mention

    review = check(teg)             # проеряем проверялса ли уже
    if review == 'нужно провериться':
        name = 'Эээ нет!'
        report = 'Cперва проверься на $stuffy'
        type = await style(name, report)
        await ctx.send(teg, embed=type)
    else:
        xyi = mat(review)                     # проеряем кто он согласно процентам
        name = 'Ты сегодня... 🤔'
        report = xyi
        type = await style(name, report)
        await ctx.send(teg, embed=type)


    # xyi = mat()                      # проеряем кто он согласно процентам
    # name = 'Ты сегодня... 🤔'
    # report = xyi
    #
    # type = await style(name, report)
    # await ctx.send(teg, embed=type)


@bot.command()      # ебзделушка
async def puke(ctx):
    await ctx.send('<@531958734495154176> **НИКОГДА НЕ РЫГАЛ!!!**')


@bot.command()
async def weather(ctx, *, massage=' '):     # погода в некоторых городах

    #   ('*' указывает на то, что нужно взять в работу то, что находится после каманды WEATHER. В нашем случае город)

    news = await pogoda(massage)
    author = ctx.message.author

    name = news[0]
    report = (f'{news[1]}')

    type = await style(name, report)
    await ctx.send(author.mention, embed=type)


@bot.command()
async def skills(ctx, *, massage):
    author = ctx.message.author
    rank = await codwars(massage)

    name = 'Че кодишь, да? Красавчик! '
    report = rank

    type = await style(name, report)
    await ctx.send(author.mention, embed=type)


# @bot.command()
# async def work(ctx, *, massage):    # кто чем занят (парсинг из графаны)
#
#     job = await lazyjob(massage)
#     author = ctx.message.author
#     await ctx.send(f'{author.mention}, {job}')


@bot.command()
async def stuffy(ctx, victim=''):
    author = ctx.message.author

    if len(victim) != 0:
        teg = victim
    else:
        teg = author.mention

    dushno = dushnila(teg)

    if dushno == 'Уже взвешен':
        name = 'А вот все'
        report = (f'Ты уже вычеслен')
    else:
        name = 'На сколько % ты душный сегодня?'
        report = (f'🤓 Ты сегодня душный на {dushno} %🤓')

    type = await style(name, report)
    await ctx.send(teg, embed=type)


@bot.command()
async def swap(ctx, victim):
    author = ctx.message.author

    who = author.mention
    whom = victim

    msg = await ctx.send((f'{who}, {whom}'),
        embed=discord.Embed(title=(f'Вы готовы обненяться semen??')),
        components=[
            Button(style=ButtonStyle.green, label='That turns me on', emoji='😳'),
            Button(style=ButtonStyle.red, label='Fuck you', emoji='🖕')
        ]
    )

    response = await  bot.wait_for('button_click')
    if response.channel == ctx.channel:
        if response.component.label == 'That turns me on':
            await response.respond(content='🤵 Ganging up 🤵')

        else:
            await response.respond(content='Оh sh"t im sorry 😞')
            name = 'Садись в угол с гречкой, ты  сегодня'
            report = ('Фуфло явное')
            type = await style(name, report)
            await ctx.send(victim, embed=type)

    await msg.delete()


@bot.command()
async def list(ctx):
    spisok = total()
    await ctx.send(spisok)


token = ''

bot.run(token)
