import discord
from discord.ext import commands, tasks
import asyncio
from discord.ext.commands import has_permissions
from discord import member
from discord.ext.commands import Bot
import random
from discord import Message
from itertools import cycle


client = commands.Bot(command_prefix="+")

@client.remove_command("help")


@client.command()
@has_permissions(kick_members=True)
async def kick(ctx , member : discord.Member , * , reason=None):
    kicked = client.get_user(member.id)
    server_name = ctx.guild.name
    await member.kick(reason=reason)
    if reason==None:
            await kicked.send(f"You were kicked from **{server_name}** for:**(no reason given)**")
            embed = discord.Embed(title="ModCamp" , description=f"**{member.display_name}** has been kicked by **{ctx.author}**!(reason=**No reason given!**)"  , color = discord.Color.blue())
            embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png" , text="Made by Ekamjot#9133")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/724157354106421288/727859761739071518/tenor-3.gif")
            await ctx.send(embed=embed)
    else:
            await kicked.send(f"You were kicked from **{server_name}** for:**{reason}**")
            embed = discord.Embed(title="ModCamp",description=f"**{member.display_name}** has been kicked by **{ctx.author}**!(reason=**{reason}**)",color=discord.Color.blue())
            embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",text="Made by Ekamjot#9133")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/724157354106421288/727859761739071518/tenor-3.gif")
            await ctx.send(embed=embed)




@client.command()
@has_permissions(ban_members=True)
async def ban(ctx , member : discord.Member ,*, reason=None):
    banned = client.get_user(member.id)
    the_server = ctx.guild.name
    await member.ban(reason=reason)
    if reason==None:
        await banned.send(f"You were banned from **{the_server}** for:**(no reason given)**")
        embed = discord.Embed(title="ModCamp",description=f"**{member.display_name}** has been banned by **{ctx.author}**! (reason=**No reason given!**",color=discord.Color.blue())
        embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",text="Made by Ekamjot#9133")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/724157354106421288/727861108932608010/tenor-4.gif")
        await ctx.send(embed=embed)
    else:
        await banned.send(f"You were banned from **{the_server}** for:**{reason}**")
        embed = discord.Embed(title="ModCamp",description=f"**{member.display_name}** was banned by **{ctx.author}**! (reason=**{reason}**)",color=discord.Color.blue())
        embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",text="Made by Ekamjot#9133")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/724157354106421288/727861108932608010/tenor-4.gif")
        await ctx.send(embed=embed)


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



status=cycle(["+help" , "in 7 servers!"])

@client.event
async def on_ready():
    change_status.start()
    print("I have logged in as {0.user}".format(client))


@tasks.loop(seconds=10.0)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=1 , name=next(status)))

@client.command()
async def info(ctx):
    embed = discord.Embed(
            title="**Information about me**",
            description='''      ---ModCamp---
Feeling it difficult to configure moderation bots? :thinking: 
**No worries I am here to help you!**:slight_smile:

In me there are a number of commands to keep your server free from spammers!

You can give role to any person , you can even kick or ban a user with my help!
My prefix is **+**

I'll help you in moderating your server!

To assign roles always keep the bot role on top of the role you want to assign!!

To know my commands and for more information type ``+help`` 

To invite me to your server type ``+invite``

If you face any problem you can DM Ekamjot#9133
Thanks :slight_smile:''',
            colour=discord.Colour.blue()
        )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png")
    embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png", text="Made by Ekamjot#9133")
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    help_user = client.get_user(ctx.author.id)
    embed = discord.Embed(
        title="**Help Commands!**",
        description="These are the commands that you can use:",
        colour=discord.Colour.blue()
    )

    embed.add_field(name="**+info**", value="To know about the bot", inline=False)
    embed.add_field(name="**+tservers**",value="To know the number of servers that I am in",inline=False)
    embed.add_field(name="**+avatar [member]**", value="To check avatar of other members", inline=False)
    embed.add_field(name="**+users**" , value="To know about the number of members in the server", inline=False)
    embed.add_field(name="**+botstatus**", value="To check the bot status", inline=False)
    embed.add_field(name="**+kick [member]**", value="To kick a person out of the server!(**Can be only used by the person who has ``Kick Members`` permission!**)", inline=False)
    embed.add_field(name="**+ban [member]**", value="To ban a person!(**Can be only used by the person who has ``Ban Members`` permission!**)" , inline=False)
    embed.add_field(name="**+unban [member#1234]**", value="To unban a person!(**Can be only used by the person who has ``Ban Members`` permission!**)" , inline=False)
    embed.add_field(name="**+role [member] [role]**", value="To give a role to a person!(**Can be only used by the person who has ``Manage Roles`` permission!**)" , inline=False)
    embed.add_field(name="**+removerole [member] [role]**",value="To remove a role from a person!(**Can be only used by the person who has ``Manage Roles`` permission!**)",inline=False)
    embed.add_field(name="**+mute [member]**",value="To mute a person!(**Can be only used by the person who has ``Manage Roles`` permission!**)",inline=False)
    embed.add_field(name="**+unmute [member]**",value="To unmute a person!(**Can be only used by the person who has ``Manage Roles`` permission!**)",inline=False)
    embed.add_field(name="**+purge [number of messages]**",value="To delete a number of messages!(**Can be only used by the person who has ``Manage Messages`` permission!**)",inline=False)
    embed.add_field(name="**+warn [member] [reason]**",value="To warn a person!(**Can be only used by the person who has ``Ban Members`` permission!**)",inline=False)
    embed.add_field(name="**+report [issue]**", value="To report a issue!", inline=False)
    embed.add_field(name="**+suggest [suggestion]**", value="To suggest something!", inline=False)
    embed.add_field(name="**+invite**", value="To invite me to your server", inline=False)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png")
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",
        text="Made by Ekamjot#9133")
    await help_user.send(embed=embed)
    await ctx.send("**Check your DM for a list of help commands!**")

@client.command()
async def ready(ctx):
    await ctx.send("> **ModCamp is connected successfully!** :white_check_mark:")
@client.command()
async def speak(ctx,message):
    answer = random.choice(["lol" , "loli" , "yes" , "no" , "nope" , "ok" , "umm","maybe","IDK","I dont know" , "me neither","nevermind" ,"Are you sure about that?" , "Are you sorry for that" , "Damn" ,"oh","bruh","sayonara","hello","hi"])
    await ctx.send(answer)

@client.command()
async def userinfo(ctx , member: discord.Member):
    infouser = client.get_user(member.id)
    embed = discord.Embed(
        title =f"**{member}**" ,
        color = discord.Color.blue()
    )
    embed.add_field(name="**Joined at:**" , value =member.joined_at.strftime("%a , %#d %B %Y , %I:%M %p UTC") , inline=False)
    embed.add_field(name="**Account Created on:**" , value=member.created_at.strftime("%a , %#d %B %Y , %I:%M %p UTC") , inline=False)
    values = member.top_role
    embed.add_field(name="**Top Role:**" , value =values.mention , inline=False)
    a = discord.utils.get(member.guild_permissions)
    embed.add_field(name="**Status:**" , value=member.status , inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Member ID: {member.id} Requested by: {ctx.author}")

    await ctx.send(embed=embed)

@userinfo.error
async def userinfo_error(ctx , error):
    if isinstance(error , commands.BadArgument):
        await ctx.send("**No member with that name was found!**")

@client.command()
@has_permissions(ban_members=True)
async def warn(ctx , member: discord.Member ,*, reason):
    user = client.get_user(member.id)
    server = ctx.guild.name
    embed = discord.Embed(
        title="**ModCamp**",
        description=f"**{member}** was warned! (reason=**{reason}**!)",
        colour=discord.Colour.blue()
    )
    embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png" , text="Made by Ekamjot#9133")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png")
    await user.send(f"You were warned in **{server}** server for: **{reason}**")
    await ctx.send(embed=embed)

@warn.error
async def warn_error(ctx , error):
    if isinstance(error , commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention} you need ``Ban Members`` permission to use this command!")

   
@client.command()
async def report(ctx ,*, message):
    myself = client.get_user(457044079994470402)
    await myself.send(f"Complaint :- {message} by {ctx.author} in {ctx.guild.name}")
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
async def tservers(ctx):
    embed = discord.Embed(
        title="**ModCamp**" ,
        description=f"I am currently in total **{len(client.guilds)}** servers!" ,
        color = discord.Color.blue()
    )
    await ctx.send(embed=embed)

@client.command()
async def invite(ctx):
    embed = discord.Embed(
        title="**ModCamp**",
        color=discord.Color.blue()
        )
    embed.add_field(name="**Invite Link**:",
                        value="[Click Here](https://discord.com/api/oauth2/authorize?client_id=724158223401091153&permissions=8&scope=bot)",
                        inline=False)
    embed.set_footer(
            icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",
            text="Made by Ekamjot#9133")
    embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png")
    await ctx.send(embed=embed)



@client.command()
async def botstatus(ctx):
    embed = discord.Embed(
        title="**Bot Status**",
        description='''Take it easy!
**Everything seems good for now!** ''',
        color=discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",
        text="Made by Ekamjot#9133")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png")
    await ctx.send(embed=embed)

@client.command()
async def users(ctx):
    embed = discord.Embed(
            title="**Total number of members in this server:-**",
            description=f"{ctx.guild.member_count}",
            color=discord.Color.blue()
        )
    embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",
            text="Made by Ekamjot#9133")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png")
    await ctx.send(embed=embed)

@users.error
async def users_error(ctx , error):
    if isinstance(error , commands.CommandInvokeError):
        await ctx.send(f"**{ctx.author.mention}** you can use this command only in a server!")


@client.command()
async def avatar(ctx ,*, member: discord.Member):
    embed = discord.Embed(
        title = "ModCamp" ,
        description= f" Showing {member.mention}'s avatar!" ,
        color = discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",
        text="Made by Ekamjot#9133")


    embed.set_image(url=f"{member.avatar_url}")
    await ctx.send(embed=embed)

@client.command()
@has_permissions(administrator=True)
async def give(ctx,member:discord.Member , karma: int):
    await ctx.send(f"Gave {karma} karma to {member}. They now have {karma} karma!")

@avatar.error
async def avatar_error(ctx , error):
    if isinstance(error , commands.MissingRequiredArgument):
        await ctx.send(f"**{ctx.author.mention}** please mention a member too!")


@client.command()
@has_permissions(manage_roles=True)
async def role(ctx , member: discord.Member ,*, role: discord.Role):
    await member.add_roles(role)
    embed = discord.Embed(
        title="ModCamp" ,
        description=f":white_check_mark: **Changed roles for {member}** , ``+{role}`` (role to **{member}** was given by **{ctx.author})**" ,
        color = discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",
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
        title="ModCamp",
        description=f":white_check_mark: **Removed roles for {member}** , ``-{role}`` (``{role}`` role of the user **{member}** was removed by **{ctx.author})**",
        color=discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",
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
    await ctx.send(f"Pong! ({round(client.latency*1000)}ms)")


@client.command()
@has_permissions(manage_roles=True)
async def mute(ctx,*, member: discord.Member, mute_time: int):
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(mute_role)
    embed = discord.Embed(
        title="ModCamp" ,
        description=f":white_check_mark: **{member}** was muted by **{ctx.message.author}**!" ,
        color = discord.Color.blue()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png")
    embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",text="Made by Ekamjot#9133")
    await ctx.send(embed=embed)

@mute.error
async def mute_error(ctx , error):
    if isinstance(error , commands.CommandInvokeError):
        await ctx.send("**Please make a role named as ``Muted`` first!**")

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention} you need ``Manage Roles`` permission for this command!")

@client.command()
@has_permissions(manage_roles=True)
async def unmute(ctx, *, member: discord.Member):
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted" or "muted")
    await member.remove_roles(mute_role)
    embed = discord.Embed(
        title="ModCamp",
        description=f":white_check_mark: **{member}** was unmuted by **{ctx.message.author}**!",
        color=discord.Color.blue()
    )

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png")
    embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png", text = "Made by Ekamjot#9133")
    await ctx.send(embed=embed)

@unmute.error
async def unmute_error(ctx , error):
    if isinstance(error , commands.MissingRequiredArgument):
        await ctx.send("**Please mention a member to unmute!**")

    elif isinstance(error , commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention} you need ``Manage Roles`` permission to use this command!")



@client.event
async def on_member_join(member):
    embed = discord.Embed(
        title="Welcome!",
        description=f"**{member.name}** just joined! It is nice to have you here! :slight_smile: Please abide by the rules here and ENJOY! :wink:",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",
        name="LBS Trivia")
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/attachments/724157354106421288/727363623898578964/Z.png",
        text="Made by Ekamjot#9133")
    channel = client.get_channel(id=724157354106421288)
    await channel.send(embed=embed)

@client.command()
async def on_member_join(ctx, member: discord.Member):
    incoming = client.get_user(member.id)
    await incoming.send(f"Hello {member.mention}")















client.run('NzI0MTU4MjIzNDAxMDkxMTUz.XvDeTw.09x0ea906dwMdXJfc9t25bnZqxk')
