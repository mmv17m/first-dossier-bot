import discord

servers={  
}
votes={}


from discord.ext import commands
import os
from discord.ext.commands import bot



Bot=commands.Bot(command_prefix="")
Bot.remove_command("help")




@Bot.event
async def on_guild_join(guild): # событие подключения к серверу
    servers[guild.id]={
        "members":["lzlz"],
        "mut_role":False
    }
    category = guild.categories[0] # выбирает первую категорию из сервера, к которому подключился
    channel = category.channels[0] # получает первый канал в первой категории
    await channel.send("Привет,я EggBot, бот с упрощенным управлением и минимальными настройками, список моих команд можно узнать написав help(без префикса).Административными командами может пользоваться только участник с ролью EggMaster, которая создается при входе на сервер, если по какой-то причине роль не создалась, необходимо создать ее вручную. Простыми командами может пользоваться каждый") # отправка самого сообщения
    await guild.create_role(name="EggMaster")




@Bot.command()
async def link(ctx):
    author=ctx.message.author
    await ctx.send("Привет,я EggBot, бот с упрощенным управлением и минимальными настройками,  список моих команд можно узнать написав help(без префикса).Административными командами может пользоваться только участник с ролью EggMaster,  которая создается при входе на сервер, если по какой-то причине роль не создалась, необходимо создать ее вручную. Простыми командами может пользоваться каждый. На данный момент с моей помощью можно быстро создавать открытые и анонимные голосования,  удобно собирать и просматривать информацию об участниках, а так же управлять сообщениями и текстовыми каналами, и другие, в том числе, стандартые функции. Следите за обновлениями, так как создатели еще не забили на меня))) https://discordapp.com/oauth2/authorize?client_id=691227190729375784&permissions=8&scope=bot")

    

@Bot.command()
#@commands.has_role("EggMaster")
async def help(ctx):
    author=ctx.message.author
    role=discord.utils.get(ctx.guild.roles, name="EggMaster")
    emb=""
    if role in author.roles:
        emb = discord.Embed(description = "Вот команды, которые ты можешь использовать  \n Команды пишутся без префикса\n __*help*__ - Выдает список доступных команд \n __*link*__ - Дает ссылку и краткое описание бота \n **Регулятивные команды:**\n Стандартные команды для наказания участников\n __*bun*__{member} - банит указаного участника \n __*mute*__{member} - мутит указаного участника\n __*unmute*__{member} - снятие мута с указаного участника\n **Текстовые команды:**\n Команды для контроля за текстовыми каналами\n  __*find*__{\"text\"} - Выдает сколко раз каждый участник употреблял указанную фразу, полезно для отлова фейков \n __*clear*__{number} - Стирает указанное число сообщений, начиная с последнего \n __*count*__{id} - считает сколько сообщений было отправлено с указаного Id сообщения\n **Команды для голосований:**\n Помогает создавать как анонимные, так и открытые голосования __*StartVote*__{number} - Запускает голосование с указанным числом участников \n __*rename*__{number} {\"text\"} - Переименовывает кандидата с указанным номером \n __*VoteList*__ - Выдает список кандидатов с их номером голосования, можно использовать как в каналах сервера, так и в личных сообщениях с ботом \n __*vote*__{number} - Отдать голос за кандидата с указаным номером, можно использовать как в каналах сервера, так и в личных сообщениях с ботом  \n __*EndVote*__ - Закончить голосование, подведение итогов \n **Команды информации об участнике:**\n Информация об участнике помогает другим людям знать, как правильно общаться с выбранным участником. Рекомендуется сохранять всю информацию т.к. при обновлении бота вся известная информация стирается. \n__*info*__{member} - выдает всю записанную информацию об участнике\n __*reset*__{member} {\"text\"} - заменяет известную информацию на новую\n __*add*__{member} {\"text\"} - дополняет известную информацию новой\n",colour=discord.Color.light_grey())
    else:
         emb = discord.Embed(description = "Вот команды, которые ты можешь использовать \n Команды пишутся без префикса\n __*help*__-Выдает список доступных команд\n __*link*__ - Дает ссылку и краткое описание бота \n __*VoteList*__ - Выдает список кандидатов с их номером голосования, можно использовать как в каналах сервера, так и в личных сообщениях с ботом  \n __*vote*__{number} - отдать голос за кандидата с указаным номером, можно использовать как в каналах сервера, так и в личных сообщениях с ботом  \n __*count*__{id} - считает сколько сообщений было отправлено с указаного Id сообщения\n",colour=discord.Color.light_grey())
    await ctx.send(embed=emb)






@Bot.command()
@commands.has_role("EggMaster")
async def StartVote(ctx, kol: int):
    j=0
    modno=0
    idd=""
    while j<len(votes)and modno==0:
        if len(votes[j])==0:
            modno=1
            idd=j
            votes[j]={
            "vote_nick":[],
            "golos":[],
            "ludi":[],
            "kolic":kol,
            "serv":ctx.guild
            }
        j=j+1
    if modno==0:
        print("ypa")
        modno=1
        idd=j
        votes[j]={
        "vote_nick":[],
        "golos":[],
        "ludi":[],
        "kolic":kol,
        "serv":ctx.guild
        }
        
        print(votes[idd]["kolic"])
        

    
    i=0
    while i<=votes[idd]["kolic"]:
        print("1")
        votes[idd]["vote_nick"].append(i+1)        
        i=i+1
    z=0
    while z<kol:
        votes[idd]["golos"].append(0)
        z=z+1
    emb = discord.Embed(description = f"голосование успешно началось,Id голосования-{idd}",colour=discord.Color.light_grey())
    await ctx.send(embed=emb)  



@Bot.command()
async def vote(ctx, kol: int, idd: int):
    print("ok")
    if len(votes[idd])>0:
        if ctx.author in votes[idd]["serv"].members:
            print(votes[idd]["serv"].members)
            if kol<=votes[idd]["kolic"] and kol != 0:
                print("ok")
                if ctx.author.id in votes[idd]["ludi"]:
                    print("ok6")
                    emb = discord.Embed(description = "вы уже голосовали",colour=discord.Color.light_grey())
                    await ctx.send(embed=emb)
                else:
                    print("ok7")
                    votes[idd]["ludi"].append(ctx.author.id)
                    nick=votes[idd][ "vote_nick"]
                    votes[idd]["golos"][kol-1]=votes[idd]["golos"][kol-1]+1
                    emb = discord.Embed(description = f"Вы проголосовали за: {nick[kol-1]}",colour=discord.Color.light_grey())
                    await ctx.send(embed=emb)


@Bot.command()
async def VoteList(ctx, idd: int):
    if len(votes[idd])>0:
        i=0
        text=""
        while i<len(votes[idd]["golos"]):
            print("dl")
            nick=votes[idd][ "vote_nick"]
            text=f"{text} {i+1}) __*{nick [i]}*__\n"
            i=i+1
        emb = discord.Embed(description = text,colour=discord.Color.light_grey())
        await ctx.send(embed=emb)



@Bot.command()
@commands.has_role("EggMaster")
async def rename(ctx, idd: int, num: int, nam: str):
    if len(votes[idd])>0:
        if num<=votes[idd]["kolic"] and num !=0:
            votes[idd]["vote_nick"][num-1] = nam




@Bot.command()
@commands.has_role("EggMaster")
async def EndVote(ctx, idd: int):
    print(votes[idd])
    if len(votes[idd])>0:
        i=0
        text=""
        while i<len(votes[idd]["golos"]):
            print("dl")
            nick=votes[idd][ "vote_nick"]
            ick=votes[idd][ "golos"]
            text=f"{text} __*{nick[i]}*__:\n  {ick[i]} голосов \n"
            i=i+1
        emb = discord.Embed(description = text,colour=discord.Color.light_grey())
        await ctx.send(embed=emb)
        votes[idd].clear()
        
        
    
    




@Bot.command()
async def привет(ctx):
    author=ctx.message.author
    await ctx.send(f"привет{author.mention}")



@Bot.command()
async def пока(ctx):
    author=ctx.message.author
    await ctx.send(f"пока{author.mention}")









@Bot.command()
async def count(ctx,d):
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



@Bot.command()
@commands.has_role("EggMaster")
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



















@Bot.command()
@commands.has_role("EggMaster")
async def mute(ctx,member:discord.Member):
    if servers[ctx.guild.id]["mut_role"]==False:
            await ctx.guild.create_role(name="mute")
            servers[ctx.guild.id]["mut_role"]==True
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
    emb = discord.Embed(description =f"{user.mention}был забанен",colour=discord.Color.light_grey())
    await ctx.send(embed=emb)
    await ctx.guild.ban(user)

@Bot.command()
@commands.has_role("EggMaster")
async def clear(ctx, amount):
    await ctx.channel.purge(limit=int(amount))
    emb = discord.Embed(description =f"**Удалено сообщений:**\n{amount}",colour=discord.Color.light_grey())
    await ctx.channel.send(embed=emb)












@Bot.command()
@commands.has_role("EggMaster")
async def info(ctx, member:discord.Member):
    m=member
    vid="нет значения"
    i=0
    kol=len(servers[ctx.guild.id]["members"])
    while i<kol:
        i+=1
        if servers[ctx.guild.id]["members"][i-1][0]==m:
            vid=servers[ctx.guild.id]["members"][i-1][1]
                        
                        
    emb = discord.Embed(description = vid,colour=discord.Color.light_grey())
    await ctx.send(embed=emb)
    print(servers[ctx.guild.id]["members"])




@Bot.command()
@commands.has_role("EggMaster")
async def reset(ctx, member:discord.Member, text ):
    m=member
    servers[ctx.guild.id]["members"]=[m,text]
    servers[ctx.guild.id]["members"].append(member)

    vid="нет значения"
    i=0
    kol=len(servers[ctx.guild.id]["members"])
    while i<kol:
        i+=1
        if servers[ctx.guild.id]["members"][i-1][0]==m:
            vid=servers[ctx.guild.id]["members"][i-1][1]
                        
       
    emb = discord.Embed(description = vid,colour=discord.Color.light_grey())
    await ctx.send(embed=emb)
    print(servers[ctx.guild.id]["members"])



@Bot.command()
@commands.has_role("EggMaster")
async def add(ctx, member:discord.Member, text ):
    m=member

    vid="нет значения"
    i=0
    kol=len(servers[ctx.guild.id]["members"])
    while i<kol:
        i+=1
        if servers[ctx.guild.id]["members"][i-1][0]==m:
            s=servers[ctx.guild.id]["members"][i-1][1]
            servers[ctx.guild.id]["members"][i-1][1]=f"{s} {text}"
            vid=servers[ctx.guild.id]["members"][i-1][1]
                        
       
    emb = discord.Embed(description = vid,colour=discord.Color.light_grey())
    await ctx.send(embed=emb)
    print(servers[ctx.guild.id]["members"])















token = os.environ.get("BOT_TOKEN")
Bot.run(str(token))
