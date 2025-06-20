import random
import asyncio
from discord.ext import commands

class GenerateurDeblocage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def debloque(self, ctx):
        questions = [
            "Quel est le dernier choix difficile qu’a fait ton personnage ?",
            "Quel secret ton monde cache-t-il encore au lecteur… ou à toi-même ?",
            "Quelle émotion ton personnage refuse-t-il d’affronter ?",
            "Qu’as-tu laissé en suspens entre deux personnages ?",
            "Que s’est-il passé juste avant la scène que tu n’arrives pas à écrire ?",
            "Que pourrait-il arriver si quelqu’un faisait le mauvais choix maintenant ?",
            "Qu’est-ce que tu ne veux pas admettre sur l’intrigue que tu écris ?"
        ]

        question = random.choice(questions)
        auteur = ctx.author

        await ctx.send(f"✨ **Débloquons ton histoire, {auteur.display_name}**\n{question}\n\n📝 Réponds dans ce salon, je t’écoute...")

        def check(m):
            return m.author == auteur and m.channel == ctx.channel

        try:
            réponse = await self.bot.wait_for("message", check=check, timeout=240)  # 4 min
            texte = réponse.content

            mots = [mot.strip(",.?!;:") for mot in texte.split() if len(mot) > 3]
            motcle = random.choice(mots) if mots else "ce qui n’est pas dit"

            rebonds = [
                f"Et si **{motcle}** était au cœur d’un malentendu crucial entre deux personnages ?",
                f"Tu pourrais faire de **{motcle}** un élément déclencheur d’un revirement majeur.",
                f"Peut-être que **{motcle}** contient une vérité que seul un enfant oserait nommer.",
                f"Et si **{motcle}** revenait sous une forme inattendue… ou était un leurre narratif ?",
                f"Et si **{motcle}** n’existait pas réellement, mais façonnait pourtant tout ?"
            ]

            idée = random.choice(rebonds)
            await ctx.send(f"🔓 **Piste narrative proposée** : {idée}")

        except asyncio.TimeoutError:
            await ctx.send("⏳ Je n’ai rien reçu… N’hésite pas à relancer `!debloque` quand tu es prêt·e 😊")

async def setup(bot):
    await bot.add_cog(GenerateurDeblocage(bot))
