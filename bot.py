import discord
from discord.ext import commands
from modelo import get_class
import os, random

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import requests

intents = discord.Intents.default()  # Asegúrate de habilitar los intents necesarios en el portal de desarrolladores de Discord
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, {bot.user}!, soy un bot clasificador de imágenes.')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{attachment.filename}')
            res = get_class(
                model_path='./keras_model.h5',
                labels_path='labels.txt',
                image_path=f'./{attachment.filename}'
            )
            await ctx.send(f"{res}")

    else:
        await ctx.send("Olvidaste subir la imagen !!!")

bot.run("")
