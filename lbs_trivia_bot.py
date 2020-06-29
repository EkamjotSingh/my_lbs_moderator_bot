import discord
from discord.ext import commands
import asyncio
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
            await ctx.send(f"**{member.display_name}** has been kicked by **{ctx.author}**!(reason=**No reason given!**)")
        else:
            await ctx.send(f"**{member.display_name}** has been kicked by **{ctx.author}**!(reason=**{reason}**)")



@client.command()
@has_permissions(ban_members=True)
async def ban(ctx , member : discord.Member ,*, reason=None):
    await member.ban(reason=reason)
    if reason==None:
        await ctx.send(f"**{member.display_name}** has been banned by **{ctx.author}**! (reason=**No reason given!**)")
    else:
        await ctx.send(f"**{member.display_name}** was banned by **{ctx.author}**! (reason=**{reason}**)")

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
    embed.add_field(name="**-users**" , value="To know about the number of members in the server", inline=False)
    embed.add_field(name="**-botstatus**", value="To check the bot status", inline=False)
    embed.add_field(name="**-setnick [member] [nickname]**",value="To change the nickname of a person!(**Can be only used by the person who has ``Manage Nicknames`` permission!**)", inline=False)
    embed.add_field(name="**-kick [member]**", value="To kick a person out of the server!(**Can be only used by the person who has ``Kick Members`` permission!**)", inline=False)
    embed.add_field(name="**-ban [member]**", value="To ban a person!(**Can be only used by the person who has ``Ban Members`` permission!**)" , inline=False)
    embed.add_field(name="**-unban [member#1234]**", value="To unban a person!(**Can be only used by the person who has ``Ban Members`` permission!**)" , inline=False)
    embed.add_field(name="**-role [member] [role]**", value="To give a role to a person!(**Can be only used by the person who has ``Manage Roles`` permission!**)" , inline=False)
    embed.add_field(name="**-removerole [member] [role]**",value="To remove a role from a person!(**Can be only used by the person who has ``Manage Roles`` permission!**)",inline=False)
    embed.add_field(name="**-purge [number of messages]**",value="To delete a number of messages!(**Can be only used by the person who has ``Manage Messages`` permission!**)",inline=False)
    embed.add_field(name="**-warn [member] [reason]**",value="To warn a person!(**Can be only used by the person who has ``Ban Members`` permission!**)",inline=False)
    embed.add_field(name="**-report [issue]**", value="To report a issue!", inline=False)
    embed.add_field(name="**-suggest [suggestion]**", value="To suggest something!", inline=False)
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
@has_permissions(ban_members=True , kick_members=True)
async def warn(ctx , member: discord.Member ,*, reason):
    user = client.get_user(member.id)
    server = ctx.guild.name
    await user.send(f"You were warned in **{server}** server for: **{reason}**")
    await ctx.send(f"**{member}** was warned! (reason=**{reason}**!)")



@client.command()
async def report(ctx ,*, message):
    myself = client.get_user(457044079994470402)
    await myself.send(f"Complaint :- {message}")
    await ctx.send("Your complaint has been registered successfully! We will fix this as soon as possible!")

@report.error
async def report_error(ctx , error):
    if isinstance(error , commands.MissingRequiredArgument):
        await ctx.send(f"**{ctx.author.mention}** please write the complaint too!")

@client.command()
async def suggest(ctx ,*, message):
    myself = client.get_user(457044079994470402)
    await myself.send(f"Suggestion :- {message}")
    await ctx.send("Thank you for your suggestion! I have escalated your suggestion to the developer!:smile: If he finds your suggestion useful he will surely implement it! :wink:")

@suggest.error
async def suggest_error(ctx , error):
    if isinstance(error , commands.MissingRequiredArgument):
        await ctx.send(f"**{ctx.author.mention}** please write the suggestion too!")

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
@has_permissions(manage_nicknames=True)
async def setnick(ctx , member: discord.Member ,*, nick):
    await member.edit(nick=nick)
    await ctx.send("Nickname Changed!")

@setnick.error
async def setnick_error(ctx , error):
    if isinstance(error , commands.MissingPermissions):
        await ctx.send(f"**{ctx.author.mention}** you need ``Manage Nicknames`` permission!")

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

@client.command()
@has_permissions(manage_roles=True)
async def role(ctx , member: discord.Member ,*, role: discord.Role):
    await member.add_roles(role)
    embed = discord.Embed(
        title="LBS Trivia" ,
        description=f":white_check_mark: **Changed roles for {member}** , ``+{role}`` (role to **{member}** was given by **{ctx.author})**" ,
        color = discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png",
        text="Made by Ekamjot#9133")
    await ctx.send(embed=embed)

@role.error
async def role_error(ctx , error):
    if isinstance(error , commands.MissingPermissions):
        await ctx.send(f"**{ctx.author.mention}** you need ``Manage Roles`` permission for this command!")



@client.command()
@has_permissions(manage_roles=True)
async def removerole(ctx , member: discord.Member ,*, role: discord.Role):
    await member.remove_roles(role)
    embed = discord.Embed(
        title="LBS Trivia",
        description=f":white_check_mark: **Removed roles for {member}** , ``-{role}`` (``{role}`` role of the user **{member}** was removed by **{ctx.author})**",
        color=discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/724994399452528730/PVcZAHL6AjRzF3CEhAGD1McKptRcS_3oT0HVW5-lTkeXAniryHiF09Oh_09QXx3nFRON.png",
        text="Made by Ekamjot#9133")
    await ctx.send(embed=embed)

@removerole.error
async def removerole_error(ctx , error):
    if isinstance(error , commands.MissingPermissions):
        await ctx.send(f"**{ctx.author.mention}** you need ``Manage Roles`` permission for this command!")

@client.command()
@has_permissions(manage_messages=True)
async def purge(ctx):
    llmit = ctx.message.content[6:]
    await ctx.channel.purge(limit=int(llmit) + 1)


@purge.error
async def purge_error(ctx , error):
    if isinstance(error , commands.MissingPermissions):
        await ctx.send(f"**{ctx.author.mention}** you need ``Manage Messages`` permission for this command!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! ({client.latency}ms)")

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
