from discord.ext import commands
import discord
import asyncio
import random

class Atelier(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def défi(self, ctx):
        defis = [
            "Écris une scène uniquement avec des dialogues, sans narration.",
            "Décris un lieu à travers les sensations d’un animal.",
            "Écris une lettre que ton personnage n’enverra jamais.",
            "Fais un texte sans utiliser le verbe *être*.",
            "Commence par : « Je n’aurais jamais dû faire ça… »",
            "Invente une scène dans un monde où les émotions sont interdites.",
            "Écris une scène de rupture du point de vue d’un objet.",
            "Décris un souvenir... qui n’a peut-être jamais eu lieu.",
            "Écris à la manière d’un journal intime trouvé dans 1000 ans.",
            "Fais un texte où chaque phrase commence par une conjonction de coordination.",
            "Écris un monologue intérieur d’un personnage qui attend quelqu’un… mais qui ne viendra jamais.",
            "Fais une description sans aucun adjectif.",
            "Écris une scène où le décor est plus important que les personnages.",
            "Fais dialoguer deux éléments naturels (ex : la mer et le vent).",
            "Imagine un monde sans lumière. Écris une scène qui s’y déroule.",
            "Écris la suite d’un conte célèbre, mais en version dystopique.",
            "Crée une recette de cuisine... qui évoque une émotion précise.",
            "Fais parler un mur, une pierre ou un vieux meuble.",
            "Écris un poème en prose qui tourne autour d’un secret.",
            "Transforme une dispute réelle en scène de fantasy ou de science-fiction.",
             "Imagine un monde où le soleil s’éteint lentement. Écris une scène quotidienne dans ce contexte.",
                "Écris un texte sans ponctuation. Ni point ni virgule. Juste le souffle.",
                "Ton personnage découvre une boîte dont il ne faut surtout pas parler. Décris ce qu’il fait.",
                "Tu es un rêve oublié. Raconte ce que tu ressens en disparaissant.",
                "Choisis une couleur inventée et construis un monde autour d’elle.",
                "Écris une histoire d’amour sans utiliser le mot *amour*.",
                "Décris une odeur d’enfance et ce qu’elle déclenche aujourd’hui.",
                "Écris une scène entre un robot et un peintre. Qui comprend le mieux l’humanité ?",
                "Ton texte ne peut contenir que des mots de 4 lettres maximum.",
                "Écris comme si tu écrivais une prière à quelque chose que tu redoutes.",
                "Transforme un SMS banal en poème existentiel.",
                "Ta plume est amnésique. Elle n’a qu’un souvenir flou : écris-le.",
                "Ton personnage ne parle qu’avec des métaphores. Raconte une scène de tension.",
                "Décris une chambre vide… qui raconte une vie entière.",
                "Fais parler un reflet.",
                "Imagine une langue inconnue, mais traduis-la avec émotion.",
                "Tu es une chanson coincée dans la tête de quelqu’un. Que veux-tu lui dire ?",
                "Une pluie tombe, mais elle ne mouille pas. Que provoque-t-elle ?",
                "Écris un conte de fée… sans magie, sans roi, sans dragon.",
                "Raconte une dispute avec ton ombre.",
                "Tu es dans un carnet abandonné dans le métro. Décris ce qu’on découvre en toi.",
                "Crée une déclaration d’amour à un silence.",
                "Écris un texte qui commence joyeux… et ne finit pas.",
                "Invente une cérémonie dans un monde étrange. Qui l’attend ? Pourquoi ?",
                "Tu es un arbre qui se réveille dans un désert.",
                "Écris un monologue intérieur en pleine tempête (réelle ou émotionnelle).",
                "Ton texte ne peut contenir que 3 voyelles différentes.",
                "Écris une page de roman d’un auteur imaginaire… et glisse une note manuscrite dans la marge.",
                "Imagine une carte du monde… d’après les sensations (la colère est un volcan, la tendresse un lac).",
                "Tu écris la dernière page d’un journal intime dont tu ignores tout… sauf la fin."

        ]
        await ctx.send(f"🎯 **Défi d’écriture** : {random.choice(defis)}\nBonne plume ! 🖋️")

    @commands.command()
    async def blocage(self, ctx):
        conseils = [
            "✍️ Écris comme si personne ne te lisait. Vraiment.",
            "📎 Commence par : *Je ne sais pas quoi dire mais j’écris quand même…*",
            "🎭 Mets-toi dans la peau de quelqu’un d’autre pour parler de toi.",
            "🌀 Décris une sensation, pas une pensée.",
            "🧠 Ton brouillon n’a pas à être joli. Il doit juste *exister*.",
            "💬 Parle à haute voix en écrivant, même si tu bafouilles.",
            "🚪Ferme les yeux 10 secondes, puis écris ce qui te vient sans t’arrêter pendant 3 minutes.",
            "🧩 Écris sur *pourquoi tu n’arrives pas à écrire*."
        ]
        await ctx.send(f"🧱 **Conseil anti-blocage** :\n{random.choice(conseils)}")

    @commands.command()
    async def sprint(self, ctx, durée: int = 5):
        if durée <= 0 or durée > 60:
            await ctx.send("⏰ Donne une durée entre 1 et 60 minutes. Exemple : `!sprint 10`")
            return

        secondes = durée * 60
        await ctx.send(f"🔥 **Sprint d’écriture** lancé pour {durée} minutes !\nMets ta musique, ton thé, et c’est parti ✍️")

        await asyncio.sleep(secondes)

        await ctx.send("🛎️ **Temps écoulé !** Tu peux faire une pause, ou relire ce que tu viens de créer 💚")

async def setup(bot):
    await bot.add_cog(Atelier(bot))
