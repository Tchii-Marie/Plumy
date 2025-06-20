from discord.ext import commands
import discord
import asyncio

class Univers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def univers(self, ctx):
        questions = [
            "1️⃣ Quel est le **nom de ton monde** ?",
            "2️⃣ *Comment pourrais-tu le décrire en quelques lignes ?* (ambiance, époque, inspiration...)",
            "3️⃣ *Quel est le type d’univers ?* (monde médiéval, dystopie, royaume céleste, dimension parallèle...)",

            "4️⃣ *Quelle est la géographie du monde ?* (climat, relief, biomes, océans...)",
            "5️⃣ *Quelle faune et flore y trouve-t-on ?*",
            "6️⃣ *Existe-t-il des créatures fantastiques ou inventées dans cet univers ?*",

            "7️⃣ *Y a-t-il un système de magie ou de technologies spéciales ?* (formes, limites, rareté...)",

            "8️⃣ *Qui peuple ce monde ?* (races, espèces, civilisations...)",
            "9️⃣ *Comment sont organisés les lieux de vie ?* (villes, habitations, défenses...)",
            "🔟 *Quelles sont les structures sociales ?* (famille, gouvernements, systèmes de santé, culture...)",

            "1️⃣1️⃣ *Comment fonctionne la société ?* (classes sociales, lois, conflits, commerce...)",

            "1️⃣2️⃣ *Y a-t-il une ou plusieurs religions ou croyances ?* (valeurs, rites, créateurs...)",
            "1️⃣3️⃣ *Existe-t-il un ou plusieurs langages ?* Et un calendrier ou des unités de temps particulières ?",

            "1️⃣4️⃣ *Quels événements historiques importants ont marqué ce monde ?* (guerres, révolutions, exodes...)",

            "1️⃣5️⃣ *Existe-t-il des tensions actuelles ou des mystères non résolus dans cet univers ?*",
            "1️⃣6️⃣ *Y a-t-il des règles particulières, interdites, lois universelles ou tabous ?*",

            "1️⃣7️⃣ *Quelle est la place des arts, des sciences, de la nature ou du sacré ?*",

            "1️⃣8️⃣ *Comment s'organisent les déplacements dans le monde ?* (navires, portails, montures, magie...)",

            "1️⃣9️⃣ *Ajoute tout autre détail ou idée libre que tu veux intégrer à ton monde !*"
        ]


        await ctx.send("🌐 Plumy t’invite à créer un monde inédit. Réponds à chaque question une par une :")

        reponses = []
        def check(m): return m.author == ctx.author and m.channel == ctx.channel

        for q in questions:
            await ctx.send(q)
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=300)
                reponses.append(msg.content)
            except asyncio.TimeoutError:
                await ctx.send("⏰ Temps écoulé. Tu peux relancer `!univers` quand tu es prêt(e).")
                return

        nom_fichier = f"univers_{ctx.author.name}.txt"
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(f"🌍 Univers imaginé par {ctx.author.display_name}\n\n")
            for i in range(len(questions)):
                f.write(f"{questions[i]}\n{reponses[i]}\n\n")

        await ctx.send("📁 Univers enregistré avec succès ! Voici ton fichier :", file=discord.File(nom_fichier))

async def setup(bot):
    await bot.add_cog(Univers(bot))
