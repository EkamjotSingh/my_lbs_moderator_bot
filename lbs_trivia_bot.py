import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord import member
from discord.ext.commands import Bot
import random
from discord import Message

client = commands.Bot(command_prefix="-")

@client.remove_command("help")


@client.command()
@has_permissions(kick_members=True)
async def kick(ctx , member : discord.Member , * , reason=None):
        await member.kick(reason=reason)
        if reason==None:
            await ctx.send(f"**{member.display_name}** has been kicked (reason=**No reason given!**)")
        else:
            await ctx.send(f"**{member.display_name}** has been kicked (reason=**{reason}**)")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx , member : discord.Member ,*, reason=None):
    await member.ban(reason=reason)
    if reason==None:
        await ctx.send(f"**{member.display_name}** has been banned! (reason=**No reason given!**)")
    else:
        await ctx.send(f"**{member.display_name}** was banned! (reason=**{reason}**)")

@client.command()
@has_permissions(ban_members=True)
async def unban(ctx , * , member):
    banned_users = await ctx.guild.bans()
    member_name , member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name , user.discriminator) == (member_name , member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"**{user.name , user.discriminator}** was unbanned!")



@client.event
async def on_ready():
    print("I have logged in as {0.user}".format(client))
    return await client.change_presence(activity=discord.Activity(type=1, name="-help"))

@client.command()
async def info(ctx):
    embed = discord.Embed(
            title="**Information about me**",
            description='''I was developed by Ekamjot!
I moderate this server!
I am a bot!
I can help you in every way possible!''',
            colour=discord.Colour.blue()
        )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png")
    embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png", text="Made by Ekamjot#9133")
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="**Help Commands!**",
        description="These are the commands that you can use:",
        colour=discord.Colour.blue()
    )

    embed.add_field(name="**-info**", value="To know about the bot", inline=False)
    embed.add_field(name="**-avatar [member]**", value="To check avatar of other members", inline=False)
    embed.add_field(name="**-botstatus**", value="To check the bot status", inline=False)
    embed.add_field(name="**-kick [member]**", value="To kick a person out of the server!(**Can be only used by the person who has ``Kick Members`` permission!**)", inline=False)
    embed.add_field(name="**-ban [member]**", value="To ban a person!(**Can be only used by the person who has ``Ban Members`` permission!**)" , inline=False)
    embed.add_field(name="**-unban [member#1234]**", value="To unban a person!(**Can be only used by the person who has ``Ban Members`` permission!**)" , inline=False)
    embed.add_field(name="**-users**",
                    value="To know about the number of members in the server", inline=False)
    embed.add_field(name="**-invite**", value="To invite me to your server", inline=False)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png")
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png",
        text="Made by Ekamjot#9133")
    await ctx.send(embed=embed)

@client.command()
async def ready(ctx):
    await ctx.send("> **LBS Trivia Bot is connected successfully!** :white_check_mark:")

@client.command()
async def invite(ctx):
    embed = discord.Embed(
        title="**LBS Trivia**",
        color=discord.Color.blue()
        )
    embed.add_field(name="**Invite Link**:",
                        value="[Click Here](https://discord.com/api/oauth2/authorize?client_id=724158223401091153&permissions=8&scope=bot)",
                        inline=False)
    embed.set_footer(
            icon_url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png",
            text="Made by Ekamjot#9133")
    embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png")
    await ctx.send(embed=embed)
    
@client.command()
async def botstatus(ctx):
    embed = discord.Embed(
        title="**Bot Status**",
        description='''Take it easy!
**Eveything seems good for now!** ''',
        color=discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png",
        text="Made by Ekamjot#9133")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png")
    await ctx.send(embed=embed)

@client.command()
async def users(ctx):
    embed = discord.Embed(
            title="**Total number of members in this server:-**",
            description=f"{ctx.guild.member_count}",
            color=discord.Color.blue()
        )
    embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png",
            text="Made by Ekamjot#9133")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png")
    await ctx.send(embed=embed)

@client.command()
async def avatar(ctx , member: discord.Member):
    embed = discord.Embed(
        title = "LBS Trivia" ,
        description= f" Showing {member.mention}'s avatar!" ,
        color = discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png",
        text="Made by Ekamjot#9133")


    embed.set_image(url=f"{member.avatar_url}")
    await ctx.send(embed=embed)

@client.event
async def on_member_join(member):
    embed = discord.Embed(
        title="Welcome!",
        description=f"**{member.name}** just joined! It is nice to have you here! :slight_smile: Please abide by the rules here and ENJOY! :wink:",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png",
        name="LBS Trivia")
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png",
        text="Made by Ekamjot#9133")
    channel = client.get_channel(id=724157354106421288)
    await channel.send(embed=embed)

client.run('NzI0MTU4MjIzNDAxMDkxMTUz.XvDeTw.09x0ea906dwMdXJfc9t25bnZqxk')
