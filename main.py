import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv
from keep_alive import keep_alive

# Charger les variables d'environnement (.env)
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents pour activer la lecture du contenu des messages
intents = discord.Intents.default()
intents.message_content = True

# Initialisation du bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Événement : prêt
@bot.event
async def on_ready():
    print(f"🟢 Plumy est connecté en tant que {bot.user}")

# Fonction principale pour charger les extensions puis démarrer le bot
async def main():
    keep_alive()  # 🔄 Lancer dès le début
    print("✅ Serveur keep_alive lancé")
  
    extensions = [
    "cogs.fiche", "cogs.roman", "cogs.univers", "cogs.acte", "cogs.scene",
    "cogs.titre", "cogs.pourquoi", "cogs.atelier", "cogs.generateur_nom",
    "cogs.generateur_intrigue", "cogs.generateur_personnages", "cogs.generateur_lieux",
    "cogs.generateur_objets", "cogs.generateur_univers", "cogs.generateur_ides",
    "cogs.generateur_deblocage", "cogs.generateur_pitch", "cogs.generateur_declencheurs",
    "cogs.generateur_miniscene_interactif", "cogs.datamuse_recherche",
    "cogs.menu_plumy", "cogs.correction"
    ]
  for ext in extensions:
        try:
            if ext in bot.extensions:
                await bot.reload_extension(ext)
            else:
                await bot.load_extension(ext)
            print(f"✅ Extension chargée : {ext}")
        except Exception as e:
            print(f"❌ Erreur lors du chargement de {ext} : {e}")

    print("TOKEN chargé :", TOKEN)
    await bot.start(TOKEN)

# Lancer le bot
asyncio.run(main())
