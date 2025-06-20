import random
from discord.ext import commands

class GenerateurLieu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lieu(self, ctx):
        types_lieux = [
            "un monastère abandonné",
            "une forêt pétrifiée",
            "une station orbitale en ruine",
            "un village enseveli sous la cendre",
            "une bibliothèque souterraine oubliée",
            "une auberge perchée dans un arbre géant",
            "un marché flottant au-dessus d’un marais",
            "une caverne sculptée par des chants anciens",
            "un temple englouti aux murs luminescents",
            "un laboratoire désert suspendu dans le vide",
            "une ville en spirale bâtie à flanc de falaise",
            "une tour inversée creusée dans la terre",
            "un amphithéâtre désert où résonnent encore les voix",
            "un phare noyé dans une mer de sable",
            "un jardin minéral figé dans le temps",
            "une île mouvante perdue entre les dimensions",
            "un cimetière d’aéronefs recouvert de mousses",
            "une passerelle infinie suspendue au-dessus du vide",
            "un ancien palais reconquis par la végétation",
            "un théâtre bâti dans une carcasse de dragon fossile",
            "un campement nomade sur le dos d’une créature géante",
            "un réseau de tunnels chantants sous une cité oubliée",
            "une horloge colossale dont chaque engrenage contient une pièce",
            "une arche de pierre flottant dans un ciel nocturne figé"
        ]


        elements_remarquables = [
            "où le temps semble ralentir",
            "dont les murs suintent une lumière verte",
            "protégé par un golem endormi",
            "où chaque bruit semble être une voix",
            "tapissé de symboles mouvants",
            "où des illusions prennent vie à la tombée du jour",
            "rempli d’échos d’une langue oubliée",
            "où il neige même en plein été",
            "alimenté par un cœur mécanique encore battant",
            "où l’eau coule vers le ciel",
            "où les ombres ne suivent pas les mouvements",
            "dont le sol est recouvert d’écailles d’or",
            "où les miroirs reflètent un monde parallèle",
            "abritant un arbre qui murmure les noms des visiteurs",
            "où toute technologie cesse de fonctionner",
            "à l’intérieur duquel règne une gravité inversée",
            "constamment éclairé par une lune invisible",
            "envahi par des papillons de verre incassables",
            "dont les portes ne s’ouvrent qu’en chantant",
            "où le silence devient assourdissant",
            "hanté par les rêves de ceux qui y dorment",
            "dont les murs se déplacent la nuit",
            "où l'air sent le souvenir de l’enfance",
            "où les statues changent de position à chaque regard",
            "où résonne une mélodie que personne n'a jamais composéé"
        ]

        ambiances = [
            "calme et inquiétante",
            "oppressante mais fascinante",
            "étrangement chaleureuse",
            "baignée d’une nostalgie irréelle",
            "déformée par un passé inaccessible",
            "emplie de murmures lointains",
            "silencieuse comme un monde figé",
            "saturée d’énergie inconnue",
            "tristement belle comme une ruine sacrée",
            "troublante comme un rêve lucide",
            "tendue comme avant une tempête",
            "habitée d’une grâce surnaturelle",
            "froide et indifférente au vivant",
            "palpitante comme un cœur ancien",
            "électrisante malgré l’immobilité",
            "poudrée d’un silence irréel",
            "désorientante comme un mirage mouvant",
            "hantée par des souvenirs oubliés",
            "lumineuse sans source visible",
            "fragile comme une illusion sur le point de disparaître",
            "écrasante comme le poids d’un secret trop vieux",
            "altérée comme un souvenir mal reconstruit",
            "solennelle, comme un lieu sacré sans divinité",
            "suspendue hors du temps et du bruit",
            "vivante, mais d’une vie étrangère à toute logique"
        ]


        description = f"📍 **Lieu généré** : {random.choice(types_lieux)}, {random.choice(elements_remarquables)}, dans une ambiance {random.choice(ambiances)}."

        await ctx.send(description)

async def setup(bot):
    await bot.add_cog(GenerateurLieu(bot))
