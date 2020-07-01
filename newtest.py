import discord

client = discord.Client()

@client.event
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

client.run("NzI3ODU2MDk0NDQ1MDQzODUz.Xvx7Wg.XNraMY7D2h73RyxGTL4g39YVKT8")


