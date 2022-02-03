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
"https://media.discordapp.net/attachments/862570143754223626/919884537402650664/gatto-cibo.gif?width=603&height=603",
"https://media.discordapp.net/attachments/862570143754223626/930773458101612564/cat-sleep.gif",
"https://media.discordapp.net/attachments/862570143754223626/930773458768498718/cat-cats.gif",
"https://media.discordapp.net/attachments/862570143754223626/930773459225681950/sleepy-sleep.gif",
"https://media.discordapp.net/attachments/862570143754223626/930773459716440114/big-hug.gif",
"https://media.discordapp.net/attachments/862570143754223626/930773460664340490/cat-hug.gif",
"https://media.discordapp.net/attachments/862570143754223626/930773461398331402/cat-cats.gif?width=569&height=603",
"https://media.discordapp.net/attachments/862570143754223626/934752882824187904/cute-cat.gif",
"https://c.tenor.com/-L3KmHAaMGcAAAAd/manul-sneak.gif",
"https://c.tenor.com/HSjA9S4R4osAAAAd/manul.gif",
"https://c.tenor.com/mpwUJliEKywAAAAd/elisttm-jotism.gif",
"https://c.tenor.com/sdo7BUeRFtYAAAAd/elisttm-jotism.gif",
"https://c.tenor.com/oy-mdeRTit0AAAAd/snow-manul-cat.gif"]

bite = ["https://media.discordapp.net/attachments/862570143754223626/920195275132403812/cat-neck.gif",
"https://media.discordapp.net/attachments/862570143754223626/920195275644096572/cat-angry.gif",
"https://media.discordapp.net/attachments/862570143754223626/920195276164173885/gato-morder.gif",
"https://media.discordapp.net/attachments/862570143754223626/920196250580688957/bite-cat.gif?width=603&height=603",
"https://media.discordapp.net/attachments/862570143754223626/920196301780549682/discat-that-bites.gif",
"https://media.discordapp.net/attachments/862570143754223626/920196310328545280/weird-crazy.gif?width=603&height=603",
"https://media.discordapp.net/attachments/862570143754223626/920197033405612042/ear-bite.gif",
"https://media.discordapp.net/attachments/862570143754223626/920197099675602974/cat-kitten.gif",
"https://media.discordapp.net/attachments/862570143754223626/920197314335875072/kitty-windup.gif?width=482&height=603",
"https://media.discordapp.net/attachments/862570143754223626/920197403863302175/cat-bite.gif",
"https://media.discordapp.net/attachments/862570143754223626/920197463158169630/nom-tik-tok.gif?width=339&height=603",
"https://media.discordapp.net/attachments/862570143754223626/920197481239822396/cat-bite.gif?width=482&height=603",
"https://media.discordapp.net/attachments/862570143754223626/920197641541914634/cat-love-cat.gif",
"https://media.discordapp.net/attachments/862570143754223626/920197654544273418/cat-finger-bite-cat.gif?width=475&height=603",
"https://media.discordapp.net/attachments/862570143754223626/920197666909069363/rip-bite.gif",
"https://media.discordapp.net/attachments/861938732525682699/926087909705146398/tumblr_c96ef3c484626b199a0136b5eef9c169_0cf63c4d_400.gif"]

ngcats = ["https://tenor.com/view/new-years-eve-happy2021-trash-2020-happy-gif-19680726",
"https://tenor.com/view/holidays-happyholidays-newyears-newyearseve-happynewyear-gif-3615802",
"https://tenor.com/view/happy-new-year-cats-funny-animals-gif-10400642",
"https://tenor.com/view/holiday-cats-gif-13187783",
"https://tenor.com/view/newyear-happy-new-year-cheers-duck-cat-gif-4894378",
"https://tenor.com/view/cat-cats-gif-13510791",
"https://tenor.com/view/smudge-cat-smudge-the-cat-fireworks-happy-new-year-new-year-gif-23933807",
"https://tenor.com/view/business-cat-working-cat-boss-angry-gif-15945776",
"https://tenor.com/view/kedi-cat-cat-christmas-happy-new-year2021-today-gif-19789933",
"https://tenor.com/view/cat-cats-funny-light-sabers-light-saber-gif-19792677",
"https://tenor.com/view/koshka-kotik-cat-miau-meow-gif-10601927",
"https://tenor.com/view/dancing-cat-salsa-new-year-gif-13197808",
"https://tenor.com/view/happy-new-years-eve-out-with-the-old-cat-christmas-tree-gif-15937624",
"https://tenor.com/view/fran-healy-travis-huey-cat-happy-new-year-gif-24021052",
"https://tenor.com/view/cat-2017-2016-bye2016-hello2017-gif-7413036",
"https://tenor.com/view/new-year-new-me-funny-smile-funny-cats-funny-animals-gif-13202066",
"https://tenor.com/view/graphene-happy-new-year-happy_new_year-happy-new-year2021-happy_new_year_2021-gif-19771243",
"https://tenor.com/view/me-lon-cat-me-lon-happy-new-year-gif-19778302"]

norm = ["http://memesmix.net/media/created/hmf983.jpg",
"http://memesmix.net/media/created/9oyqqy.jpg",
"http://memesmix.net/media/created/h5v5kl.jpg",
"http://memesmix.net/media/created/sidv0x.jpg",
"https://www.meme-arsenal.com/memes/cf50e4e7a26ff4993db857247bcf724f.jpg",
"http://risovach.ru/upload/2016/05/mem/kot-zavis_114023153_orig_.jpg",
"https://memepedia.ru/wp-content/uploads/2020/09/9ce2d3974b3dd6ca57cf9491b23c9949.jpg"]

foxs = ["https://tenor.com/view/fox-cute-adorable-gif-15311172",
"https://tenor.com/view/fox-gif-23017609",
"https://tenor.com/view/fox-bite-attack-snow-gif-14065812",
"https://tenor.com/view/cute-jump-fox-artic-fox-gif-10954757",
"https://tenor.com/view/fox-babies-foxes-biting-yummy-gif-11278762",
"https://tenor.com/view/fox-insane-crazy-losing-it-animal-gif-17548624",
"https://tenor.com/view/fox-cute-sleepy-gif-11781776",
"https://tenor.com/view/pet-a-fox-cute-fox-fox-gif-22514095",
"https://tenor.com/view/brown-fox-dog-lazy-gif-10445506",
"https://tenor.com/view/hmmm-fox-gif-20955251",
"https://tenor.com/view/funny-animals-fox-bounce-gif-12253057",
"https://tenor.com/view/fox-cute-pet-happy-smile-gif-16846934",
"https://tenor.com/view/fox-funny-animals-cute-hair-brush-grooming-gif-8952998",
"https://tenor.com/view/funny-animals-fox-eating-gluttony-when-they-say-they-are-gluten-free-you-im-gluten-free-me-gif-10234708",
"https://tenor.com/view/jerk-what-does-the-fox-say-tongue-fox-bleh-gif-4486853",
"https://tenor.com/view/fox-cute-funny-starbucks-wake-gif-9541964",
"https://tenor.com/view/fox-happy-tail-wag-sleepy-listening-gif-4918833",
"https://tenor.com/view/fox-smile-cute-gif-15311132",
"https://tenor.com/view/fox-belly-rubs-cute-foxes-pet-gif-4918788",
"https://tenor.com/view/fox-cute-adorable-gif-15311166",
"https://tenor.com/view/fox-lots-of-foxes-fluffy-horde-gif-18777084",
"https://c.tenor.com/tjNWAMnU11kAAAAi/fox.gif"]

ravens = ["https://tenor.com/view/crow-raven-kar-vorona-gif-11111592",
"https://tenor.com/view/food-gif-22015888",
"https://tenor.com/view/crow-bow-gif-18499721",
"https://tenor.com/view/the-crow-brandon-lee-crow-raven-tombstone-gif-12575684",
"https://tenor.com/view/pet-raven-crow-bird-cuddle-gif-15379661",
"https://tenor.com/view/ookbob-crow-spinning-crow-ceiling-fan-funny-bird-gif-20851786",
"https://tenor.com/view/yyy-crow-why-gif-15278387",
"https://tenor.com/view/raven-gif-20069584",
"https://tenor.com/view/funny-animals-frey-crow-dogs-crows-gif-14368269",
"https://tenor.com/view/pet-crow-egg-good-bird-bird-gif-13777072",
"https://tenor.com/view/dark-souls-thepruld-crow-solaire-sunlight-lautrec-oscar-knight-dance-gif-18427086",
"https://tenor.com/view/crow-bird-gif-8893792",
"https://tenor.com/view/dog-startled-scared-crow-jump-gif-3967021",
"https://tenor.com/view/dark-souls-dance-sif-gif-14567450",
"https://tenor.com/view/dark-souls-thepruld-solaire-of-astora-sunlight-warrior-sif-grey-wolf-dance-gif-18427159",
"https://tenor.com/view/darksouls-demon-souls-gif-19056864",
"https://c.tenor.com/NczONFOynDwAAAAC/cuddle-raven.gif",
"https://c.tenor.com/3XaW0-r2UR8AAAAC/follow-join.gif",
"https://c.tenor.com/gvGn0JMdbZwAAAAC/workout-goth.gif",
"https://c.tenor.com/oT78bEvJZGoAAAAd/vsm.gif",
"https://c.tenor.com/7WKc50AMcoMAAAAC/wolf-crow.gif"]


nehody = "https://media.discordapp.net/attachments/861938732525682699/925373506047320074/unknown.png";

help = "!maw !баклажан !злюсь !кот !кусь !сойдет !неходи !лис";

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

  if '!кусь' in message.content:
    random_index = random.randrange(len(bite))
    await message.channel.send(bite[random_index])

  if '!нгкот' in message.content:
    random_index = random.randrange(len(ngcats))
    await message.channel.send(ngcats[random_index])

  if '!сойдет' in message.content:
    random_index = random.randrange(len(norm))
    await message.channel.send(norm[random_index])

  if '!неходи' in message.content or '!уходи' in message.content:
    await message.channel.send(nehody)
  
  if '!helphelp' in message.content in message.content:
    await message.channel.send(help)

  if '!лис' in message.content:
    random_index = random.randrange(len(foxs))
    await message.channel.send(foxs[random_index])

  if '!кар' in message.content:
    random_index = random.randrange(len(ravens))
    await message.channel.send(ravens[random_index])

client.run(os.getenv('TOKEN'))