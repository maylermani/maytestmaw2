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
zluzyaCat = "http://img2.joyreactor.cc/pics/comment/%D0%B3%D0%B8%D1%84%D0%BA%D0%B0-%D0%BA%D0%BE%D1%82%D1%8D-%D1%80%D1%83%D0%BA%D0%B0-%D0%B7%D0%B0%D0%B4%D1%83%D0%BC%D0%B0%D0%BB%D1%81%D1%8F-2422589.gif"

cat1 = "https://i.gifer.com/1Rda.gif"
cat2 = "https://i.gifer.com/sSD.gif"
cat3 = "https://i.gifer.com/1Cs3.gif"
cat4 = "https://i.gifer.com/MAOR.gif"
cat5 = "https://i.gifer.com/7ZFG.gif"
cat6 = "https://i.gifer.com/Aq.gif"
cat7 = "https://i.gifer.com/v5T.gif"
cat8 = "https://i.gifer.com/WU7.gif"
cat9 = "https://img.btdmp.com/files/10224256/2021/09/18/16319758899dce7d9360.gif" 
cat10 = "https://i.gifer.com/3Qe6.gif"
cat11 = "https://i.gifer.com/JtaW.gif"
cat12 = "https://i.gifer.com/11tv.gif"
cat13 = "https://i.gifer.com/Ao.gif"
cat14 = "https://c.tenor.com/Ls7KslPkMqYAAAAd/surprised-cat-omg-wow.gif"

testcat = "https://c.tenor.com/Ls7KslPkMqYAAAAd/surprised-cat-omg-wow.gif"

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
    await message.channel.send(random.choice([ragnaros, zluzyaCat]))

  if message.content.startswith('!кот'):
    await message.channel.send(random.choice([cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10, cat11, cat12, cat13, cat14]))

  if message.content.startswith('!ntcnrjn'):
    await message.channel.send(testcat)

client.run(os.getenv('TOKEN'))