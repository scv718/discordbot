import discord
from discord.ext import commands
import asyncio
import random
import datetime
import os

client = discord.Client()
embed = discord.Embed(title="   ", description="   ", color=0x00aaaa)
count = [1, 2]
bot = commands.Bot(command_prefix='!')
channel = 731012289452572685

@client.event
@bot.event

async def on_message(message):
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
        await message.channel.send("```유보스방어구(우둔제외)\n"
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
    if message.content.startswith("!고녹각"):
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/727925313497071698/737638703043838002/unknown.png")
        await message.channel.send("``` 고녹각 19단까지 435개 소모```")
        await message.channel.send(embed=embed)

    if message.content.startswith("!고단델"):
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/727925313497071698/737638703043838002/unknown.png")
        await message.channel.send("``` 고단델 19단까지 1700개 소모```")
        await message.channel.send(embed=embed)
        
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
                                   "공방효율\n"
                                   "추적 [이름]"
                                   "입력하세요(ex: !선원)\n"
                                   "소라고둥님, 마법의소라고둥님 을 붙이면 소라고둥님이 나와요```")
        
      
        
    if message.content.startswith("!보너스구간"):
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/727925313497071698/751785513681289266/18c75b0fb92537ff.png")
        await message.channel.send(embed=embed)

    if message.content.startswith("!공방효율"):
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/727925313497071698/751785513681289266/18c75b0fb92537ff.png")
        await message.channel.send(embed=embed)

    if message.content.startswith("소라고둥님") or message.content.startswith(tuple("마법의 소라고둥님".split())):
        if random.choice(count) == 1:
            embed.set_image(url="https://cdn.discordapp.com/attachments/727925313497071698/728147135593316372/yes.gif")
            await message.channel.send(embed=embed)
        else:
            embed.set_image(url="https://cdn.discordapp.com/attachments/727925313497071698/728147124621017158/no.jpg")
            await message.channel.send(embed=embed)

    if message.content.startswith("!추적"):
        Nickname = message.content.split(' ')[1]
        url = 'https://www.google.co.kr/search?q=site:https://www.kr.playblackdesert.com/adventure/guild%20{}'.format(Nickname)
        await message.channel.send(url)
        await message.channel.send("```위에 링크로 접속.```")

    guild = message.guild
    if guild:
        path = "C:\chatlogs{}.txt".format(guild.id)
        with open(path, 'a+') as f:
            print("{0.author.name} : {0.content}".format(message), file=f)

    if message.author.bot:
        return

    data = f"[{datetime.datetime.today()}] {message.author.name}: {message.content}"
    await client.get_channel(channel).send(data)
        


        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)


