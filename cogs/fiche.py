from discord.ext import commands
import discord
import asyncio

class Fiche(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fiche(self, ctx):
        questions = [
            "1️⃣ *Quel est le nom, le sexe et l’âge du personnage ?*",
            "2️⃣ *Décris son apparence (cheveux, yeux, taille, allure...)*",
            "3️⃣ *Quels sont sa personnalité, ses qualités, ses défauts ?*",
            "4️⃣ *Comment interagit-il/elle avec les autres ? (relations)*",
            "5️⃣ *Quel est son objectif personnel ou secret ?*",
            "6️⃣ *Quels sont les enjeux ou conséquences de cet objectif ?*",
            "7️⃣ *Quelles sont ses forces et faiblesses ?*",
            "8️⃣ *Autres éléments ? (talents, peurs, particularités...)*",
            "9️⃣ *Quel est son passé ou l’événement marquant de sa vie ?*",
            "🔮 *Comment pourrait-il/elle évoluer dans l’histoire ?*"
        ]

        await ctx.send("🎭 Créons la fiche de ton personnage. Réponds à chaque question une par une.")

        reponses = []
        def check(m): return m.author == ctx.author and m.channel == ctx.channel

        for q in questions:
            await ctx.send(q)
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=180)
                reponses.append(msg.content)
            except asyncio.TimeoutError:
                await ctx.send("⏰ Temps écoulé. Tu peux relancer la commande avec `!fiche`.")
                return

        nom_fichier = f"fiche_personnage_{ctx.author.name}.txt"
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(f"Fiche Personnage de {ctx.author.display_name}\n\n")
            for i in range(len(questions)):
                f.write(f"{questions[i]}\n{reponses[i]}\n\n")

        await ctx.send("✅ Fiche terminée ! Voici le fichier à télécharger :", file=discord.File(nom_fichier))

async def setup(bot):
    await bot.add_cog(Fiche(bot))
