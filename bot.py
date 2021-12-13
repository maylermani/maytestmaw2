import discord
import os
import random

client = discord.Client()

maws = ['https://static.wikia.nocookie.net/leagueoflegends/images/3/35/Kog%27Maw_Pug%27MawSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20210922235126','https://static.wikia.nocookie.net/leagueoflegends/images/b/b2/Kog%27Maw_MonarchSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20181021120652', 'https://static.wikia.nocookie.net/leagueoflegends/images/0/01/Kog%27Maw_LionDanceSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20181021042930','https://static.wikia.nocookie.net/leagueoflegends/images/3/30/Kog%27Maw_JurassicSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20181021104244','https://static.wikia.nocookie.net/leagueoflegends/images/4/4e/Kog%27Maw_ArcanistSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20210922235242','https://static.wikia.nocookie.net/leagueoflegends/images/b/b1/Kog%27Maw_BattlecastSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20181021120624','https://static.wikia.nocookie.net/leagueoflegends/images/1/19/Kog%27Maw_OriginalSkin.jpg/revision/latest/scale-to-width-down/1000?cb=20181021103708']

baklazhan = "https://808.media/wp-content/uploads/2021/11/baklazhan-1.gif"

ragnaros = ["https://thumbs.gfycat.com/FlatElegantArmedcrab-size_restricted.gif","http://img2.joyreactor.cc/pics/comment/%D0%B3%D0%B8%D1%84%D0%BA%D0%B0-%D0%BA%D0%BE%D1%82%D1%8D-%D1%80%D1%83%D0%BA%D0%B0-%D0%B7%D0%B0%D0%B4%D1%83%D0%BC%D0%B0%D0%BB%D1%81%D1%8F-2422589.gif",
"https://media.discordapp.net/attachments/862570143754223626/919885148508528640/-.gif"]

cats = ["https://media.discordapp.net/attachments/862570143754223626/919840530131718194/happy-kitty.gif","https://media.discordapp.net/attachments/862570143754223626/919840624470024202/smiling-cat-creepy-cat.gif", "https://media.discordapp.net/attachments/862570143754223626/919856864043352114/Ao.gif?width=603&height=603", "https://media.discordapp.net/attachments/862570143754223626/919857441372532746/surprised-cat-omg-wow.gif", "https://media.discordapp.net/attachments/862570143754223626/919862131061571634/3Qe6.gif","https://media.discordapp.net/attachments/862570143754223626/919862131506159647/WU7.gif","https://media.discordapp.net/attachments/862570143754223626/919862425707249684/v5T.gif","https://media.discordapp.net/attachments/862570143754223626/919862829920686110/funny-cat-2020-19.gif?width=426&height=603","https://media.discordapp.net/attachments/862570143754223626/919862858072866827/funny-cat-59.gif","https://media.discordapp.net/attachments/862570143754223626/919863003841695754/funny-cat-2020-9.gif","https://media.discordapp.net/attachments/862570143754223626/919863021726232596/funny-cat-2020-10.gif?width=524&height=603","https://media.discordapp.net/attachments/862570143754223626/919863211799486474/funny-cat-2020-14.gif","https://media.discordapp.net/attachments/862570143754223626/919863225653276722/funny-cat-2020-21.gif", "https://media.discordapp.net/attachments/862570143754223626/919863567728140349/Aq.gif","https://media.discordapp.net/attachments/862570143754223626/919863571062603796/cat-cutehg.gif?width=603&height=603","https://media.discordapp.net/attachments/862570143754223626/919863769440596058/MAOR.gif","https://media.discordapp.net/attachments/862570143754223626/919864252771229726/1Rda.gif","https://media.discordapp.net/attachments/862570143754223626/919864273587544074/dance-dancing.gif","https://media.discordapp.net/attachments/862570143754223626/919864423114481665/cat-cute.gif","https://media.discordapp.net/attachments/862570143754223626/919864439610683443/sleep-cat-two-cat.gif?width=567&height=603","https://media.discordapp.net/attachments/862570143754223626/919864416722362368/suspense-suspicious.gif?width=473&height=603",
"https://media.discordapp.net/attachments/862570143754223626/919884433341968414/schastye-kotiki.gif",
"https://media.discordapp.net/attachments/862570143754223626/919884437976670248/bread-cats.gif",
"https://media.discordapp.net/attachments/862570143754223626/919884531392217118/sleep-cat-two-cat.gif?width=623&height=603",
"https://media.discordapp.net/attachments/862570143754223626/919884537402650664/gatto-cibo.gif?width=603&height=603" ]


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if '!maw' in message.content:
    random_index = random.randrange(len(maws))
    await message.channel.send(maws[random_index])

  if '!хуй' in message.content or '!баклажан' in message.content:
    await message.channel.send(baklazhan)

  if '!злюся' in message.content or '!злюсь' in message.content:
    random_index = random.randrange(len(ragnaros))
    await message.channel.send(ragnaros[random_index])

  if '!кот' in message.content:
    random_index = random.randrange(len(cats))
    await message.channel.send(cats[random_index])

client.run(os.getenv('TOKEN'))