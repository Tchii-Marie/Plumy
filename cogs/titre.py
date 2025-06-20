from discord.ext import commands
import discord
import asyncio

class Titre(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def titre(self, ctx):
        questions = [
            "1️⃣ Donne-moi un mot ou une idée forte au cœur de ton histoire (ex: exil, vengeance, oubli…)",
            "2️⃣ Quel est le **ton ou l'ambiance principale** ? (épique, poétique, sombre, ironique…)",
            "3️⃣ Quel est le **genre de ton récit** ? (fantasy, SF, historique, romance, thriller…)"
        ]

        await ctx.send("🖋️ Trouvons ensemble un titre puissant pour ton histoire. Réponds à ces 3 questions :")

        reponses = []
        def check(m): return m.author == ctx.author and m.channel == ctx.channel

        for q in questions:
            await ctx.send(q)
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=180)
                reponses.append(msg.content.strip())
            except asyncio.TimeoutError:
                await ctx.send("⏰ Temps écoulé. Tu peux relancer la commande avec `!titre`.")
                return

        idee_centrale, ambiance, genre = reponses

        # Génération de titres (simple inspiration textuelle basée sur les réponses)
        propositions = [
            f"• *{idee_centrale.capitalize()} {('éternelle' if ambiance == 'poétique' else 'perdue')}*",
            f"• *Le {idee_centrale.lower()} des {genre.lower()}*",
            f"• *Sous une ombre {ambiance.lower()}*",
            f"• *Chroniques de {idee_centrale.lower()}*",
            f"• *En terres {ambiance.lower()}s*",
            f"• *Mémoire(s) de {idee_centrale.lower()}*",
            f"• *{idee_centrale.capitalize()} parmi les ruines*",
            f"• *À l’orée du {idee_centrale.lower()}*",
            f"• *Quand {idee_centrale.lower()} rencontre l’oubli*",
            f"• *L’héritage {ambiance.lower()}*",
            f"• *L’enfant de {idee_centrale.lower()}*",
            f"• *La dernière {idee_centrale.lower()}*",
            f"• *Ceux qui portaient le {idee_centrale.lower()}*",
            f"• *Derrière le voile {ambiance.lower()}*",
            f"• *Dans l’ombre du {genre.lower()}*",
            f"• *{idee_centrale.capitalize()} dans le sang*",
            f"• *Les vents de {ambiance.lower()}*",
            f"• *Par-delà le {idee_centrale.lower()}*"
        ]

        await ctx.send("🎇 Voici quelques idées de titre que Plumy te souffle :\n" + "\n".join(propositions))

async def setup(bot):
    await bot.add_cog(Titre(bot))
