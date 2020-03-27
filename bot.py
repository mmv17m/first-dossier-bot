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




helpText=" ще не готов"
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


@commands.has_role("EggMaster")
@Bot.command()
async def find(ctx,txt:str):
    guild=ctx.guild
    emb = discord.Embed(description = "операция выполняется...",colour=discord.Color.light_grey())
    await ctx.send(embed=emb)
    prob=["никто",0]
    num=[prob]

    kol=0
    i=0
    while i<len(guild.categories):
        category=guild.categories[i]
        j=0
        while j<len(category.channels):
            channel=category.channels[j]
            if channel.type ==discord.ChannelType.text:
                print("ok1")
                
                
                k=0
                mgs=[]
                
                async for elen in channel.history( limit = 1000000000000000000000000000):
                    mgs.append(elen)
                    print("ok2")
                while k<len(mgs):
                    print("ok3")
                    m=mgs[k]
                    if txt in m.content:
                        print("ok4")
                        z=0
                        key=0
                        while z<len(num) and key==0:
                            print("ok5")
                            if num[z][0]==m.author.name:
                                print("ok6")
                                num[z][1]=num[z][1]+1
                                key=1
                            z=z+1

                        if key==0:
                            print("ok7")
                            goil=[m.author.name,1]
                            num.append(goil)
                            #emb = discord.Embed(description = num[],colour=discord.Color.light_grey())
                            #await ctx.send(num)
                            print(num)
                        kol=kol+1
                        
                    k=k+1
            j=j+1
        i=i+1
    n=0
    if len(num) != 0:
        while n<len(num):
            print("ok8")
            #emb = discord.Embed(description = f"@{num[n][0]} - {num[n][1]}",colour=discord.Color.light_grey())
            await ctx.send(f"@{num[n][0]} - {num[n][1]}")
            n=n+1
    emb = discord.Embed(description = f"Операция выполнена. Всего:{kol}",colour=discord.Color.light_grey())
    await ctx.send(embed=emb)    


















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
