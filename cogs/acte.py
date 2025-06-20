from discord.ext import commands
import discord
import asyncio

class Scene(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def acte(self, ctx):
        questions = [
            "1️⃣ Quelle est la **situation initiale** de ton histoire ? (où, qui, quoi)",
            "2️⃣ Quel est **l’élément déclencheur** qui fait tout basculer ?",
            "3️⃣ Quels sont les **obstacles, péripéties ou retournements** rencontrés ?",
            "4️⃣ Décris le **climax**, le moment de tension ou de bascule final.",
            "5️⃣ Quelle est **la fin de l’histoire** ? (dénouement, conséquences)"
        ]

        await ctx.send("🎬 Détaillons ton acte narratif ! Réponds à chaque question une par une.")

        reponses = []
        def check(m): return m.author == ctx.author and m.channel == ctx.channel

        for q in questions:
            await ctx.send(q)
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=180)
                reponses.append(msg.content)
            except asyncio.TimeoutError:
                await ctx.send("⏰ Temps écoulé. Tu peux relancer avec `!acte` quand tu veux.")
                return

        nom_fichier = f"acte_{ctx.author.name}.txt"
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(f"Structure narrative créée par {ctx.author.display_name}\n\n")
            for i in range(len(questions)):
                f.write(f"{questions[i]}\n{reponses[i]}\n\n")

        await ctx.send("✅ Acte terminé ! Voici ton fichier : ", file=discord.File(nom_fichier))

async def setup(bot):
    await bot.add_cog(Scene(bot))
