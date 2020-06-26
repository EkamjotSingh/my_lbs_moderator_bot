import discord

client = discord.Client(command_prefix = '-')

from discord.ext.commands import bot

@client.event
async def on_ready():
    print("I have logged in as {0.user}" .format(client))
    return await client.change_presence(activity=discord.Activity(type=1 , name="-help"))

@client.event
async def on_message(message):
    id = client.get_guild(724157353632727087)

    if message.content.find("-info") != -1:
        embed = discord.Embed(
            title = "**Information about me**" ,
            description='''I was developed by Ekamjot!
I moderate this server!
I am a bot!
I can help you in every way possible!''' ,
            colour = discord.Colour.blue()
            )
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png")
        embed.set_footer(icon_url= "https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png" , text= "Made by Ekamjot#9133")
        await message.channel.send(embed=embed)
    elif message.content.find("-members") != -1:
        embed = discord.Embed(
            title = "**Total number of members in this server:-**" ,
            description= f"{id.member_count}" ,
            color = discord.Color.blue()
        )
        embed.set_footer(icon_url= "https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png" , text= "Made by Ekamjot#9133")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png")
        await message.channel.send(embed=embed)

    elif message.content.startswith("-help"):
        embed = discord.Embed(
        title = "**Help Commands!**" ,
        description = "These are the commands that you can use:" ,
        colour = discord.Colour.blue()
        )

        embed.add_field(name="**-info**" , value="To know about the bot" , inline=False)
        embed.add_field(name="**-botstatus**" , value="To check the bot status" , inline=False)
        embed.add_field(name="-members** (currently being fixed)**", value="To know about the number of members in the server", inline=False)
        embed.add_field(name="**-invite**" , value = "To invite me to your server" , inline=False)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png")
        embed.set_footer(icon_url= "https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png", text = "Made by Ekamjot#9133")
        await message.channel.send(embed=embed)
    elif message.content.find("What is the prefix") != -1:
        await message.channel.send("The prefix for this bot is -")


    elif message.content.find("bye bye" or "Bye Bye") != -1:
        await message.channel.send("Bye!")

    elif message.content.find("-ready") != -1:
        await message.channel.send("> **LBS Trivia Bot is connected successfully!** :white_check_mark:")

    elif message.content.find("-botstatus") != -1:
        embed = discord.Embed(
            title = "**Bot Status**" ,
            description= '''Take it easy! 
**Eveything seems good for now!** ''' ,
            color = discord.Color.blue()
        )
        embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png" , text = "Made by Ekamjot#9133")
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png")
        await message.channel.send(embed = embed)

    elif message.content.find("-invite") != -1:
        embed = discord.Embed(
            title="**LBS Trivia**",
            color=discord.Color.blue()
        )
        embed.add_field(name = "**Invite Link**:" , value = "[Click Here](https://discord.com/api/oauth2/authorize?client_id=724158223401091153&permissions=8&scope=bot)" , inline = False)
        embed.set_footer(
            icon_url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png",
            text="Made by Ekamjot#9133")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png")
        await message.channel.send(embed=embed)
        
@client.event
async def on_member_join(member):
    embed = discord.Embed(
        title = "Welcome!",
        description= f"**{member.name}** just joined! It is nice to have you here! :slight_smile: Please abide by the rules here and ENJOY! :wink:" ,
        color = discord.Color.blue()
)
    embed.set_thumbnail(url = f"{member.avatar_url}")
    embed.set_author(icon_url= "https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png" , name = "LBS Trivia")
    embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png" , text="Made by Ekamjot#9133")
    channel = client.get_channel(id = 725731686733709393)

    await channel.send(embed=embed)
    

client.run('NzI0MTU4MjIzNDAxMDkxMTUz.XvDeTw.09x0ea906dwMdXJfc9t25bnZqxk')
