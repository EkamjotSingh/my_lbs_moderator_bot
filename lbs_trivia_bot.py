import discord
from discord.ext import commands, tasks
import asyncio
from discord.ext.commands import has_permissions
from discord import member
from discord.ext.commands import Bot
import random
from discord import Message
from itertools import cycle

client = commands.Bot(command_prefix="-")


@client.remove_command("help")


@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    kicked = client.get_user(member.id)
    server_name = ctx.guild.name
    await member.kick(reason=reason)
    if reason == None:

        embed = discord.Embed(title="ModCamp",
                              description=f"**{member.display_name}** has been kicked by **{ctx.author}**!(reason=**No reason given!**)",
                              color=discord.Color.blue())
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                         text="Made by Ekamjot#9133")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    else:

        embed = discord.Embed(title="ModCamp",
                              description=f"**{member.display_name}** has been kicked by **{ctx.author}**!(reason=**{reason}**)",
                              color=discord.Color.blue())
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                         text="Made by Ekamjot#9133")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
        await ctx.message.delete()
        await ctx.send(embed=embed)




@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    banned = client.get_user(member.id)
    the_server = ctx.guild.name
    await member.ban(reason=reason)
    if reason == None:

        embed = discord.Embed(title="ModCamp",
                              description=f"**{member.display_name}** has been banned by **{ctx.author}**! (reason=**No reason given!**",
                              color=discord.Color.blue())
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                         text="Made by Ekamjot#9133")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
        await ctx.message.delete()
        await ctx.send(embed=embed)
    else:

        embed = discord.Embed(title="ModCamp",
                              description=f"**{member.display_name}** was banned by **{ctx.author}**! (reason=**{reason}**)",
                              color=discord.Color.blue())
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                         text="Made by Ekamjot#9133")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
        await ctx.message.delete()
        await ctx.send(embed=embed)


@client.command()
@has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.message.delete()
            await ctx.send(f"**{user.name, user.discriminator}** was unbanned!")


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            f"**{ctx.author.mention} you do not have permissions required for this command! You need ``Ban Members`` permission for this command!**")

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-unban [member#1234]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)


status = cycle(["-help", "-help"])


@client.event
async def on_ready():
    change_status.start()
    print("I have logged in as {0.user}".format(client))


@tasks.loop(seconds=10.0)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=1, name=next(status)))


@client.command()
async def info(ctx):
    embed = discord.Embed(
        title="**Information about me**",
        description='''      ---ModCamp---
Feeling it difficult to configure moderation bots? :thinking: 
**No worries I am here to help you!**:slight_smile:
In me there are a number of commands to keep your server free from spammers!
You can give role to any person , you can even kick or ban a user with my help!
My prefix is **-**
I'll help you in moderating your server!
To assign roles always keep the bot role on top of the role you want to assign!!
To know my commands and for more information type ``-help`` 
To invite me to your server type ``-invite``
If you face any problem you can DM Ekamjot#9133
Thanks :slight_smile:''',
        colour=discord.Colour.blue()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                     text="Made by Ekamjot#9133")
    await ctx.send(embed=embed)


@client.command()
async def guildinfo(ctx):
    channels = len([x for x in ctx.guild.channels if type(x) == discord.TextChannel])
    role_count = len(ctx.guild.roles)
    online_members = len([y for y in ctx.guild.members if
                          y.status == discord.Status.online or y.status == discord.Status.idle or y.status == discord.Status.dnd])
    embed = discord.Embed(
        title=f"**{ctx.guild.name}**",
        color=discord.Color.blue()
    )
    embed.add_field(name="**Owner:**", value=f"**{ctx.guild.owner}**", inline=False)
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    embed.add_field(name=f"**Server Region:**", value=f"**{ctx.guild.region}**")
    embed.add_field(name="**Total Members:**", value=f"**{ctx.guild.member_count}**", inline=False)
    embed.add_field(name="**Online Members:**", value=f"**{online_members}**", inline=False)
    embed.add_field(name="**Text Channels:**", value=f"**{channels}**", inline=False)
    embed.add_field(name="**Total Roles:**", value=f"**{role_count}**", inline=False)
    embed.add_field(name="**Server Created at:**",
                    value=ctx.guild.created_at.strftime("%a , %#d %B %Y , %I:%M %p **UTC**"), inline=False)
    embed.add_field(name="**Server ID:**", value=f"**{ctx.guild.id}**", inline=False)
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                     text="Made by Ekamjot#9133")
    await ctx.send(embed=embed)

@client.command()
async def report(ctx,*,message: str):
    name = ctx.author
    user_id = ctx.author.id
    server = ctx.guild.name
    server_id = ctx.guild.id
    myself = client.get_user(457044079994470402)
    await ctx.send('**Your report about a bug/error has successfully reached to us and we will surely try to fix it** :slight_smile:')
    await myself.send(f'''
**Report**
By:- {name}
User ID:- {user_id}
Server:- {server}
Server ID:- {server_id}
Message:- {message}
-----------------------------''')
    
    
@report.error
async def report_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-report [error/bug/message]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)



    elif isinstance(error, commands.BadArgument):
        await ctx.send(
            "**Sorry I was not able to get your message to the developer writing words in the starting of the suggestion instead of numbers might help**")


@client.command()
async def suggest(ctx,*,message):
    name = ctx.author
    user_id = ctx.author.id
    server = ctx.guild.name
    server_id = ctx.guild.id
    myself = client.get_user(457044079994470402)
    await ctx.send('**Your suggestion has successfully reached to us. Thanks for your suggestion!** :slight_smile:')
    await myself.send(f'''
**Suggestion**
By:- {name}
User ID:- {user_id}
Server:- {server}
Server ID:- {server_id}
Message:- {message}
---------------------------''')
    

@suggest.error
async def suggest_error(ctx, error):

    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-suggest [suggestion/message]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)



    elif isinstance(error, commands.BadArgument):
        await ctx.send("**Sorry I was not able to get your message to the developer writing words in the starting of the suggestion instead of numbers might help**")






@client.command()
@has_permissions(manage_roles=True)
async def roleall(ctx , role: discord.Role):
    embed = discord.Embed(
        title="**ModCamp**" ,
        description=f"Please wait for the process to complete! It takes almost {ctx.guild.member_count} seconds to assign roles to {ctx.guild.member_count} users!" ,
        color=discord.Color.blue()
    )
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                     text="Made by Ekamjot#9133")
    c = await ctx.send(embed=embed)
    for members in ctx.guild.members:
        await members.add_roles(role)
    embed = discord.Embed(
        title="**ModCamp**",
        description=f":white_check_mark: Done added the role {role.mention} to {ctx.guild.member_count} users!",
        color=discord.Color.blue()
    )
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                     text="Made by Ekamjot#9133")
    await c.edit(embed=embed)

@roleall.error
async def roleall_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"**{ctx.author.mention}** you need ``Manage Roles`` permission for this command!")

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-roleall [role]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send('''**I do not have the permissions to use this command. Please provide me permissions and try again!
**NOTE**:-To assign roles always keep the bot role on top of the role you want to assign!**
**Giving me ``Administrator`` Permission might fix the issue!''')

    elif isinstance(error, commands.BadArgument):
        await ctx.send("**Sorry I was not able to find that user or the role!**")

@client.command()
@has_permissions(manage_roles=True)
async def removeall(ctx , role: discord.Role):
    embed = discord.Embed(
        title="**ModCamp**" ,
        description=f"Please wait for the process to complete! It takes almost {ctx.guild.member_count} seconds to remove roles of {ctx.guild.member_count} users!" ,
        color=discord.Color.blue()
    )
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                     text="Made by Ekamjot#9133")
    c = await ctx.send(embed=embed)
    for members in ctx.guild.members:
        await members.remove_roles(role)
    embed = discord.Embed(
        title="**ModCamp**",
        description=f":white_check_mark: Done removed the role {role.mention} from {ctx.guild.member_count} users!",
        color=discord.Color.blue()
    )
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                     text="Made by Ekamjot#9133")
    await c.edit(embed=embed)

@removeall.error
async def removeall_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"**{ctx.author.mention}** you need ``Manage Roles`` permission for this command!")

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-removeall [role]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send('''**I do not have the permissions to use this command. Please provide me permissions and try again!
**NOTE**:-To assign roles always keep the bot role on top of the role you want to assign!**
**Giving me ``Administrator`` Permission might fix the issue!''')

    elif isinstance(error, commands.BadArgument):
        await ctx.send("**Sorry I was not able to find that user or the role!**")







@client.command()
async def help(ctx):
    requested_id = client.get_user(ctx.author.id)
    embed = discord.Embed(
        title="**Help Commands!**",
        description="These are the commands that you can use:",
        colour=discord.Colour.blue()
    )

    embed.add_field(name="**-info**", value="To know about the bot", inline=False)
    embed.add_field(name="**-say**",
                    value="To announce anything with a @everyone ping!(**Can be only used by the person who has ``Manage Messages`` Permission!**)",
                    inline=False)
    embed.add_field(name="**-avatar [member]**", value="To check avatar of other members", inline=False)
    embed.add_field(name="**-users**", value="To know about the number of members in the server", inline=False)
    embed.add_field(name="**-guildinfo**", value="To know about the server info!", inline=False)
    embed.add_field(name="**-botstatus**", value="To check the bot status", inline=False)
    embed.add_field(name="**-setnick [member] [nickname]**",
                    value="To change the nickname of a person!(**Can be only used by the person who has ``Manage Nicknames`` permission!**)",
                    inline=False)
    embed.add_field(name="**-kick [member]**",
                    value="To kick a person out of the server!(**Can be only used by the person who has ``Kick Members`` permission!**)",
                    inline=False)
    embed.add_field(name="**-ban [member]**",
                    value="To ban a person!(**Can be only used by the person who has ``Ban Members`` permission!**)",
                    inline=False)
    embed.add_field(name="**-unban [member#1234]**",
                    value="To unban a person!(**Can be only used by the person who has ``Ban Members`` permission!**)",
                    inline=False)
    embed.add_field(name="**-role [member] [role]**",
                    value="To give a role to a person!(**Can be only used by the person who has ``Manage Roles`` permission!**)",
                    inline=False)
    embed.add_field(name="**-removerole [member] [role]**",
                    value="To remove a role from a person!(**Can be only used by the person who has ``Manage Roles`` permission!**)",
                    inline=False)
    embed.add_field(name="**-roleall [role]**",
                    value="To give a role to every member of the server! (**Can be only used by the person who has ``Manage Roles`` permission!**)",
                    inline=False)
    embed.add_field(name="**-removeall [role]**",
                    value="To remove a role from every member of the server! (**Can be only used by the person who has ``Manage Roles`` permission!**)",
                    inline=False)
    embed.add_field(name="**-mute [member]**",
                    value="To mute a person!(**Can be only used by the person who has ``Manage Roles`` permission!**)",
                    inline=False)
    embed.add_field(name="**-unmute [member]**",
                    value="To unmute a person!(**Can be only used by the person who has ``Manage Roles`` permission!**)",
                    inline=False)
    embed.add_field(name="**-purge [number of messages]**",
                    value="To delete a number of messages!(**Can be only used by the person who has ``Manage Messages`` permission!**)",
                    inline=False)
    embed.add_field(name="**-warn [member] [reason]**",
                    value="To warn a person!(**Can be only used by the person who has ``Ban Members`` permission!**)",
                    inline=False)
    embed.add_field(name="**-report [error]**" , value="To report an error/bug!" , inline=False)
    embed.add_field(name="**-suggest [suggestion]**" , value="To give a suggestion!" , inline=False)
    embed.add_field(name="**-invite**", value="To invite me to your server", inline=False)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
        text="Made by Ekamjot#9133")

    await ctx.send(embed=embed)


@client.command()
@has_permissions(manage_messages=True)
async def say(ctx, *, announcement):
    await ctx.message.delete()
    await ctx.send(f'''@everyone 
{announcement}''')


@client.command()
@has_permissions(administrator=True)
async def acc(ctx, *, time):
    await ctx.message.delete()
    await ctx.send(f'''
<:LastBrainStanding:716103983764078630> **Last Brain Standing starts in just {time} minutes!** 
:white_check_mark:**Connect in <#731844357745016842>  to get access to <#715986102590373959> text channel!  ** ''')


@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            f"**{ctx.author.mention} you do not have the permission required! You need ``Manage Messages`` permission for this command!**")

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-say [announcement]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send(
            '''**I do not have the permissions to use this command. Please provide me permissions and try again!**
**NOTE:-** Giving me ``Administrator`` permission might fix the issue!''')


@client.command()
async def tmem(ctx):
    await ctx.send(f"With **{len(client.users)}** users")


@client.command()
async def ready(ctx):
    await ctx.message.delete()

    read = await ctx.send("> **ModCamp is connected successfully!** :white_check_mark:")
    await read.add_reaction("✅")


@client.command()
async def speak(ctx, message):
    answer = random.choice(
        ["lol", "loli", "yes", "no", "nope", "ok", "umm", "maybe", "IDK", "I dont know", "me neither", "nevermind",
         "Are you sure about that?", "Are you sorry for that", "Damn", "oh", "bruh", "sayonara", "hello", "hi" , "np"])
    await ctx.send(answer)


@client.command()
async def userinfo(ctx, member: discord.Member):
    infouser = client.get_user(member.id)
    embed = discord.Embed(
        title=f"**{member}**",
        color=discord.Color.blue()
    )
    embed.add_field(name="**Joined at:**", value=member.joined_at.strftime("%a , %#d %B %Y , %I:%M %p UTC"),
                    inline=False)
    embed.add_field(name="**Account Created on:**", value=member.created_at.strftime("%a , %#d %B %Y , %I:%M %p UTC"),
                    inline=False)
    values = member.top_role
    embed.add_field(name="**Top Role:**", value=values.mention, inline=False)
    a = discord.utils.get(member.guild_permissions)
    embed.add_field(name="**Status:**", value=member.status, inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Member ID: {member.id} Requested by: {ctx.author}")

    await ctx.send(embed=embed)


@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("**No member with that name was found!**")

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-userinfo [user]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)


@client.command()
@has_permissions(ban_members=True)
async def warn(ctx, member: discord.Member, *, reason):
    user = client.get_user(member.id)
    server = ctx.guild.name

    embed = discord.Embed(
        title="**ModCamp**",
        description=f"**{member}** was warned! (reason=**{reason}**!)",
        colour=discord.Colour.blue()
    )
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                     text="Made by Ekamjot#9133")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
    await ctx.message.delete()
    await ctx.send(embed=embed)
    await user.send(f"You were warned in {server} for: {reason}")


@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention} you need ``Ban Members`` permission to use this command!")


    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-warn [member][reason]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send(
            '''**I do not have the permissions to use this command. Please provide me permissions and try again!**
**NOTE:-** Giving me ``Administrator`` permission might fix the issue!''')

    elif isinstance(error, commands.BadArgument):
        await ctx.send("**Sorry I was not able to find that user!**")


@client.command()
async def tdiscord(ctx):
    embed = discord.Embed(
        title="**ModCamp**",
        description=f"I am currently in total **{len(client.guilds)}** servers!",
        color=discord.Color.blue()
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
        icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
        text="Made by Ekamjot#9133")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
    await ctx.send(embed=embed)


@client.command()
@has_permissions(manage_nicknames=True)
async def setnick(ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)
    embed = discord.Embed(
        title="**ModCamp**",
        description="**:white_check_mark:Nickname Changed!**",
        color=discord.Color.blue()
    )
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                     text="Made by Ekamjot#9133")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
    await ctx.message.delete()
    await ctx.send(embed=embed)


@setnick.error
async def setnick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"**{ctx.author.mention}** you need ``Manage Nicknames`` permission!")

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description=f"**-setnick [member] [nickname]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    elif isinstance(error, commands.BadArgument):
        await ctx.send("**Sorry I was not able to find that user!**")

    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send('''**I do not have the permissions to do that! Please provide me permissions and try again!**
**NOTE:-** Giving me ``Administrator`` permission might fix the issue!''')


@client.command()
async def botstatus(ctx):
    embed = discord.Embed(
        title="**Bot Status**",
        description='''Take it easy!
**Everything seems good for now!** ''',
        color=discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
        text="Made by Ekamjot#9133")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
    await ctx.send(embed=embed)


@client.command()
async def users(ctx):
    embed = discord.Embed(
        title="**Total number of members in this server:-**",
        description=f"{ctx.guild.member_count}",
        color=discord.Color.blue()
    )
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                     text="Made by Ekamjot#9133")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
    await ctx.send(embed=embed)


@users.error
async def users_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(f"**{ctx.author.mention}** you can use this command only in a server!")


@client.command()
async def avatar(ctx, *, member: discord.Member):
    embed = discord.Embed(
        title="ModCamp",
        description=f" Showing {member.mention}'s avatar!",
        color=discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
        text="Made by Ekamjot#9133")

    embed.set_image(url=f"{member.avatar_url}")
    await ctx.send(embed=embed)


@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-avatar [member]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    elif isinstance(error, commands.BadArgument):
        await ctx.send("**Sorry! I was not able to find that user!**")


@client.command()
async def av(ctx, *, member: discord.Member):
    embed = discord.Embed(
        title="ModCamp",
        description=f" Showing {member.mention}'s avatar!",
        color=discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
        text="Made by Ekamjot#9133")

    embed.set_image(url=f"{member.avatar_url}")
    await ctx.send(embed=embed)


@av.error
async def av_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-av [member]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    elif isinstance(error, commands.BadArgument):
        await ctx.send("**Sorry! I was not able to find that user!**")


@client.command()
@has_permissions(administrator=True)
async def give(ctx, member: discord.Member, karma: int):
    await ctx.send(f"Gave {karma} karma to {member}. They now have {karma} karma!")


@client.command()
@has_permissions(manage_roles=True)
async def role(ctx, member: discord.Member, *, role: discord.Role):
    await member.add_roles(role)
    embed = discord.Embed(
        title="ModCamp",
        description=f":white_check_mark: **Changed roles for {member}** , ``+{role}`` (role to **{member}** was given by **{ctx.author})**",
        color=discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
        text="Made by Ekamjot#9133")
    await ctx.message.delete()
    await ctx.send(embed=embed)


@role.error
async def role_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"**{ctx.author.mention}** you need ``Manage Roles`` permission for this command!")

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-role [member][role]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send('''**I do not have the permissions to use this command. Please provide me permissions and try again!
**NOTE**:-To assign roles always keep the bot role on top of the role you want to assign!**
Giving me ``Administrator`` permission might fix the issue!''')

    elif isinstance(error, commands.BadArgument):
        await ctx.send("**Sorry I was not able to find that user or the role!**")


@client.command()
@has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, *, role: discord.Role):
    await member.remove_roles(role)
    embed = discord.Embed(
        title="ModCamp",
        description=f":white_check_mark: **Removed roles for {member}** , ``-{role}`` (``{role}`` role of the user **{member}** was removed by **{ctx.author})**",
        color=discord.Color.blue()
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
        text="Made by Ekamjot#9133")
    await ctx.message.delete()
    await ctx.send(embed=embed)


@removerole.error
async def removerole_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"**{ctx.author.mention}** you need ``Manage Roles`` permission for this command!")

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-removerole [member][role]**",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send('''**I do not have the permissions to use this command. Please provide me permissions and try again!**
**NOTE**:-To remove roles always keep the bot role on top of the role you want to remove!
Giving me ``Administrator`` permission might fix the issue!''')

    elif isinstance(error, commands.BadArgument):
        await ctx.send("**Sorry I was not able to find that user!**")


@client.command()
@has_permissions(manage_messages=True)
async def purge(ctx):
    llmit = ctx.message.content[6:]
    await ctx.channel.purge(limit=int(llmit) + 1)

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(
            '''**I do not have permissions to use this command! Please give me permissions and try again!**
**NOTE:-** Giving me ``Administrator`` permission might fix the issue!''')

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention} you need ``Manage Messages`` permission for this command!")


    elif isinstance(error, commands.BadArgument):
        await ctx.send('''**Sorry I was not able to find the messages to purge!**
Please write the number of messages to purge in numbers.
**Examples:-**
-purge 10
-purge 50''')

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-unmute [member]**",
            color=discord.Color.blue()
        )
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! ({round(client.latency * 1000)}ms)")


@client.command()
@has_permissions(manage_roles=True)
async def mute(ctx, *, member: discord.Member, mute_time: int = None):
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(mute_role)
    embed = discord.Embed(
        title="ModCamp",
        description=f":white_check_mark: **{member}** was muted by **{ctx.message.author}**!",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                     text="Made by Ekamjot#9133")
    await ctx.message.delete()
    await ctx.send(embed=embed)


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(
            '''**Please make a role named as ``Muted`` first! or I do not have permissions to use this command! Please give me permissions and try again!**
**NOTE:-** Giving me ``Administrator`` permission might fix the issue!''')

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention} you need ``Manage Roles`` permission for this command!")


    elif isinstance(error, commands.BadArgument):
        await ctx.send("**Sorry I was not able to find that user!**")

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-mute [member]**",
            color=discord.Color.blue()
        )
    await ctx.send(embed=embed)


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

    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024")
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/724158223401091153/c3bea140522f580cd678080274c7d5ba.webp?size=1024",
                     text="Made by Ekamjot#9133")
    await ctx.message.delete()
    await ctx.send(embed=embed)


@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(
            '''**I do not have permissions to use this command! Please give me permissions and try again!**
**NOTE:-** Giving me ``Administrator`` permission might fix the issue!''')

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention} you need ``Manage Roles`` permission for this command!")


    elif isinstance(error, commands.BadArgument):
        await ctx.send("**Sorry I was not able to find that user!**")

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="**Correct Use**",
            description="**-unmute [member]**",
            color=discord.Color.blue()
        )
    await ctx.send(embed=embed)





client.run('NzI0MTU4MjIzNDAxMDkxMTUz.Xu8G5g.MU7bFWvbuhrEFBOXi2S5h8tqExI')
