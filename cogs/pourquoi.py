from discord.ext import commands
import discord
import asyncio

# Dictionnaire des mots-clés
themes = {
    "émotion": [
        "libérer", "tristesse", "vide", "guérir", "colère", "lâcher", "douleur", "blessure",
        "chagrin", "cicatrice", "soulagement", "pleurer", "rage", "trauma", "mal-être", "solitude", "larmes"
    ],
    "identité": [
        "vérité", "être", "moi", "exister", "authentique", "réel", "propre", "unique", "âme",
        "qui je suis", "nudité", "intérieur", "singularité"
    ],
    "partage": [
        "dire", "transmettre", "aider", "témoigner", "écho", "comprendre", "partager",
        "donner", "écouter", "raconter", "relier", "joindre", "liaison"
    ],
    "blocage": [
        "peur", "doute", "paralyser", "impossible", "bloqué", "perfection", "angoisse", "pression",
        "critique", "raté", "imposteur", "retenir", "blocage", "jugement", "inhibition"
    ],
    "ambition": [
        "briller", "réussir", "visible", "reconnu", "immortel", "trace", "impact", "influencer",
        "notoriété", "fierté", "posterité", "marquer"
    ]
}

conseils = {
    "émotion": "💔 Tu sembles écrire pour te libérer intérieurement. Pose tes émotions sur le papier, sans filtre ni peur. Même le chaos a sa poésie.",
    "identité": "🪞 Tu écris peut-être pour affirmer ce que tu es. Laisse ta voix résonner, elle est précieuse. Ne la maquille pas.",
    "partage": "📣 Tu veux créer du lien, transmettre. Écris comme si quelqu’un t’écoutait au loin — quelqu’un que tu sauves, peut-être.",
    "blocage": "🧱 On sent une tension, une barrière. Écris sans t’interdire, même maladroitement. La beauté naît souvent dans les tremblements.",
    "ambition": "🌟 Tu veux laisser une trace. C’est noble. Ne cours pas après l’impact : construis-le mot après mot, à ton rythme."
}

# État temporaire par auteur
pourquoi_etat = {}

class Pourquoi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pourquoi(self, ctx):
        user_id = ctx.author.id
        pourquoi_etat[user_id] = {"étape": 1, "réponses": []}
        await ctx.send("🧠 **Exploration : Pourquoi j’écris ?**\n\n1️⃣ Pourquoi écris-tu ?")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        state = pourquoi_etat.get(message.author.id)
        if state:
            réponse = message.content.strip().lower()
            state["réponses"].append(réponse)
            étape = state["étape"]

            if étape < 5:
                state["étape"] += 1
                await message.channel.send(f"{étape+1}️⃣ Pourquoi cela est-il important pour toi ?")
            else:
                texte_total = " ".join(state["réponses"])
                scores = {cat: sum(m in texte_total for m in mots) for cat, mots in themes.items()}
                dominant = max(scores, key=lambda cat: scores.get(cat) or 0) if scores else None
                if dominant:
                    conseil = conseils.get(dominant, "✍️ Continue d’écrire. Même si tu doutes, la vérité se révèle toujours par fragments.")
                else:
                    conseil = "✍️ Continue d’écrire. Même si tu doutes, la vérité se révèle toujours par fragments."

                await message.channel.send(f"🧠 **Conseil de Plumy :**\n{conseil}")
                del pourquoi_etat[message.author.id]

async def setup(bot):
    await bot.add_cog(Pourquoi(bot))
