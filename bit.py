import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("솔마따까리짓")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("누구세요")


client.run("NzY3OTYzODkxOTkyMzYzMDA5.X45kGw.ynD3U2-HwrE0aI3uQgdWPUQZnTk")
