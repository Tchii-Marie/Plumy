import requests
from discord.ext import commands

class CorrecteurTexte(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def corriger(self, texte, langue="fr"):
        url = "https://api.languagetool.org/v2/check"
        payload = {
            "text": texte,
            "language": langue
        }

        try:
            r = requests.post(url, data=payload)
            if r.status_code != 200:
                return [f"⚠️ Erreur HTTP ({r.status_code}) lors de la correction."]
            result = r.json()
            matches = result.get("matches", [])
            suggestions = []

            for match in matches[:5]:  # Limite à 5 suggestions pour éviter la surcharge
                extrait = match["context"]["text"]
                offset = match["context"]["offset"]
                length = match["context"]["length"]
                mot = extrait[offset:offset+length]
                message = match.get("message", "Suggestion")
                remplacement = match["replacements"][0]["value"] if match["replacements"] else "?"

                suggestions.append(f"🔧 `{mot}` → **{remplacement}** ({message})")

            if not suggestions:
                return ["✅ Aucun problème détecté dans le texte."]
            return suggestions

        except Exception as e:
            return [f"⚠️ Erreur inattendue : {str(e)}"]

    @commands.command(name="corrige")
    async def corrige_texte(self, ctx, *, texte: str):
        await ctx.send("🔍 Analyse grammaticale en cours...")
        corrections = self.corriger(texte)
        for ligne in corrections:
            await ctx.send(ligne)

async def setup(bot):
    await bot.add_cog(CorrecteurTexte(bot))
