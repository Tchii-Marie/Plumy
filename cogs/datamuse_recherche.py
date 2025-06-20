import requests
from discord.ext import commands

class DatamuseRecherche(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def chercher_mots(self, mot, relation, max_results=10):
        url = f"https://api.datamuse.com/words?{relation}={mot}&max={max_results}"
        r = requests.get(url)
        if r.status_code == 200:
            return [entry["word"] for entry in r.json()]
        return ["(aucun résultat trouvé)"]

    @commands.command()
    async def synonyme(self, ctx, *, mot):
        mots = self.chercher_mots(mot, "rel_syn")
        await ctx.send(f"🔄 **Synonymes de _{mot}_** : {', '.join(mots)}")

    @commands.command()
    async def rime(self, ctx, *, mot):
        mots = self.chercher_mots(mot, "rel_rhy")
        await ctx.send(f"🎵 **Rimes avec _{mot}_** : {', '.join(mots)}")

    @commands.command()
    async def associe(self, ctx, *, mot):
        mots = self.chercher_mots(mot, "rel_trg")
        await ctx.send(f"🧠 **Mots associés à _{mot}_** : {', '.join(mots)}")

    @commands.command()
    async def adjectif(self, ctx, *, mot):
        mots = self.chercher_mots(mot, "rel_jjb")
        await ctx.send(f"🎨 **Adjectifs pour _{mot}_** : {', '.join(mots)}")

    @commands.command()
    async def antonyme(self, ctx, *, mot):
        mots = self.chercher_mots(mot, "rel_ant")
        await ctx.send(f"🔁 **Contraires de _{mot}_** : {', '.join(mots)}")

async def setup(bot):
    await bot.add_cog(DatamuseRecherche(bot))
