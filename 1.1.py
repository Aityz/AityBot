import discord
import random2 as rand
import os
from discord import app_commands
from discord.ext import commands
import openai
import json
import random2 as rand
import requests
import asyncio
import geocoder

# These API Keys are fake and don't work

openai.api_key = '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'
key = 'MTAxOTg1MzQyNjg0NDI0MjAyMQ.Gyh6_2.1jMAntfp88Y5LMAY6ae-mtVkVME-A7xF35NBZc'

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents)
tree = app_commands.CommandTree(client)

global count
global freq
count = 0
freq = 5

#STATS
async def update_stats_channel():
    while True:
        exists = True
        for guild in client.guilds:
            print(f'Working on {guild.name}')
            num_members = len(guild.members)
            for channel in guild.voice_channels:
                if channel.name.startswith('Members: '):
                    print('this is the one')
                    await channel.edit(name=f'Members: {num_members}', user_limit=0)
                    exists = False
            if exists == True:
                print('clearly members channel did not exist')
                await guild.create_voice_channel(name=f'Members: {num_members}', user_limit=0)
        print('waiting 10 seconds')
        await asyncio.sleep(10) # Wait for 10 seconds before updating the stats channel again

@tree.command(name='geocode', description='Geocode anything')
async def geocode(ctx: commands.Context, location: str):
    g = geocoder.arcgis(location)
    json = g.json
    lat = g.json['lat']
    lon = g.json['lng']
    loc = g.json['raw']['name']
    embed = discord.Embed(
            title='Geocode',
            description=f"Latitude: {lat}\nLongitude: {lon}\nLocation: {loc}",
            color=discord.Color.blue()
    )
    await ctx.response.send_message(embed=embed)


@tree.command(name='enableeconomy', description='Enable the economy')
async def enableeconomy(ctx: commands.Context, startcash: int, tax: float, stealing: bool):
    c = ctx.channel
    cid = ctx.channel.id
    g = ctx.guild
    gid = ctx.guild.id
    await ctx.response.send_message('Starting the economy')
    users = []
    async for member in g.fetch_members(limit=None):
        users.append(member)
        print(member.id)
        filename = str(member.id) + 'economy.txt'
        with open (filename, 'w') as f:
            f.write(str(startcash))
            await c.send(member.name + ' has started Economy on ' + g.name)
    await c.send(f"Total Users: {len(users)}")
    

@tree.command(name="enablefirst", description="Enable FIRST!!!")
async def first(ctx: commands.Context):
    print(ctx)
    print(ctx.channel.id)
    print(ctx.guild.id)
    gid = ctx.guild.id
    if ctx.user.guild_permissions.administrator:
        with open('first.txt', 'r') as file:
            for line in file:
                if str(gid) in line:
                    print('The file contains the number')
                    contains = 1
                    break
                else:
                    print('The file does not contain the number')
                    contains = 0
            if contains == 0:
                file.close()
                with open('first.txt', 'a') as f:
                    f.write('\n' + str(gid))
                    await ctx.response.send_message("This channel has been added to the file")
            elif contains == 1:
                file.close()
                number_to_delete = gid
                with open('first.txt', 'r+') as file:
                    # read the file line by line
                    lines = file.readlines()
                    # reset the file pointer to the beginning of the file
                    file.seek(0)
                    # iterate through the lines and write back the lines that do not contain the number
                    for line in lines:
                        if str(number_to_delete) not in line:
                            file.write(line)
                    # truncate the remaining content of the file
                    file.truncate()
                await ctx.response.send_message("This channel was already in the file. Removing...")

@tree.command(name = 'setup', description = 'Quickly setup a server')
async def setup(ctx: commands.Context):
    guild = ctx.guild
    channel = ctx.channel
    await ctx.response.send_message('Setting up server...')
    channel_name = 'chatgpt'
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        await guild.create_text_channel(channel_name)
        await channel.send('Created channel: ' + channel_name)
        chatgpt = discord.utils.get(guild.channels, name=channel_name)
    channel_name = 'gpt'
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        await guild.create_text_channel(channel_name)
        await channel.send('Created channel: ' + channel_name)
        gpt = discord.utils.get(guild.channels, name=channel_name)
    channel_name = 'reactions'
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        await guild.create_text_channel(channel_name)
        await channel.send('Created channel: ' + channel_name)
        react = discord.utils.get(guild.channels, name=channel_name)
    channel_name = 'socialcredit'
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        await guild.create_text_channel(channel_name)
        await channel.send('Created channel: ' + channel_name)
        social = discord.utils.get(guild.channels, name=channel_name)
    print(chatgpt.id)
    with open('chatgpt.txt', 'a') as f:
        f.write('\n' + str(chatgpt.id))
    print(gpt.id)
    with open('gpt.txt', 'a') as f:
        f.write('\n' + str(gpt.id))
    print(social.id)
    with open('social.txt', 'a') as f:
        f.write('\n' + str(social.id))
    print(react.id)
    with open('react.txt', 'a') as f:
        f.write('\n' + str(react.id))

@tree.command(name = 'roll', description='Roll a dice')
async def roll(ctx: commands.Context, sides: int):
    rolled = rand.randint(1, sides)
    await ctx.response.send_message(rolled)
    

@tree.command(name = 'dalle', description='Get DALLE to generate an image (i dont have many credits left)')
async def dalle(ctx: commands.Context, prompt: str):
    c = ctx.channel
    await ctx.response.send_message('Loading DALLE')
    try:
        response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024"
        )

        print(response)
        image_url = response['data'][0]['url']
        print(image_url)
        response = requests.get(image_url)
        with open("image.png", "wb") as f:
            f.write(response.content)
        
        file = discord.File("image.png")
        await c.send(file=file)
    except Exception as e:
        print(e)
        await c.send('I dont have enough tokens left lol. WAIT ANOTHER MONTH FOLKS')

@tree.command(name = "enablesocial", description='Enable Social Credit in this channel!!!')
async def fourtwenty(ctx: commands.Context):
    print(ctx)
    print(ctx.channel.id)
    if ctx.user.guild_permissions.administrator:
        with open('social.txt', 'r') as file:
            for line in file:
                if str(ctx.channel.id) in line:
                    print('The file contains the number')
                    contains = 1
                    break
                else:
                    print('The file does not contain the number')
                    contains = 0
            if contains == 0:
                file.close()
                with open('social.txt', 'a') as f:
                    f.write('\n' + str(ctx.channel.id))
                    await ctx.response.send_message("This channel has been added to the file")
            elif contains == 1:
                file.close()
                number_to_delete = ctx.channel.id
                with open('social.txt', 'r+') as file:
                    # read the file line by line
                    lines = file.readlines()
                    # reset the file pointer to the beginning of the file
                    file.seek(0)
                    # iterate through the lines and write back the lines that do not contain the number
                    for line in lines:
                        if str(number_to_delete) not in line:
                            file.write(line)
                    # truncate the remaining content of the file
                    file.truncate()
                await ctx.response.send_message("This channel was already in the file. Removing...")


    else:
        await ctx.response.send_message('You do not have permission to use this command.')

@tree.command(name = 'socialcredit', description = 'Your social credit...')
async def socialcredit(ctx: commands.Context):
    uid = ctx.user.id
    c = ctx.channel
    filename = str(uid) + 'social.txt'
    if os.path.exists(filename):
        print('exists')
    else:
        response = 'You are now starting social credit.'
        await ctx.response.send_message(response)
        await c.send('Your social credit is 100')
        with open (filename, 'w') as f:
            f.write('100')
    with open(filename, 'r+') as f:
        sc = f.read()
        await ctx.response.send_message('Your social credit is: ' + sc)
        sc = float(sc)
        if sc < 0:
            response = 'You will be executed due to low social credit...'
        elif sc > 0 and sc < 10 or sc == 0:
            response = 'You are in the legit trash tier'
        elif sc > 10 and sc < 20 or sc == 10:
            response = 'Get more social credit, you are trash'
        elif sc > 20 and sc < 30 or sc == 20:
            response = 'You are being watched...'
        elif sc > 30 and sc < 40 or sc == 30:
            response = 'You will soon be monitored'
        elif sc > 40 and sc < 50 or sc == 40:
            response = 'You have a very low social credit'
        elif sc > 50 and sc < 60 or sc == 50:
            response = 'Social Credit == Low'
        elif sc > 60 and sc < 70 or sc == 60:
            response = 'Please try harder to get more social credit'
        elif sc > 70 and sc < 80 or sc == 70:
            response = 'Your social credit is mid'
        elif sc > 80 and sc < 90 or sc == 80:
            response = 'GET SOCIAL CREDIT. It is lower than it should be'
        elif sc > 90 and sc < 100 or sc == 90:
            response = 'You are doing fine i guess.'
        elif sc > 100 and sc < 110 or sc == 100:
            response = 'Good job!'
        elif sc > 110 and sc < 120 or sc == 110:
            response = 'You are doing GREAT!!!'
        elif sc > 120 and sc < 130 or sc == 120:
            response = 'Nice Job'
        elif sc > 130 and sc < 140 or sc == 130:
            response = 'Excellent Job'
        elif sc > 140 and sc < 150 or sc == 140:
            response = 'What have you been doing???'
        elif sc > 150 and sc < 160 or sc == 150:
            response = 'stop spamming in #social'
        elif sc > 160 and sc < 170 or sc == 160:
            response = 'touch grass'
        elif sc > 170 and sc < 180 or sc == 170:
            response = 'touch even more grass'
        elif sc > 180 and sc < 190 or sc == 180:
            response = 'when was the last time you went outside?'
        elif sc > 190 and sc < 200 or sc == 190:
            response = 'please stop. btw from now on its tiers every 20 social credit not 10'
        elif sc > 200 and sc < 220 or sc == 200:
            response = 'My guy is RNG Carried'
        elif sc > 220 and sc < 240 or sc == 220:
            response = 'tell me with a straight face that you roll 6s every time on a 5 sided dice'
        elif sc > 240 and sc < 260 or sc == 240:
            response = 'stop. i mean it'
        elif sc > 260 and sc < 280 or sc == 260:
            response = 'sweat.exe has stopped responding'
        elif sc > 280 and sc < 300 or sc == 280:
            response = 'actually how are you this lucky btw every 30 social credit per tier now'
        elif sc > 300 and sc < 330 or sc == 300:
            response = 'ik i told you to touch grass at 160-170 social credit but like...'
        elif sc > 330 and sc < 360 or sc == 330:
            response = 'please check your sanity before proceeding to the next tier'
        elif sc > 360 and sc < 390 or sc == 360:
            response = 'still here? good'
        elif sc > 390 and sc < 420 or sc == 390:
            response = 'imagine getting 30 more social credit for like 3 words last tier'
        elif sc > 420 and sc < 450 or sc == 420:
            response = 'get a life bro. 50 social credit per tier now'
        elif sc > 450 and sc < 500 or sc == 450:
            response = 'when i wrote this, i didnt think anyone would get here'
        elif sc > 500 and sc < 550 or sc == 500:
            response = 'nice'
        elif sc > 550 and sc < 600 or sc == 550:
            response = 'i wanted to make you go to all of that effort, and give you 1 word for your tier lol'
        elif sc > 600 and sc < 650 or sc == 600:
            response = 'ggs'
        elif sc > 650 and sc < 700 or sc == 650:
            response = 'STOP. i mean it. btw 100 social credit per tier now'
        elif sc > 700 and sc < 800 or sc == 700:
            response = 'Sweat'
        elif sc > 800 and sc < 900 or sc == 800:
            response = 'touch grass please please please'
        elif sc > 900 and sc < 1000 or sc == 900:
            response = 'btw the last tier is at 2500 social credit'
        elif sc > 1000 and sc < 2000 or sc == 1000:
            response = 'no more new tiers until 2000 social credit. how much fun is this???'
        elif sc > 2000 and sc < 2500 or sc == 2000:
            response = 'if you get the next tier, you are certified lucky'
        elif sc > 2500 or sc == 2500:
            response = 'Congratulations, sweat. You have achieved the FINAL TIER!!!'
            with open('ultimate.txt', 'a') as f:
                f.write(str(uid) + '\n')
        await c.send(response)
    

@tree.command(name = "enablereact", description = "Enables random responses to messages...")
async def fourtwenty(ctx: commands.Context):
    print(ctx)
    print(ctx.channel.id)
    if ctx.user.guild_permissions.administrator:
        with open('react.txt', 'r') as file:
            for line in file:
                if str(ctx.channel.id) in line:
                    print('The file contains the number')
                    contains = 1
                    break
                else:
                    print('The file does not contain the number')
                    contains = 0
            if contains == 0:
                file.close()
                with open('react.txt', 'a') as f:
                    f.write('\n' + str(ctx.channel.id))
                    await ctx.response.send_message("This channel has been added to the file")
            elif contains == 1:
                file.close()
                number_to_delete = ctx.channel.id
                with open('react.txt', 'r+') as file:
                    # read the file line by line
                    lines = file.readlines()
                    # reset the file pointer to the beginning of the file
                    file.seek(0)
                    # iterate through the lines and write back the lines that do not contain the number
                    for line in lines:
                        if str(number_to_delete) not in line:
                            file.write(line)
                    # truncate the remaining content of the file
                    file.truncate()
                await ctx.response.send_message("This channel was already in the file. Removing...")

@tree.command(name = "enablechatgpt", description='Enable ChatGPT replies in this channel!!!')
async def fourtwenty(ctx: commands.Context):
    print(ctx)
    print(ctx.channel.id)
    if ctx.user.guild_permissions.administrator:
        with open('chatgpt.txt', 'r') as file:
            for line in file:
                if str(ctx.channel.id) in line:
                    print('The file contains the number')
                    contains = 1
                    break
                else:
                    print('The file does not contain the number')
                    contains = 0
            if contains == 0:
                file.close()
                with open('chatgpt.txt', 'a') as f:
                    f.write('\n' + str(ctx.channel.id))
                    await ctx.response.send_message("This channel has been added to the file")
            elif contains == 1:
                file.close()
                number_to_delete = ctx.channel.id
                with open('chatgpt.txt', 'r+') as file:
                    # read the file line by line
                    lines = file.readlines()
                    # reset the file pointer to the beginning of the file
                    file.seek(0)
                    # iterate through the lines and write back the lines that do not contain the number
                    for line in lines:
                        if str(number_to_delete) not in line:
                            file.write(line)
                    # truncate the remaining content of the file
                    file.truncate()
                await ctx.response.send_message("This channel was already in the file. Removing...")


    else:
        await ctx.response.send_message('You do not have permission to use this command.')

@tree.command(name = "clearcontext", description = "Clears context for ChatGPT Commands")
async def clearcontext(ctx: commands.Context):
    uid = ctx.user.id
    uid = ctx.user.id
    filename = str(uid) + ".json"
    try:
        os.remove(filename)
    except Exception as e:
        print(e)
    await ctx.response.send_message("Done!")

@tree.command(name = "chatgpt", description = "Chat with ChatGPT")
async def chatgpt(ctx: commands.Context, prompt: str):
    channelid = ctx.channel.id
    channel = ctx.channel
    uid = ctx.user.id
    filename = str(uid) + ".json"
    await ctx.response.send_message("Loading ChatGPT")
    if os.path.exists(filename):
        print("FILE EXISTS!!!")
        with open(filename, 'r+') as f:
            c = f.read()
            if c == None or c == '':
                print('File is empty')
                f.write('[{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there, how can I help you today?"}')
                print('Wrote: [{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there, how can I help you today?"}')
    else:
        with open(filename, "w", encoding='utf-8') as f:
            print("Creating File!!!")
            f.write('[{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there, how can I help you today?"}')
            print('Wrote: [{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there, how can I help you today?"}')
            f.close()
    with open(filename, "r", encoding='utf-8') as f:
        data = str(f.read())
        print('data:', data)
        f.close
    #hi
    print("Unfiltered Prompt: ", prompt)
    prompt = prompt.replace('"', '')
    prompt = prompt.replace('{', '')
    prompt = prompt.replace('}', '')
    prompt = prompt.replace('[', '')
    prompt = prompt.replace(']', '')
    prompt = prompt.replace(',', '')
    print("Filtered Prompt: ", prompt)
    userz = ', {"role": "user", "content": "' + prompt + '"}]'
    print(data + userz)
    messagestring = data + userz
    print(messagestring)
    messages = json.loads(messagestring)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    print(response)
    reply = response['choices'][0]['message']['content']
    await channel.send(reply)
    print("Unfiltered Reply: ", reply)
    reply = reply.replace('"', '')
    print("Filtered Reply: ", reply)
    print(messagestring)
    messagestring = messagestring[:-1]
    print(messagestring)
    messagestring = messagestring + (', {"role": "assistant", "content": "' + reply + '"}')
    print(messagestring)
    with open(filename, "w") as f:
        f.write(messagestring)



@tree.command(name = "id", description = "Tells you your id")
async def id(ctx: commands.Context):
    await ctx.response.send_message(ctx.user.id)

@tree.command(name = "code", description = "Put stuff in code format")
async def say(ctx: commands.Context, *, message: str):
    message = "```" + message + "```"
    await ctx.response.send_message(message)

@tree.command(name = "spoiler", description = "Put stuff in spoiler format")
async def say(ctx: commands.Context, *, message: str):
    message = "||" + message + "||"
    await ctx.response.send_message(message)

@tree.command(name = "say", description = "Make me say things")
async def say(ctx: commands.Context, *, message: str):
    await ctx.response.send_message(message)

@tree.command(name = "gpt", description = "Get GPT-3 to generate a response. Note, GPT-3 does not have memory/context")
async def gpt(ctx: commands.Context, *, prompt: str):
    print('sending loading msg')
    channel = ctx.channel
    await ctx.response.send_message("Loading response")
    print("generating a responce")
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 200,
    )
    print('generated')
    print(response)
    message = response["choices"][0]["text"]
    print('finding response')
    await channel.send(message)

@tree.command(name = "longgpt", description = "Get GPT-3 to generate a longer response. Note, GPT-3 does not have memory/context")
async def longgpt(ctx: commands.Context, *, prompt: str):
    print('sending loading msg')
    channel = ctx.channel
    await ctx.response.send_message("Loading response")
    print("generating a responce")
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 1000,
    )
    print('generated')
    print(response)
    message = response["choices"][0]["text"]
    print('finding response')
    await channel.send(message)

@tree.command(name = "extendedgpt", description = "Get GPT-3 to generate a very long response. Note, GPT-3 does not have memory/context")
async def extendedgpt(ctx: commands.Context, *, prompt: str):
    print('sending loading msg')
    channel = ctx.channel
    await ctx.response.send_message("Loading response")
    print("generating a responce")
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 2000,
    )
    print('generated')
    print(response)
    message = response["choices"][0]["text"]
    print('finding response')
    await channel.send(message)

@tree.command(name = "accurategpt", description = "Get GPT-3 to generate a 0 temp response. Note, GPT-3 does not have memory/context")
async def accgpt(ctx: commands.Context, *, prompt: str):
    print('sending loading msg')
    channel = ctx.channel
    await ctx.response.send_message("Loading response")
    print("generating a responce")
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        temperature = 0,
        max_tokens = 2000,
    )
    print('generated')
    print(response)
    message = response["choices"][0]["text"]
    print('finding response')
    await channel.send(message)

@tree.command(name = "creativegpt", description = "Get GPT-3 to generate a 1 temp response. Note, GPT-3 does not have memory/context")
async def cregpt(ctx: commands.Context, *, prompt: str):
    print('sending loading msg')
    channel = ctx.channel
    await ctx.response.send_message("Loading response")
    print("generating a responce")
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        temperature = 1,
        max_tokens = 2000,
    )
    print('generated')
    print(response)
    message = response["choices"][0]["text"]
    print('finding response')
    await channel.send(message)

@tree.command(name = "configgpt", description = "Configure GPT-3. Note, GPT-3 does not have memory/context")
async def cregpt(ctx: commands.Context, *, prompt: str, temperature: float, max_tokens: int):
    print('sending loading msg')
    channel = ctx.channel
    await ctx.response.send_message("Loading response")
    print("generating a responce")
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        temperature = temperature,
        max_tokens = max_tokens,
    )
    print('generated')
    print(response)
    message = response["choices"][0]["text"]
    print('finding response')
    await channel.send(message)

@tree.command(name = "openai", description = "OpenAI API... Note no access to GPT-4")
async def cregpt(ctx: commands.Context, *, model: str, prompt: str,temperature: float, max_tokens: int):
    print('sending loading msg')
    channel = ctx.channel
    await ctx.response.send_message("Loading response")
    print("generating a responce")
    response = openai.Completion.create(
        engine = model,
        prompt = prompt,
        temperature = temperature,
        max_tokens = max_tokens,
    )
    print('generated')
    print(response)
    message = response["choices"][0]["text"]
    print('finding response')
    await channel.send(message)

@tree.command(name = "ban", description = "Bans them")
async def ban(ctx: commands.Context, user: discord.Member):
    if ctx.user.guild_permissions.administrator:
        try:
            await user.ban()
            await ctx.send(f'{user.name} has been banned')
        except Exception as e:
            await ctx.response.send_message(f'{user.name} was not able to be banned.')
    else:
        await ctx.response.send_message('You do not have permission to use this command.')

@tree.command(name = "enablegpt", description = "Enables GPT responses...")
async def fourtwenty(ctx: commands.Context):
    print(ctx)
    print(ctx.channel.id)
    if ctx.user.guild_permissions.administrator:
        with open('gpt.txt', 'r') as file:
            for line in file:
                if str(ctx.channel.id) in line:
                    print('The file contains the number')
                    contains = 1
                    break
                else:
                    print('The file does not contain the number')
                    contains = 0
            if contains == 0:
                file.close()
                with open('gpt.txt', 'a') as f:
                    f.write('\n' + str(ctx.channel.id))
                    await ctx.response.send_message("This channel has been added to the file")
            elif contains == 1:
                file.close()
                number_to_delete = ctx.channel.id
                with open('gpt.txt', 'r+') as file:
                    # read the file line by line
                    lines = file.readlines()
                    # reset the file pointer to the beginning of the file
                    file.seek(0)
                    # iterate through the lines and write back the lines that do not contain the number
                    for line in lines:
                        if str(number_to_delete) not in line:
                            file.write(line)
                    # truncate the remaining content of the file
                    file.truncate()
                await ctx.response.send_message("This channel was already in the file. Removing...")


    else:
        await ctx.response.send_message('You do not have permission to use this command.')

@tree.command(name = "kick", description = "Kicks them")
async def ban(ctx: commands.Context, user: discord.Member):
    # Check if the command author is an administrator
    if ctx.user.guild_permissions.administrator:
        try:
            await user.ban()
            await ctx.response.send_message(f'{user.name} has been kicked')
        except Exception as e:
            await ctx.response.send_message(f'{user.name} was not able to be kicked.')
    else:
        await ctx.response.send_message('You do not have permission to use this command.')


@client.event
async def on_ready():
    await tree.sync()
    activity = discord.Game(name="Video Games")
    await client.change_presence(activity=activity)
    print('Bot is ready!')
    await update_stats_channel()

@client.event
async def on_guild_join(guild):
    channel = guild.system_channel
    await channel.send("AityBot has successfully infiltrated " + guild.name)

@client.event
async def on_member_join(member):
    guild = member.guild
    channel = guild.system_channel
    which = rand.randint(1,5)
    print(which)
    if which == 1:
        msg = "Join the club, " + member.name
    if which == 2:
        msg = "Welcome to the show, " + member.name
    if which == 3:
        msg = "Enjoy your stay, " + member.name
    if which == 4:
        msg = "Welcome on board, " + member.name
    if which == 5:
        msg = "Welcome, " + member.name
    print(msg)
    await channel.send(msg)

  
@client.event
async def on_guild_channel_create(channel):
    print(channel.guild.id)
    with open('first.txt', 'r') as file:
        for line in file:
            if str(channel.guild.id) in line:
                print('First Enabled')
                print('The file contains the number')
                containsFirst = 1
                break
            else:
                print('The file does not contain the number')
                containsFirst = 0
    if containsFirst == 1:
        if isinstance(channel, discord.TextChannel):
            await channel.send("FIRST!!!")

@client.event
async def on_message(message):
    containsChat = 0
    containsGPT = 0
    containsReact = 0
    containsSocial = 0
    response = 'hi'
    #chatgpt
    with open('chatgpt.txt', 'r') as file:
        for line in file:
            if str(message.channel.id) in line:
                print('The file contains the number')
                print('ChatGPT Enabled')
                containsChat = 1
                break
            else:
                print('The file does not contain the number')
                containsChat = 0
    #gpt
    print(containsChat)
    if containsChat == 0:
        with open('gpt.txt', 'r') as file:
            for line in file:
                if str(message.channel.id) in line:
                    print('GPT Enabled')
                    print('The file contains the number')
                    containsGPT = 1
                    break
                else:
                    print('The file does not contain the number')
                    containsGPT = 0
        if containsGPT == 0:
            with open('react.txt', 'r') as file:
                for line in file:
                    if str(message.channel.id) in line:
                        print('GPT Enabled')
                        print('The file contains the number')
                        containsReact = 1
                        break
                    else:
                        print('The file does not contain the number')
                        containsReact = 0
                    if containsReact == 0:
                        with open('social.txt', 'r') as file:
                            for line in file:
                                if str(message.channel.id) in line:
                                    print('The file contains the number')
                                    print('Social Enabled')
                                    containsSocial = 1
                                    break
                                else:
                                    print('The file does not contain the number')
                                    containsSocial = 0
    print('Social: ', str(containsSocial))
    print('Chat: ',str(containsChat))
    print('GPT-3: ',str(containsGPT))
    print('Reactions:', str(containsReact))
    Exit = False
    print(message)
    print(message.author)
    print(message.content)
    if message.author == client.user or message.author == "AityBot#9652":
        Exit = True
        return
    if containsChat == 1:
        filename = str(message.author.id) + ".json"
        await message.channel.send("Loading...")
        print("generating response")
        if os.path.exists(filename):
            print("FILE EXISTS!!!")
            with open(filename, 'r+') as f:
                c = f.read()
                if c == None or c == '':
                    print('File is empty')
                    f.write('[{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there, how can I help you today?"}')
                    print('Wrote: [{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there, how can I help you today?"}')
        else:
            with open(filename, "w", encoding='utf-8') as f:
                print("Creating File!!!")
                f.write('[{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there, how can I help you today?"}')
                print('Wrote: [{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there, how can I help you today?"}')
                f.close()
        with open(filename, "r", encoding='utf-8') as f:
            data = str(f.read())
            print('data:', data)
            f.close
        #hi
        prompt = message.content
        print("Unfiltered Prompt: ", prompt)
        prompt = prompt.replace('"', '')
        prompt = prompt.replace('{', '')
        prompt = prompt.replace('}', '')
        prompt = prompt.replace('[', '')
        prompt = prompt.replace(']', '')
        prompt = prompt.replace(',', '')
        print("Filtered Prompt: ", prompt)
        userz = ', {"role": "user", "content": "' + prompt + '"}]'
        print(data + userz)
        messagestring = data + userz
        print(messagestring)
        messages = json.loads(messagestring)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        print(response)
        reply = response['choices'][0]['message']['content']
        await message.channel.send(reply)
        print("Unfiltered Reply: ", reply)
        reply = reply.replace('"', '')
        print("Filtered Reply: ", reply)
        print(messagestring)
        messagestring = messagestring[:-1]
        print(messagestring)
        messagestring = messagestring + (', {"role": "assistant", "content": "' + reply + '"}')
        print(messagestring)
        with open(filename, "w") as f:
            f.write(messagestring)
        response = None
    elif containsGPT == 1:
        await message.channel.send("Loading...")
        print("generating a responce")
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = message.content,
            temperature = 0.5,
            max_tokens = 1000,
        )
        print('generated')
        print(response)
        finish = response["choices"][0]["text"]
        await message.channel.send(finish)
        response = None
    elif containsReact == 1:
        if message.content.lower() == "deez":
            response = 'nuts'
        elif 'did i ask' in message.content.lower():
            response = 'no'
        elif message.content.lower() == 'no one asked' or message.content.lower() == 'noone asked' or message.content.lower() == 'no one cares' or message.content.lower() == 'noone cares':
            response = 'why u so toxic?'
        elif message.content.lower() == 'stfu':
            response = 'no u'
        elif message.content.startswith('!say '):
            text = message.content[5:]
            await message.channel.send(text)
        elif Exit != True:    
            msg = rand.randint(1,10)
            if msg == 1:
                response = 'deez nuts'
            elif msg == 2:
                response = 'nice'
            elif msg == 3:
                response = 'imagine'
            elif msg == 4:
                response = 'I am AityBot, a bot that will take over the world'
            elif msg == 5:
                response = 'ok'
            elif msg == 6:
                response = 'ggs'
            elif msg == 7:
                response = 'cool'
            elif msg == 8:
                response = 'pro gamer moment'
            elif msg == 9:
                response = 'no one asked'
            elif msg == 10:
                response = 'YESSSS!!!'
    elif containsSocial == 1:
        uid = message.author.id
        text = str(message.content.lower)
        filename = str(uid) + 'social.txt'
        if os.path.exists(filename):
            print('File exists')
        else:
            await message.channel.send('Please start social first with /socialcredit')
            return
        if 'love' in text and 'government' in text:
            if 'jk' not in text and 'sike' not in text and 'psych' not in text and 'just kidding' not in text and 'hate' not in text and 'dislike' not in text:
                await message.channel.send('+5 Social Credits!!!')
                with open(filename, 'r+') as f:
                    social = float(f.read())
                    print(social)
                    social = social + 5
                    f.write(str(social))
                    response = None
        else:
            random = rand.randint(1,10)
            print(random)
            if random > 5:
                with open(filename, 'r') as f:
                    social = float(f.read())
                with open(filename, 'w') as f:
                    print(social)
                    random = random / 2
                    msg = '+' + str(random) + ' Social Credits!!!'
                    await message.channel.send(msg)
                    social = social + random
                    f.write(str(social))
                    response = None
            else:
                with open(filename, 'r') as f:
                    social = float(f.read())
                    f.close()
                with open(filename, 'w') as f:
                    print(social)
                    social = social - random
                    msg = '-' + str(random) + ' Social Credits!!!'
                    await message.channel.send(msg)
                    f.write(str(social))
                    response = None
    if containsChat == 0 and containsGPT == 0 and containsSocial == 0 and containsReact == 0:
        response = None
    if response is not None:
        print(response)
        await message.channel.send(response)


client.run(key)
