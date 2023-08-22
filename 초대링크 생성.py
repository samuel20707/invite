import discord
import asyncio
import datetime
from datetime import datetime

intents = discord.Intents.all()
client = discord.Client(intents=intents)


Botname = '봇이름'
token = '봇토큰'

@ client.event
async def on_ready():
    print(f'{Botname}이 켜졌습니다.')
    print('-----------------------------------------------------------------------')
    print(f"[!] 참가 중인 서버 : {len(client.guilds)}개의 서버에 참여 중")
    print(f"[!] 서버 인원 총합 : {len(client.users)}와 함께하는 중")
    print('-----------------------------------------------------------------------')
    guild_list = client.guilds
    for i in guild_list:
        print("서버 ID: {} / 서버 이름: {} / 멤버 수: {}".format(i.id, i.name, i.member_count))
    print('-----------------------------------------------------------------------')
    now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    print(f'TIME: [ {now} ] / BOT IS ONLINE')
    while True:
        await asyncio.sleep(600)
        now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        print(f'TIME: [ {now} ] / BOT IS ONLINE')

@ client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '!초대링크':
        invite_link = await message.channel.create_invite()
        await message.reply("이 서버의 초대링크는"+invite_link+"입니다!")


client.run(token)