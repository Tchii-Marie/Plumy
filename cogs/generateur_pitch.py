import asyncio
from discord.ext import commands

class GenerateurPitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pitch(self, ctx):
        auteur = ctx.author

        await ctx.send(
            f"📘 Salut **{auteur.display_name}**, écrivons ton pitch ensemble !\n"
            f"Je vais te poser 5 questions, réponds dans le salon à chaque fois.\n"
            f"Prêt·e ? On commence 👇"
        )

        questions = [
            "🌍 **1. Contexte** — Où ou quand se déroule ton histoire ?",
            "🎬 **2. Événement déclencheur** — Quel fait déclenche l’action au départ ?",
            "👤 **3. Personnage(s)** — Qui est/sont ton/tes protagoniste(s) ?",
            "⚔️ **4. Obstacle(s)** — Quel est l’enjeu ou le conflit majeur ?",
            "🎯 **5. Objectif** — Que cherche(nt) ton/tes héros à accomplir ?"
        ]

        réponses = []

        def check(m):
            return m.author == auteur and m.channel == ctx.channel

        for question in questions:
            await ctx.send(question)
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=300)
                réponses.append(msg.content.strip())
            except asyncio.TimeoutError:
                await ctx.send("⏳ Temps écoulé. Tu pourras relancer la commande `!pitch` quand tu seras prêt·e.")
                return

        # Assemblage du pitch final
        contexte, declencheur, perso, obstacle, objectif = réponses

        pitch = (
            f"📖 **Pitch généré** :\n"
            f"Dans {contexte}, à la suite de {declencheur}, "
            f"{perso} se bat contre {obstacle} pour atteindre {objectif}."
        )

        await ctx.send("✨ Et voilà ton pitch narratif :")
        await ctx.send(pitch)

async def setup(bot):
    await bot.add_cog(GenerateurPitch(bot))
