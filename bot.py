import discord  #импортирует библиотеку discord.py
import os #импортирует библиотеку os, но она используется только для получения переменной TOKEN из файла .env

client = discord.Client()   #связь с Discord. Декоратор @client.event() используется для регистрации события.

@client.event
async def on_ready():  #бот готов к использованию
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):  #бот получает сообщение
    if message.author == client.user: #если сообщение от самих себя 
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    client.run(os.getenv('TOKEN'))  