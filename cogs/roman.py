from discord.ext import commands
import discord
import asyncio

class Roman(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roman(self, ctx):
        questions = [
            "1️⃣ Quel est le **titre** de ton roman ?",
            "2️⃣ Quel est le **genre littéraire** ?",
            "3️⃣ Quelle est l **ambiance générale** ? (mystérieuse, légère, dramatique...)", 
            "4️⃣ Qui sont les **personnages principaux** ou idées de personnages ?", 
            "5️⃣ Le roman se passe-t-il dans un **univers réel ou inventé** ?", 
            "6️⃣ Écris un **pitch rapide** (résumé en quelques lignes)."
        ]

        await ctx.send("📖 Créons ta fiche projet roman. Tu peux répondre à chaque question une par une.")

        reponses = []
        def check(m): return m.author == ctx.author and m.channel == ctx.channel

        for q in questions:
            await ctx.send(q)
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=180)
                reponses.append(msg.content)
            except asyncio.TimeoutError:
                await ctx.send("⏰ Temps écoulé. Tu peux relancer la commande avec `!roman`.")
                return

        nom_fichier = f"projet_roman_{ctx.author.name}.txt"
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(f"Projet Roman de {ctx.author.display_name}\n\n")
            for i in range(len(questions)):
                f.write(f"{questions[i]}\n{reponses[i]}\n\n")

        await ctx.send("✅ Fiche complétée ! Voici ton fichier 📎 :", file=discord.File(nom_fichier))

async def setup(bot):
    await bot.add_cog(Roman(bot))