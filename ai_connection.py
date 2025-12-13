import discord
from discord.ext import commands
import openai

# Ustawienia bota
TOKEN = "TOKEN"
OPENAI_API_KEY = "API_KEY"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

# Inicjalizacja OpenAI
openai.api_key = OPENAI_API_KEY

openai.ChatCompletion.create(
    model="gpt-4o-mini",
    store=True,
    messages=[{"role": "user", "content": "udawaj ze jestes botem na discordzie pisz po polsku "}]
)


# Funkcja generowania odpowiedzi przez ChatGPT
def odpowiedz_chatgpt(tresc):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        store=True,
        messages=[{"role": "user", "content": tresc}]
       )
    return response["choices"][0]["message"]["content"]


@bot.command()
async def pomoc(ctx, *, tresc):
    odpowiedz = odpowiedz_chatgpt(tresc)
    await ctx.send(f"{ctx.author.mention}, Odpowiedź od AI: {odpowiedz}")

   # Uruchomienie bota
bot.run(TOKEN)
