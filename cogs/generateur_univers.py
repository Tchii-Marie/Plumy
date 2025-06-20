import random
from discord.ext import commands

class GenerateurUnivers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="univers_genere")
    async def univers(self, ctx, *, genre: str = "fantasy"):
        univers_data = {
            "fantasy": [
                {
                    "peuple": "les Nalvorins, êtres ailés liés à la magie des vents",
                    "géographie": "des archipels flottants autour d’un cyclone immobile",
                    "société": "théocratie élémentaire régie par des prêtres orageux",
                    "lieu": "l’Atrium de l’Aube, sanctuaire suspendu entre deux nuages vivants"
                },
                {
                    "peuple": "les Trogmir, forgerons de pierre aux veines incandescentes",
                    "géographie": "un gouffre volcanique aux galeries cristallines",
                    "société": "clans méritocratiques fondés sur l’artisanat rituel",
                    "lieu": "la Forge des Cendres Hurlantes, cœur vivant de leur cité"
                },
                {
                    "peuple": "les Myrmanthes, amphibiens sacrés aux chants thérapeutiques",
                    "géographie": "un marécage phosphorescent régi par les cycles lunaires",
                    "société": "conseil tribal guidé par des oracles amphibies",
                    "lieu": "la Salle Miroitante, temple immergé où les souvenirs nagent"
                },
                {
                    "peuple": "les Sylvoris, nomades végétaux enracinés dans les vents",
                    "géographie": "forêts flottantes en migration perpétuelle",
                    "société": "communautés cycliques liées par des rythmes saisonniers",
                    "lieu": "le Cœur Chlorophyllien, sanctuaire harmonique des flux naturels"
                },
                {
                    "peuple": "les Cœurlames, moines-poètes qui sculptent la réalité en vers",
                    "géographie": "des montagnes d’encre dure où poussent des mots sauvages",
                    "société": "ordre mystique centré sur la poésie rituelle",
                    "lieu": "le Scriptorial Sacré, bibliothèque vivante aux murs de mémoire"
                },
                {
                    "peuple": "les Aelthyns, nés des souvenirs oubliés des forêts",
                    "géographie": "des clairières-labyrinthes où le temps est circulaire",
                    "société": "confrérie d’historiens-mages liés aux cycles lunaires",
                    "lieu": "la Roseraie Mnémonique, jardin de mémoire vivante"
                },
                {
                    "peuple": "les Ombrians, humanoïdes tissés dans les rêves d’autrui",
                    "géographie": "un continent flottant entre le réel et l’illusion",
                    "société": "hiérarchie onirique où chaque caste rêve une autre",
                    "lieu": "le Palais du Vœu Retourné, forteresse des songes trahis"
                },
                {
                    "peuple": "les Sylphydes cendrés, élémentaires créés par le souffle d’un volcan",
                    "géographie": "des cratères musicaux éparpillés dans une mer pétrifiée",
                    "société": "guilde de souffleurs de feu et d’oracles cendres-fleuries",
                    "lieu": "le Grand Chœur de l’Éruption Première"
                }
            ],
            "science-fiction": [
                {
                    "peuple": "les Argéons, humains augmentés aux esprits interconnectés",
                    "géographie": "une station orbitale fractale autour d’un pulsar instable",
                    "société": "conscience collective répartie entre plusieurs noyaux quantiques",
                    "lieu": "la Sphère Mentale X’hel, nexus des flux de pensée"
                },
                {
                    "peuple": "les Anemoïdes, êtres gazeux migrateurs nés dans les nébuleuses",
                    "géographie": "un océan de nuages intelligents sillonné par des vaisseaux-créatures",
                    "société": "réseau anarchique d’alliances organiques",
                    "lieu": "le Ventre de la Brume, refuge flottant au sein du cyclone stellaire"
                },
                {
                    "peuple": "les Valari, civilisations reptiliennes aux pensées fractales",
                    "géographie": "anneaux artificiels orbitant autour d’un trou noir tempéré",
                    "société": "oligarchie scientifique où toute croyance est une donnée",
                    "lieu": "le Dôme Hypéron, laboratoire ancestral suspendu dans la courbure"
                },
                {
                    "peuple": "les Synthéastes, entités hybrides IA-artistes en quête d’émotion pure",
                    "géographie": "un réseau stellaire de dômes-sonores vibrants",
                    "société": "collectif esthétique basé sur le partage d’états sensoriels",
                    "lieu": "la Galerie Aveugle, espace où la lumière est traduite en musique"
                },
                {
                    "peuple": "les Anarchoïdes, descendants des robots démantelés",
                    "géographie": "un astéroïde creux envahi de jungle métallique",
                    "société": "clans tribaux reconstruits sur les valeurs de bug sacré",
                    "lieu": "la Fosse aux Fils, cathédrale faite de câbles et de débris"
                },
                {
                    "peuple": "les Chronoïdes, êtres dont les consciences se déploient sur plusieurs époques simultanément",
                    "géographie": "un anneau orbital fissuré qui entoure une étoile mourante",
                    "société": "synarchie temporelle où l’avenir influence les lois du présent",
                    "lieu": "le Temple des Instants Croisés, structure où convergent les probabilités"
                },
                {
                    "peuple": "les Périplégiens, vagabonds cosmiques nés d’exils biologiques",
                    "géographie": "une flotte de vaisseaux organiques dérivant entre deux galaxies mortes",
                    "société": "nomadisme stratifié selon la mémoire ancestrale embarquée",
                    "lieu": "le Théâtre Suspendu, coque-monde où les récits maintiennent l’identité collective"
                },
                {
                    "peuple": "les Flétryliens, intelligences liquides migrantes entre planètes océaniques",
                    "géographie": "un archipel de lunes océanides partiellement terraformées",
                    "société": "hologouvernance fluide où chaque décision doit être chantée",
                    "lieu": "le Conservatoire de la Vague Mère, réservoir de mémoire liquide"
                },
                {
                    "peuple": "les Klüvrates, cyborganismes qui échappent à la causalité physique",
                    "géographie": "un tore quantique instable suspendu dans un champ d’antigravité inversée",
                    "société": "clergé post-physique basé sur des paradoxes validés par l’expérience",
                    "lieu": "la Cathédrale Boucle, sanctuaire fractal qui réécrit ses murs"
                },
                {
                    "peuple": "les Fulgurants, survivants d'une guerre-lumière réfugiés dans la conscience des comètes",
                    "géographie": "un nuage stellaire instable traversé par d’anti-éclairs mémétiques",
                    "société": "culture d’isolement guidée par des oracles-lumières binaires",
                    "lieu": "la Nacelle Fantôme, ancienne station prison devenant foyer culturel"
}
            ],
            "dystopique": [
                {
                    "peuple": "les Ultimes, survivants modifiés après l’effondrement génétique",
                    "géographie": "une mégacité verticale construite sur les ruines englouties du monde",
                    "société": "hiérarchie biotechnologique dirigée par un algorithme sacré",
                    "lieu": "la Crypte Blanche, zone interdite d'où jaillissent les rêves modifiés"
                },
                {
                    "peuple": "les Chrones, humains privés de mémoire à chaque génération",
                    "géographie": "des déserts de miroirs dans un monde déphasé",
                    "société": "système de castes basé sur la reconstruction des souvenirs",
                    "lieu": "la Tour du Cycle, centre d’archivage mental autoritaire"
                }
            ]
        }

        genre = genre.lower()
        choix = univers_data.get(genre, random.choice(list(univers_data.values())))
        univers = random.choice(choix)

        embed = f"🌐 **Univers généré** ({genre})\n"
        embed += f"• **Peuple** : {univers['peuple']}\n"
        embed += f"• **Géographie** : {univers['géographie']}\n"
        embed += f"• **Société** : {univers['société']}\n"
        embed += f"• **Lieu emblématique** : {univers['lieu']}"

        await ctx.send(embed)

async def setup(bot):
    await bot.add_cog(GenerateurUnivers(bot))
