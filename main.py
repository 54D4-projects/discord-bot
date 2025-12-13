import discord
from discord.ext import commands, tasks
import requests
import json
from discord.ui import Button, View
import openai

api_url = 'https://api.api-ninjas.com/v1/bitcoin'


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
intents.message_content = True 
intents.reactions = True
intents.messages = True

OPENAI_API_KEY = "OPEN_API_KEY"
CHANNEL_ID = "CHANEL_ID_1"
CHANNEL_2_ID = "CHANEL_ID_2"
TICKET_CHANNEL = "TICKET_CHANNEL"

ticket_embed = discord.Embed(
    title = "Ticket",
    description="How to use helper AI bot.",
    color=discord.Color.from_str('#56e1da')
    
)
ticket_embed.set_author(name="FEM Trading $", icon_url="https://cdn.discordapp.com/attachments/1350926300097019965/1350954063667138762/logo_fem.png?ex=67d94644&is=67d7f4c4&hm=b259bc020beb2b954667b34c181456fb99ecf43a6243cdc5934ff5e8d3ca715b&")
ticket_embed.add_field(name="!pomoc",value="Wygeneruje odpowiedz od Ai")
ticket_embed.add_field(name="!pomoc_admina",value="Wyśle wiadomość do admina.")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    send_bitcoin_track.start()
    
    channel = bot.get_channel(TICKET_CHANNEL)
    if channel:
        await channel.send("Click the button below!", view=MyView())
    else:
        print("Channel not found!")
    
response = requests.get(api_url, headers={'X-Api-Key': 'UVYTIbdn9zuRUyPhsrXBIQ==YJWx2tunC4TFhhkD'})
if response.status_code == requests.codes.ok:
    json_data = json.loads(response.text)
    cena = float(json_data['price'])
    m24h_high = float(json_data['24h_high'])
    m24h_low = float(json_data['24h_low'])
    embed = discord.Embed(
        title="Bitcoin - BTC",
        description="Check the latest **[BTC price](https://www.coinbase.com/pl/price/bitcoin)**!",
        color=discord.Color.from_str('#56e1da')
    )
    embed.set_author(name="FEM Trading $", icon_url="https://cdn.discordapp.com/attachments/1350926300097019965/1350954063667138762/logo_fem.png?ex=67d94644&is=67d7f4c4&hm=b259bc020beb2b954667b34c181456fb99ecf43a6243cdc5934ff5e8d3ca715b&")
    embed.add_field(name="🪙 Price: ", value="$"+ str(cena), inline=False)
    embed.add_field(name="↗️ High:", value="$"+str(m24h_high), inline=True)
    embed.add_field(name="↙️ Low:", value="$"+str(m24h_low), inline=True)
    embed.add_field(name="📈 Change:", value=json_data['24h_price_change_percent']+"%", inline=True)
   

@tasks.loop(hours=1)
async def send_bitcoin_track():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(embed=embed)
        print(f'messege sent')
    else:
        print("Error:", response.status_code, response.text)

 
@bot.command()
async def ticket(ctx):
    guild = bot.get_guild(ctx.guild_id)
    channel = bot.get_channel(1351307620576919694)
    nickname = ctx.user.name
    existing_channel = discord.utils.get(guild.channels, name=nickname+"_ticket")
    category = discord.utils.get(guild.categories, name="╰•★★★tickets★★★•╯")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),  # Hide from everyone
        ctx.user: discord.PermissionOverwrite(read_messages=True, send_messages=True)  # Allow user
    }

    if existing_channel:
        await channel.send(f"A channel named `{nickname}_ticket` already exists!")
        return
    # Create the text channel
    new_channel = await guild.create_text_channel(name=nickname+"_ticket",
                                                  category=category,
                                                  topic=f"Support ticket for {nickname}",
                                                    overwrites=overwrites)
    await new_channel.send(embed=ticket_embed)
    await channel.send(f"Text channel `{new_channel.name}` has been created!")

@bot.command()
async def close_ticket(ctx):
    guild = ctx.guild
    member = ctx.author
    nickname = member.nick if member.nick else member.name   
    channel = discord.utils.get(guild.channels, name=nickname.lower()+"_ticket") 
    CHANNEL_ID = channel.id
    a = bot.get_channel(CHANNEL_ID)
    if a:
        await a.delete()
    else:
        await ctx.send(f"Channel `{channel}` not found.")


class MyView(View):
    def __init__(self):
        super().__init__()

        # Create a button
        button = Button(label="Create ticket!", style=discord.ButtonStyle.green)

        # Set the button callback
        async def button_callback(interaction: discord.Interaction):
           await ticket(interaction)

        button.callback = button_callback
        self.add_item(button)

 


openai.api_key = OPENAI_API_KEY


# Funkcja generowania odpowiedzi przez ChatGPT
def odpowiedz_chatgpt(tresc):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        store=True,
        messages=[{
            "role": "developer",
            "content": "Pisz po polsku. udawaj ze jestes botem na discordzie pisz po polsku"
        },
            {"role": "user", "content": tresc}]
       )
    return response["choices"][0]["message"]["content"]


@bot.command()
async def pomoc(ctx, *, tresc):
    await ctx.send(f"Generowanie odpowiedzi Ai...")
    odpowiedz = odpowiedz_chatgpt(tresc)
    await ctx.send(f"{ctx.author.mention}, Odpowiedź od AI: {odpowiedz}")

@bot.command()
async def pomoc_admina(ctx):
    await ctx.send(f"Wiadomosc do admina zostala wyslan i zaraz odpowied na twoje wezwanie prosimy o cierpliwosc.")


bot.run("api_key")  
 