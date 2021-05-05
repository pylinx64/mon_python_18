import discord

# здесь хранится ваш бот
client = discord.Client()
TOKEN = 'ODM4ODAzOTQ0NDEwMDU0NjY2.YJAbDA.GjP57hGktbY7PBmuE8HBXeBeztM'

@client.event
async def on_message(message):
    print(message.author, message.content, message.guild)
    
client.run(TOKEN)
