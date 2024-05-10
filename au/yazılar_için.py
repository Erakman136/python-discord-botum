import discord
from discord.ext import commands
from bot_token import token 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$nasılsın'):
        await message.channel.send("İyiyim")
    elif message.content.startswith("$komut"):
        await message.channel.send("$merhaba $fotoğraf_düzenleyici $chatcpt $bye $hata_aldım $fotoğraftan_yazıya $teşekkür_ederim $hello_world $deyimler")
    elif message.content.startswith('$chatcpt'):
        await message.channel.send("chatcptye chat.openai.com adresinden ulaşabilirsiniz :)")
    elif message.content.startswith('$hata_aldım'):
        await message.channel.send("chatcptde sorun yaşıyorsanız en baştan bu videoyu izleyebilirsiniz :) https://youtu.be/XwF6ij2-KRY?si=lwWKexDrToc74Ekb ")
    elif message.content.startswith('$fotoğraf_düzenleyici'):
        await message.channel.send("ücretsiz fotoğraf düzenleyici: https://www.iloveimg.com")
    elif message.content.startswith('$fotoğraftan_yazıya'):
        await message.channel.send("ücretsiz fotoğrafdan yazıya çevirmek için tıkla: https://youtu.be/HP6vwQHyiPI?si=7Ba-lUOnKCTYZO5F")
    elif message.content.startswith('$teşekkür_ederim'):
        await message.channel.send("ben teşekkür ederim! size yardımcı olabildiysem ne mutlu benden başka birşey istermisiniz?")
    elif message.content.startswith('$hello_world'):
        await message.channel.send(" ")
    elif message.content.startswith('$deyimler'):
        await message.channel.send(" ")
    else:
        await message.channel.send("mesajınız kodlarımız arasında bulunmuyor lütfen chate $komut yazın ve tüm komutları görün! ve eğer boşluk kullandıysanız boşluk yerine alt tire (_) kullanarak deneyebilirsiniz")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')


client.run(token)