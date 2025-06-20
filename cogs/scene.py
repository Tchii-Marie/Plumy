from discord.ext import commands
import discord
import asyncio

class SceneAssistant(commands.Cog):  # nouveau nom unique
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def scene(self, ctx):
        
        questions = [
            "1️⃣ Quel est le **but de la scène** ? (informer, choquer, émouvoir, faire avancer l'intrigue…)",
            "2️⃣ Qui est présent dans la scène et **que veulent-ils** ?",
            "3️⃣ Quels **obstacles** ou résistances vont apparaître (internes ou externes) ?",
            "4️⃣ Où et quand se déroule cette scène ? **Décor, ambiance, heure du jour...**",
            "5️⃣ Quelle est la **tension émotionnelle** principale ? (colère, espoir, peur…)",
            "6️⃣ Quelle **action ou interaction clé** s'y déroule (révélation, confrontation, décision…) ?",
            "7️⃣ Que découvre-t-on sur un **personnage, une relation, ou l’univers** ?",
            "8️⃣ Quels sont les **éléments sensoriels** à inclure ? (sons, lumières, odeurs, détails visuels)",
            "9️⃣ Quelle est la **forme de narration** choisie ? (dialogue, flashback, narration interne…)",
            "🔟 Comment cette scène **fait-elle avancer l’histoire** ou prépare-t-elle la suivante ?",
            "1️⃣1️⃣ Y a-t-il un **changement de dynamique** entre les personnages ou dans la situation ?",
            "1️⃣2️⃣ Quels sont les **non-dits**, les sous-entendus, ou les tensions invisibles ?",
            "1️⃣3️⃣ Que ressent le lecteur/spectateur à la fin de la scène ?"
        ]

        await ctx.send("🎬 Plumy t’aide à écrire une scène vivante. Réponds à chaque question une par une :")

        reponses = []
        def check(m): return m.author == ctx.author and m.channel == ctx.channel

        for q in questions:
            await ctx.send(q)
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=300)
                reponses.append(msg.content)
            except asyncio.TimeoutError:
                await ctx.send("⏰ Temps écoulé. Tu peux relancer avec `!scene` quand tu veux.")
                return

        nom_fichier = f"scene_{ctx.author.name}.txt"
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(f"🎬 Scène rédigée par {ctx.author.display_name}\n\n")
            for i in range(len(questions)):
                f.write(f"{questions[i]}\n{reponses[i]}\n\n")

        await ctx.send("✅ Scène enregistrée avec succès 📁 :", file=discord.File(nom_fichier))

async def setup(bot):
    await bot.add_cog(SceneAssistant(bot))

