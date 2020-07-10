import discord
import asyncio
import random
import bs4
import os
from discord.ext import commands


client = discord.Client()
embed=discord.Embed(title="   ", description="   ", color=0x00aaaa)
count = [1, 2]




@client.event

    
    if message.content.startswith("!선원"):
        await message.channel.send("```렙업당 각 레벨별 최대 수치 - 순수한 선원 \n"
                                   "2 - 1.4\n"
                                   "3 - 1.6\n"
                                   "4 - 1.9\n"
                                   "5 - 2.2\n"
                                   "6 - 2.5\n"
                                   "7 - 2.9\n"
                                   "8 - 3.3\n"
                                   "9 - 3.7\n"
                                   "10 - 4.2"
                                   "```")
    if message.content.startswith("!우둔"):
        await message.channel.send("```유우둔\n"
                                   "1단계 - 88개\n"
                                   "2단계 - 148개\n"
                                   "3단계 - 236개\n"
                                   "4단계 - 414개\n"
                                   "```")
        await message.channel.send("```동우둔\n"
                                   "1단계 - 176개\n"
                                   "2단계 - 264개\n"
                                   "3단계 - 352개\n"
                                   "4단계 - 352개\n"
                                   "5단계 - 817개\n"
                                   "6단계 - 817개\n"
                                   "7단계 - 1258개\n"
                                   "8단계 - 1368개\n"
                                   "9단계 - 1408개\n"
                                   "10단계 - 1448개"
                                   "```")
    if message.content.startswith("!방어구"):
        await message.channel.send("```동보스방어구(우둔제외)\n"
                                       "1단계 - 76개\n"
                                       "2단계 - 128개\n"
                                       "3단계 - 204개\n"
                                       "4단계 - 358개\n"
                                       "```")
        await message.channel.send("```동보스방어구(우둔제외)\n"
                                       "1단계 - 153개\n"
                                       "2단계 - 230개\n"
                                       "3단계 - 307개\n"
                                       "4단계 - 307개\n"
                                       "5단계 - 713개\n"
                                       "6단계 - 714개\n"
                                       "7단계 - 1098개\n"
                                       "8단계 - 1194개\n"
                                       "9단계 - 1234개\n"
                                       "10단계 - 1274개"
                                       "```")
    if message.content.startswith("!녹뚝"):
        await message.channel.send("```동녹뚝\n"
                                    "1단계 - 28개\n"
                                    "2단계 - 43개\n"
                                    "3단계 - 57개\n"
                                    "4단계 - 57개\n"
                                    "5단계 - 134개\n"
                                     "6단계 - 134개\n"
                                     "7단계 - 206개\n"
                                     "8단계 - 224개\n"
                                     "9단계 - 264개\n"
                                   "10단계 - 305개\n"
                                   "11단계 - 336개\n"
                                   "12단계 - 376개\n"
                                   "13단계 - 416개\n"
                                   "14단계 - 456개\n"
                                   "15단계 - 496개\n"
                                   "16단계 - 536개\n"   
                                      "```")
    if message.content.startswith("!크자카"):
        await message.channel.send("```유크자카, 오핀\n"
                                       "1단계 - 124개\n"
                                       "2단계 - 208개\n"
                                       "3단계 - 332개\n"
                                       "4단계 - 582개\n"
                                       "```")
        await message.channel.send("```동크자카, 오핀\n"
                                       "1단계 - 297개\n"
                                       "2단계 - 389개\n"
                                       "3단계 - 481개\n"
                                       "4단계 - 573개\n"
                                       "5단계 - 905개\n"
                                       "6단계 - 1020개\n"
                                       "7단계 - 1135개\n"
                                       "8단계 - 1250개\n"
                                       "9단계 - 1365개\n"
                                       "10단계 - 1480개"
                                        "```")

    if message.content.startswith("!보조무기"):
       await message.channel.send("```유누베르, 쿠툼\n"
                                       "1단계 - 124개\n"
                                       "2단계 - 208개\n"
                                       "3단계 - 332개\n"
                                       "4단계 - 582개\n"
                                       "```")
       await message.channel.send("```동누베르, 쿠툼\n"
                                       "1단계 - 297개\n"
                                       "2단계 - 389개\n"
                                       "3단계 - 481개\n"
                                       "4단계 - 573개\n"
                                       "5단계 - 905개\n"
                                       "6단계 - 1020개\n"
                                       "7단계 - 1135개\n"
                                       "8단계 - 1250개\n"
                                       "9단계 - 1365개\n"
                                       "10단계 - 1480개"
                                     "```")

    if message.content.startswith("!단델"):
       await message.channel.send("```유단델\n"
                                       "1단계 - 144개\n"
                                       "2단계 - 240개\n"
                                       "3단계 - 384개\n"
                                       "4단계 - 672개\n"
                                       "```")
       await message.channel.send("```동단델\n"
                                       "1단계 - 345개\n"
                                       "2단계 - 451개\n"
                                       "3단계 - 556개\n"
                                       "4단계 - 662개\n"
                                       "5단계 - 1044개\n"
                                       "6단계 - 1176개\n"
                                       "7단계 - 1308개\n"
                                       "8단계 - 1440개\n"
                                       "9단계 - 1573개\n"
                                       "10단계 - 1705개"
                                     "```")
    if message.content.startswith("!도움말") or message.content.startswith("!명령어"):
        await message.channel.send("```!(느낌표)를 앞에 입력후\n"
                                   "선원\n"
                                   "우둔\n"
                                   "방어구\n"
                                   "크자카\n"
                                   "단델\n"
                                   "보조무기\n"
                                   "녹뚝\n"
                                   "보너스구간\n"
                                   "공효율\n"
                                   "추적 [이름]\n"
                                   "입력하세요(ex: !선원, !추적 [가문명])\n"
                                   "소라고둥님, 마법의소라고둥님 을 붙이면 소라고둥님이 나와요```")

    if message.content.startswith("!보너스구간"):
        embed.set_image(url="https://media.discordapp.net/attachments/727925313497071698/728129207787454514/a0379cb56dd4458c.jpg?width=492&height=579")
        await message.channel.send(embed=embed)

    if message.content.startswith("!공효율"):
        embed.set_image(url="https://media.discordapp.net/attachments/727925313497071698/728136520963457044/5a1d66e3af037f92.png")
        await message.channel.send(embed=embed)

    if message.content.startswith("소라고둥님") or message.content.startswith(tuple("마법의 소라고둥님".split())):
        if random.choice(count) == 1:
            embed.set_image(url="https://cdn.discordapp.com/attachments/727925313497071698/728147135593316372/yes.gif")
            await message.channel.send(embed=embed)
        else:
            embed.set_image(url="https://cdn.discordapp.com/attachments/727925313497071698/728147124621017158/no.jpg")
            await message.channel.send(embed=embed)
            
    if message.content.startswith("소라고동님") or message.content.startswith(tuple("마법의 소라고동님".split())):
        if random.choice(count) == 1:
            embed.set_image(url="https://cdn.discordapp.com/attachments/727925313497071698/728147135593316372/yes.gif")
            await message.channel.send(embed=embed)
        else:
            embed.set_image(url="https://cdn.discordapp.com/attachments/727925313497071698/728147124621017158/no.jpg")
            await message.channel.send(embed=embed)
            
            
    if message.content.startswith("!엘렌데"):
        await message.channel.send(":heart::heart::heart::heart: :heart: :heart::heart::heart::heart:\n"
      ":heart:엘렌데야넌아이돌이야:heart:\n"
      ":heart:렌                　               이:heart:\n"
      ":heart:데              엘                 돌:heart:\n"
      ":heart:넌              렌                 이:heart:\n"
      ":heart:아              데                 아:heart:\n"
      ":heart:이              귓                 넌:heart:\n"
      ":heart:돌             :heart_eyes:   　         데:heart:\n"
      ":heart:이                      　         렌:heart:\n"
      ":heart:야이돌이야넌야데렌엘:heart:\n"
      ":heart::heart::heart::heart: :heart: :heart::heart::heart::heart:")
        
        
    if message.content.startswith("!추적"):
        Nickname = message.content.split(' ')[1]
        await message.channel.send('site:https://www.kr.playblackdesert.com/adventure/guild '+ Nickname)
        await message.channel.send("위에 내용을 그대로 구글에 붙여넣어 검색하세요")

        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)


