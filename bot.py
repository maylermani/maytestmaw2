import discord
import os
import random

client = discord.Client()

img1 = 'https://static.wikia.nocookie.net/leagueoflegends/images/3/35/Kog%27Maw_Pug%27MawSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20210922235126'
img2 = 'https://static.wikia.nocookie.net/leagueoflegends/images/b/b2/Kog%27Maw_MonarchSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20181021120652'
img3 = 'https://static.wikia.nocookie.net/leagueoflegends/images/0/01/Kog%27Maw_LionDanceSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20181021042930'
img4 = 'https://static.wikia.nocookie.net/leagueoflegends/images/3/30/Kog%27Maw_JurassicSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20181021104244'
img5 = 'https://static.wikia.nocookie.net/leagueoflegends/images/4/4e/Kog%27Maw_ArcanistSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20210922235242'
img6 = 'https://static.wikia.nocookie.net/leagueoflegends/images/b/b1/Kog%27Maw_BattlecastSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20181021120624'
img7 = 'https://static.wikia.nocookie.net/leagueoflegends/images/1/19/Kog%27Maw_OriginalSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20181021103708'

baklazhan = "https://808.media/wp-content/uploads/2021/11/baklazhan-1.gif"

ragnaros = "https://thumbs.gfycat.com/FlatElegantArmedcrab-size_restricted.gif"

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!maw'):
    await message.channel.send(random.choice([img2, img1, img3, img4, img5, img6, img7]))

  if message.content.startswith('!хуй'):
    await message.channel.send(baklazhan)

  if message.content.startswith('!злюся'):
    await message.channel.send(ragnaros)

client.run(os.getenv('TOKEN'))