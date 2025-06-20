import random
import asyncio
from discord.ext import commands

class GenerateurMiniScene(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def miniscene(self, ctx):
        auteur = ctx.author

        await ctx.send(
            f"🎭 **Atelier express de micro-scène !**\n"
            f"Salut {auteur.display_name}, je vais te poser 3 questions rapides :\n"
            f"1️⃣ Le personnage\n2️⃣ Le lieu\n3️⃣ Le ton désiré\n\nRéponds dans le salon à chaque étape 💬"
        )

        questions = [
            "🧍 **Quel est le nom ou le rôle de ton personnage ?**",
            "📍 **Dans quel lieu ou décor se déroule la scène ?**",
            "🎭 **Quel ton ou quelle atmosphère veux-tu (ex : onirique, sombre, comique, absurde, poétique) ?**"
        ]

        réponses = []

        def check(m):
            return m.author == auteur and m.channel == ctx.channel

        for question in questions:
            await ctx.send(question)
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=240)
                réponses.append(msg.content.strip())
            except asyncio.TimeoutError:
                await ctx.send("⏳ Temps écoulé. Recommence avec `!miniscene` quand tu veux !")
                return

        personnage, lieu, ton = réponses

        objectifs = [
            "retrouver ce qu’iel a perdu sans savoir ce que c’est",
            "comprendre la signification d’un souvenir qui n’est peut-être pas le sien",
            "affronter une peur qu’iel n’a jamais nommée",
            "écouter un message qu’iel a refusé trop longtemps",
            "sauver quelque chose d’oublié avant qu’il ne disparaisse pour de bon",
            "retrouver un lien oublié entre deux mondes",
            "racheter une faute qu’iel n’a pas commise personnellement",
            "donner un sens à un symbole qu’iel voit partout sans le comprendre",
            "conserver un instant avant qu’il ne s’efface définitivement",
            "empêcher la répétition d’un événement dont personne ne garde le souvenir",
            "trouver un endroit qui ne figure sur aucune carte mais qui le/la hante",
            "comprendre pourquoi le silence est devenu total entre certain·es personnages",
            "recoller les morceaux d’un rêve que d’autres refusent de reconnaître"
        ]

        obstacles = [
            "un souvenir vivant", "une absence trop lourde", "un murmure qu’iel est seul·e à entendre",
            "une faille dans la réalité", "quelqu’un qui prétend tout connaître de son passé",
            "un lieu qui refuse de s’ouvrir", "une pluie qui n’existe pas",
            "une vérité trop instable pour être regardée en face",
            "un animal qui suit le personnage sans jamais se laisser approcher",
            "un personnage qu’iel connaît mais qui ne semble pas le/la reconnaître",
            "une boucle temporelle à peine perceptible",
            "la perte progressive du langage dans ce lieu",
            "une pluie de cendres qui éteint toute mémoire fraîche",
            "un reflet qui ne suit plus ses gestes",
            "une voix étrangère dans ses pensées… familière pourtant"
        ]

        objectif = random.choice(objectifs)
        obstacle = random.choice(obstacles)

        paragraphe = (
            f"🪶 **Mini-scène générée** :\n\n"
            f"{personnage} se trouve dans {lieu}. "
            f"Iel est confronté·e à {obstacle} alors qu’iel tente de {objectif}. "
            f"La scène s’inscrit dans un registre {ton}, laissant place à l’imprévu ou à l’introspection selon l’interprétation."
        )

        await ctx.send(paragraphe)

async def setup(bot):
    await bot.add_cog(GenerateurMiniScene(bot))
