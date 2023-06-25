import discord
from discord import app_commands
from discord.ext import commands
from confidential import TOKEN, NEWSAPI, OPENWEATHERMAP
import requests
import geocoder
import os
from gen1 import GEN1_LOOT, select_pokemon
from gradio_client import Client

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print('Ready!')
    await tree.sync()

@client.event
async def on_reaction_add(reaction, user):
    filename = f'{reaction.message.author.id}userkarma.txt'
    print(filename)
    react = str(reaction.emoji)
    print(f'Reaction added {react}')
    me = reaction.me
    count = reaction.count
    if count == 1 and me == True:
        return
    elif user.id == reaction.message.author.id:
        print('id = author')
        embed = discord.Embed(title="Don't Upvote/Downvote Yourself!", description='Just a friendly reminder not to upvote/downvote yourself.')
        await user.send(embed=embed)
    elif react == '⬆️':
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                karma = int(f.read())
            with open(filename, 'w') as f:
                karma = karma + 1
                f.write(str(karma))
            print('+1')
        else:
            with open(filename, 'w') as f:
                f.write(str(1))
                print('+1')
    elif react == '⬇️':
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                karma = int(f.read())
            with open(filename, 'w') as f:
                karma = karma - 1
                f.write(str(karma))
            print('-1')
        else:
            with open(filename, 'w') as f:
                f.write(str(0))
                print('-1')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        karma = True
        file = str(message.guild.id) + 'karma.txt'
        if os.path.exists(file):
            with open(file, 'r') as f:
                contents = f.read()
                if contents == '1':
                    karma = True
                else:
                    karma = False
        else:
            with open(file, 'w') as f:
                f.write(str(1))
                karma = True
        if karma == True:
            await message.add_reaction('⬆️')
            await message.add_reaction('⬇️')

@tree.command(name='userid', description='Get the User ID of Anyone')
async def test(interaction: discord.Interaction, user: discord.User):
    embed = discord.Embed(title='User ID', description=f'User ID: {user.id}')
    await interaction.response.send_message(embed=embed)



@tree.command(name='weather', description='Get the weather from anywhere!')
async def weather(interaction: discord.Interaction, loc: str):
    geo = geocoder.arcgis(loc)
    geo = geo.json
    lat, lon = geo['lat'], geo['lng']
    callurl = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHERMAP}'
    response = requests.get(callurl)

    if response.status_code == 200:
        data = response.json()
    else:
        await interaction.response.send_message("Error: Unable to fetch weather data.")

    embed = discord.Embed(title='Weather', description=f'Location: {geo["address"]}\nTemperature: {round(data["main"]["temp"] - 273.15, 2)}\nMinimum Temperature: {round(data["main"]["temp_min"] - 273.15, 2)}\nMaximum Temperature: {round(data["main"]["temp_max"] - 273.15, 2)}\nDescription: {data["weather"][0]["description"]}')

    await interaction.response.send_message(embed=embed)

@tree.command(name='news', description='Get the headlines from the US!')
async def news(interaction: discord.Interaction):
    url = "https://newsapi.org/v2/top-headlines"
    parameters = {
        "country": "us",
        "apiKey": NEWSAPI
    }
    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        data = response.json()
    else:
        await interaction.response.send_message("Error:", response.status_code)

    articles = data['articles']
    titles = []

    for article in articles:
        titles.append(article['title'])

    embed = discord.Embed(title='News Headlines')

    for index, title in enumerate(titles):
        embed.add_field(name=f"{index + 1}", value=title, inline=False)
    await interaction.response.send_message(embed=embed)

@tree.command(name='gen1', description="Catch a Generation 1 Pokemon!")
async def gen1(interaction: discord.Interaction):
    pokemon = select_pokemon(GEN1_LOOT)
    embed = discord.Embed(title='Your Catch', description=f'You Caught {pokemon}')
    await interaction.response.send_message(embed=embed)
@tree.command(name='karma', description='Check your Karma!')
async def karma(interaction: discord.Interaction, user: discord.User = None):
    if user is not None:
        filename = f'{user.id}userkarma.txt'
    
    try:
        with open(filename, 'r') as f:
            karma = int(f.read())
            embed = discord.Embed(title='Your Karma!', description=f'Currently your Karma is {karma}')
            await interaction.response.send_message(embed=embed)
    except Exception as e:
        embed = discord.Embed(title='Error', description='That user has not yet started Karma!')
        await interaction.response.send_message(embed=embed)

@tree.command(name='geocode', description="Geocode any location using ArcGIS.")
async def geocode(interaction: discord.Interaction, location: str):
    g = geocoder.arcgis(location)
    g = g.json
    embed = discord.Embed(title="Geocoder Results", description=f"Location: {g['address']}\nLatitude: {g['lat']}\nLongitude: {g['lng']}")
    await interaction.response.send_message(embed=embed)

@tree.command(name="ping", description="Pong!")
async def ping(interaction: discord.Interaction):
    embed = discord.Embed(title="PONG!", description=f"Pong!")
    await interaction.response.send_message(embed=embed)

@tree.command(name="help", description="Get help on how to use AityBot")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="AityBot Tutorial", description="Welcome to AityBot! AityBot is a multipurpose bot made for many different situations!")
    commandshelpbutton = discord.ui.Button(label="Commands", style=discord.ButtonStyle.blurple)
    settingupbutton = discord.ui.Button(label="Setting Up", style=discord.ButtonStyle.green)
    async def commands_callback(interaction):
        commandsembed = discord.Embed(title="AityBot Commands", description="AityBot has many different commands. Here is a full list of all of them, and a brief description")
        await interaction.response.send_message(embed=commandsembed)
    async def settingup_callback(interaction):
        settingupembed = discord.Embed(title="Setting Up AityBot", description="Setting up AityBot is easy! All you have to do is add AityBot to your server, and then you can use the commands! However to get more specific settings, use /setup")
        await interaction.response.send_message(embed=settingupembed)
    commandshelpbutton.callback = commands_callback
    settingupbutton.callback = settingup_callback
    view = discord.ui.View()
    view.add_item(settingupbutton)
    view.add_item(commandshelpbutton)
    await interaction.response.send_message(embed=embed, view=view)

@tree.command(name='gpt2eli5', description='Use a Casual LLM trained by Aityz (DistilGPT2 on Eli5 Dataset)')
async def gpt2eli5(interaction: discord.Interaction, prompt: str, max_tokens: int = 100):
    c = interaction.channel
    await interaction.response.send_message('Loading')
    client = Client("https://aityz-aityz-model-eli5.hf.space/")
    result = client.predict(
				prompt,	# str representing input in 'input' Textbox component
				max_tokens,	# int | float representing input in 'maxtokens' Slider component
				api_name="/predict"
    )
    embed = discord.Embed(title='Result', description=result)
    await c.send(embed=embed)


@tree.command(name="setup", description="Tune AityBot however you like.")
async def setup(interaction: discord.Interaction):
    embed = discord.Embed(title='Setup AityBot!', description='Time to tune AityBot to your liking!')
    config = discord.ui.Button(label='Karma')
    async def ph1_callback(interaction):
        karmaembed = discord.Embed(title='Karma Settings!', description='Here you can enable or disable Karma!')
        karmaview = discord.ui.View()
        karmatrue = discord.ui.Button(label='Enable')
        karmafalse = discord.ui.Button(label='Disable')
        async def true(interaction):
            file = str(interaction.guild.id) + 'karma.txt'
            with open(file, 'w') as f:
                f.write(str(1))
            await interaction.response.send_message('Done!')
        async def false(interaction):
            file = str(interaction.guild.id) + 'karma.txt'
            with open(file, 'w') as f:
                f.write(str(0))
            await interaction.response.send_message('Done!')
        karmatrue.callback = true
        karmafalse.callback = false
        karmaview.add_item(karmatrue)  
        karmaview.add_item(karmafalse)    
        await interaction.response.send_message(embed=karmaembed, view=karmaview)
    config.callback = ph1_callback
    view = discord.ui.View()
    view.add_item(config)
    await interaction.response.send_message(embed=embed, view=view)

client.run(TOKEN)