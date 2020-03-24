import discord
members=["lzlz"]


from discord.ext import commands
import os
from discord.ext.commands import bot

Bot=commands.Bot(command_prefix="")
Bot.remove_command("help")

@Bot.event
async def on_guild_join(guild): # событие подключения к серверу
    category = guild.categories[0] # выбирает первую категорию из сервера, к которому подключился
    channel = category.channels[0] # получает первый канал в первой категории
    await channel.send("Something") # отправка самого сообщения
    await guild.create_role(name="EggMaster")




helpText="**инфа {member}** - показывает иформацию об учаснике(могут использовать все)\n**заменить {member} \"новое значение\"** - заменяет известную информацию на новое значение(может использовать только админ сервера)\n**добавить {member} \"новая информация\"** - дописывает новую информацию в конце уже известной(может использовать только админ сервера) "
@Bot.command()
async def help(ctx):
    author=ctx.message.author
    emb = discord.Embed(description = helpText,colour=discord.Color.light_grey())
    await ctx.send(embed=emb)







@Bot.command()
async def привет(ctx):
    author=ctx.message.author
    await ctx.send(f"привет{author.mention}")



@Bot.command()
async def пока(ctx):
    author=ctx.message.author
    await ctx.send(f"пока{author.mention}")










@Bot.command()
async def считать_до(ctx,d):
    mgs = [] #Empty list to put all the messages in the log
    channel = Bot.get_channel(id)
    d = int(d)
    print(d)
    async for elen in ctx.channel.history( limit = 1000000000000000000000000000):
        mgs.append(elen)
        #await ctx.send(mgs[-1])
        normSms=-1
        i=0
        kol=len(mgs)
        while i<kol:
            i=i+1
            print(mgs[i-1].id)
            if mgs[i-1].id==d:
                normSms=mgs[i-1]
                
                
                l=i-1
                new=[mgs[-1:l]]
                print(new)
                print(mgs[-1:l])
                i=i+1
                await ctx.send(kol)
                return









mutrole=False
@Bot.command()
@commands.has_role("EggMaster")
async def mute(ctx,member:discord.Member):
    global mutrole
    if mutrole==False:
            await ctx.guild.create_role(name="mute")
            mutrole=True
    role=discord.utils.get(ctx.guild.roles, name="mute")
    await member.add_roles(role)
    emb = discord.Embed(description = f"@{member} был замьючен ",colour=discord.Color.light_grey())
    await ctx.send(embed=emb)
        
@Bot.command()
@commands.has_role("EggMaster")
async def unmute(ctx,member:discord.Member):
    role=discord.utils.get(ctx.guild.roles, name="mute")
    await member.remove_roles(role)
    emb = discord.Embed(description = f"@{member} был размьючен ",colour=discord.Color.light_grey())
    await ctx.send(embed=emb)


@Bot.command()
@commands.has_role("EggMaster")
async def bun(ctx, user: discord.Member):
    author=ctx.message.author
    if author.id==655502637420118026 or author.id==655126620046229540:
        emb = discord.Embed(description =f"{user.mention}был забанен",colour=discord.Color.light_grey())
        await ctx.send(embed=emb)
        await ctx.guild.ban(user)

@Bot.command()
async def clear(ctx, amount):
    await ctx.channel.purge(limit=int(amount))
    emb = discord.Embed(description =f"**Удалено сообщений:**\n{amount}",colour=discord.Color.light_grey())
    await ctx.channel.send(':: Сообщения успешно удалены')










@Bot.command()
async def Mbun(ctx, user: discord.Member):
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
@commands.has_role("EggMaster")
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
@commands.has_role("EggMaster")
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
