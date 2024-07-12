import discord
import random
from discord.ext import commands
from bot_logic import gen_pass
import os
from model import get_class
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):  # $hello
    await ctx.send(f'Привет! как дела?)')


@bot.command()
async def password(ctx): # $password
    await ctx.send(gen_pass(20))

@bot.command()
async def heh(ctx, count_heh = 5): # $heh 10
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def mem1(ctx):
    with open('images/mem2.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open('images/mem3 (1).jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    with open('images/mem3.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def rd(ctx):

    spisok = os.listdir('images')
    random_img = random.choice(spisok)

    with open(f'images/{random_img}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!

    await ctx.send(file=picture)





########
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    #'''По команде duck вызывает функцию get_duck_image_url'''
    url = get_duck_image_url()
    await ctx.send(url)


@bot.command()
async def podelka(ctx):

    spisok = os.listdir('podelka')
    random_img = random.choice(spisok)

    with open(f'podelka/{random_img}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def sovet(ctx):

    spisok2 = os.listdir('sovet')
    random_sovet = random.choice(spisok2)

    with open(f'sovet/{random_sovet}', 'r') as a:
        sov = discord.File(a)

    await ctx.send

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
            
    else:
        await ctx.send("Вы забыли загрузить картинку :(")

        
bot. run ("MTIwMDgwNjE4MjQ1NDA1NDk1Mg.G4gEZc.Go-SfuK4lRAHzZFiICCPUSSV3BPfFvQ9cIYCho")
    
