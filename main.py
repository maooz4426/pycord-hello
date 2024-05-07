import discord
import os
from dotenv import load_dotenv

load_dotenv()  # これにより .env ファイルが読み込まれる

# アクセストークンを設定
TOKEN = os.getenv("TOKEN") 


#インテントを取得
intents = discord.Intents.all()

#botの設定
bot = discord.Bot(command_prefix='!',intents=intents)


#起動するとターミナルに表示
@bot.event
async def on_ready():
    print("ready!")

# pycordがメッセージを受け取ったら実行されるイベントハンドラ
@bot.event
async def on_message(message: discord.Message):
    
    # メッセージが"hello"だった場合、"Hello!"と返信する
    if message.content == 'hello':
        await message.reply("Hello!")

#botの起動
bot.run(TOKEN)