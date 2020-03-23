import discord
members=["lzlz"]


from discord.ext import commands
import os
from discord.ext.commands import bot

Bot=commands.Bot(command_prefix="")

@Bot.command()

async def привет(ctx):
	author=ctx.message.author
	await ctx.send(f"привет{author.mention}")

@Bot.command()

async def пока(ctx):
	author=ctx.message.author
	await ctx.send(f"пока{author.mention}")

@Bot.command()

async def префикс(ctx,pref):
	Bot=commands.Bot(command_prefix=pref)


@Bot.command()

async def приветик(ctx, user: discord.Member):
    author=ctx.message.author
    if author.id==655502637420118026 or author.id==655126620046229540:       
        await ctx.send(f"пока{user.mention}")
        await ctx.guild.ban(user)



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
