from discord.ext import commands

class MenuPlumy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="plumy")
    async def menu_plumy(self, ctx):
        message = (
            "🪶 **Bienvenue dans l’univers de Plumy – Assistant narratif et créatif** 🪶\n\n"
            "**🎭 Création & narration :**\n"
            "`!roman`, `!fiche`, `!scene`, `!acte`, `!pitch`, `!titre`, `!univers`, `!univers_genere`, `!elementdeclencheur`, `!twist`, `!evolutions`\n\n"
            "**🧙 Personnages, objets, lieux :**\n"
            "`!personnage`, `!objet`, `!lieu`, `!nom`\n\n"
            "**💡 Inspiration & déblocage :**\n"
            "`!idee`, `!debloque`, `!blocage`, `!catalyseur_idee`, `!defi`, `!pourquoi`, `!miniscene`, `!sprint`\n\n"
            "**🛠️ Langage & lexique (FR/EN) :**\n"
            "`!corrige`, `!synonyme` (EN), `!rime` (EN), `!associe`, `!adjectif`, `!antonyme` (EN)\n\n"
            "_✨ Tape `!plumy` à tout moment pour afficher ce menu._\n"
            "_Plumy adore quand tu l’appelles pour t’inspirer ! 💫🖋️_"
        )
        await ctx.send(message)


async def setup(bot):
    await bot.add_cog(MenuPlumy(bot))
