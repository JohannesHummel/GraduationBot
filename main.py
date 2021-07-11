import discord
import os
from client import send_data
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #await message.channel.send(embed=create_welcome_embed())
    answer = send_data(message)
    
    await message.reply(answer)
    if 'can I help you' in answer: 
       await message.channel.send(embed=create_welcome_embed())


def create_welcome_embed():
    #### Create the initial embed object ####
    embed=discord.Embed(title="Graduation Bot", url="https://realdrewdata.medium.com/", description=" I'm a Bot that can help you writing your thesis, paper or essay. My functions are:", color=0x109319)

    # Add author, thumbnail, fields, and footer to the embed
    #embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")

    #embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")

    embed.add_field(name="Paper Search", value="Search for Papers of certain Topics.\n Use the following format: \n \n > I want to search a paper \n", inline=False) 
    embed.add_field(name="Latex", value="Ask questions about the writing of your paper or thesis in latex.\n Use the following format: \n \n > How can I create a list in latex?\n \n or \n \n > Can you help me find a professor? \n", inline=False)
    #embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)

    embed.set_footer(text="You have any further questions? Then you can get a list of all available functions with: \n What are your functions?")

    return embed
load_dotenv('.env')
client.run(os.getenv('TOKEN'))
