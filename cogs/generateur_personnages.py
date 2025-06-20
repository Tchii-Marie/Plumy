import random
from discord.ext import commands

class GenerateurPersonnage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def personnage(self, ctx, *, genre: str = "général"):
        personnages = {
            "fantasy": [
                "un mage renégat en quête de pardon",
                "une elfe noire bannie de sa tribu",
                "un paladin rongé par un serment ancien",
                "une rôdeuse taciturne au passé brisé",
                "un nain forgeron hanté par une arme maudite",
                "un druide aveugle qui parle aux arbres",
                "un voleur repenti devenu justicier",
                "une sorcière recluse qui entend les voix des ancêtres",
                "un prince déshérité pactisant avec les ombres",
                "une guérisseuse aux dons interdits",
                "un enchanteur amnésique",
                "un chevalier spectral prisonnier de son armure"
            ],
            "science-fiction": [
                "un capitaine de vaisseau en disgrâce",
                "une androïde qui développe des émotions imprévues",
                "un pilote clone en fuite d’un programme militaire",
                "une hackeuse de génie poursuivie par une IA ennemie",
                "un diplomate stellaire au bord de la rupture",
                "un scientifique qui a découvert une vérité interdite",
                "une archiviste intergalactique aux souvenirs fragmentés",
                "un mercenaire génétiquement instable",
                "un explorateur spatio-temporel échoué hors du temps",
                "une ingénieure cybernétique qui voit l’avenir"
            ],
            "historique": [
                "un moine copiste obsédé par une prophétie",
                "une espionne déguisée en suivante à la cour",
                "un chevalier revenu changé d'une croisade sanglante",
                "une guérisseuse accusée de sorcellerie",
                "un navigateur perdu entre deux empires",
                "une aristocrate exilée en quête de rédemption",
                "un corsaire patriote tiraillé par ses alliances",
                "un alchimiste poursuivi par l’inquisition",
                "un peintre révolutionnaire traqué par la monarchie",
                "une comédienne au service secret d’un roi"
            ],
            "post-apocalyptique": [
                "une survivante farouche qui parle aux machines",
                "un messager mutant insensible à la douleur",
                "un père prêt à tout pour protéger son enfant",
                "un(e) cultivateur(trice) de spores hallucinogènes",
                "une mécano adepte du feu sacré du moteur",
                "un prêcheur aveugle entouré de fous armés",
                "un ancien scientifique devenu prophète de ruines",
                "un(e) nomade à moto porteur(se) d’un artefact vital",
                "un(e) ado paranoïaque qui parle au ciel",
                "un(e) cyborg en panne de conscience"
            ],
            "conte magique": [
                "une petite fille qui comprend les oiseaux",
                "un chat botté aristocrate et cynique",
                "un esprit des bois qui se prend pour un roi",
                "un garçon de cuisine qui parle aux objets enchantés",
                "une vieille sorcière tisseuse de destinées",
                "un prince changé en cerf chaque nuit",
                "un miroir curieux qui veut voir le monde",
                "une fée rebelle qui veut devenir humaine",
                "un crapaud savant qui dispense des prophéties",
                "une poupée mécanique aux sentiments naissants"
            ],
            "polar contemporain": [
                "un inspecteur désabusé proche de la retraite",
                "une profileuse brillante mais instable",
                "un journaliste en quête de scoop quitte à tout trahir",
                "une détective privée ruinée par une affaire passée",
                "un policier ripou tiraillé entre loyauté et survie",
                "un procureur obsédé par un dossier jamais résolu",
                "une hackeuse underground traquée par Interpol",
                "un criminologue trop proche du tueur qu'il analyse",
                "une flic infiltrée qui commence à douter de sa mission",
                "un ancien détenu reconverti en justicier de rue",
                "un gardien de prison au passé trouble",
                "un avocat pénaliste alcoolique obsédé par la vérité",
                "une veuve riche persuadée qu’on veut l’éliminer",
                "un écrivain de romans policiers rattrapé par un vrai meurtre",
                "une sœur d’une victime qui enquête en secret",
                "un étudiant en criminologie fasciné par la violence",
                "un légiste solitaire découvrant des signes occultes",
                "un gérant de bar en lien avec le milieu mafieux",
                "une jeune flic idéaliste parachutée dans un commissariat corrompu"
            ]
        }
        personnalites = [
            "froid(e) et calculateur(trice)",
            "loyal(e) mais impulsif(ve)",
            "sensible et en quête de vérité",
            "arrogant(e) mais brillant(e)",
            "mystérieux(se) et mélancolique",
            "idéaliste au cœur brisé",
            "pragmatique et désabusé(e)",
            "drôle et imprévisible",
            "charismatique mais manipulateur(trice)",
            "introverti(e) aux pensées fulgurantes",
            "rêveur(se) incapable de faire face au réel",
            "autoritaire mais profondément juste",
            "sarcastique à la langue bien pendue",
            "obsessionnel(le) mais tenace",
            "téméraire jusqu’à l’inconscience",
            "calculateur(trice) au sang froid",
            "altruiste mais rongé(e) par le doute",
            "solitaire par choix ou par douleur",
            "perpétuellement optimiste",
            "passionné(e) à l’excès",
            "instable mais profondément humain(e)",
            "calme et énigmatique",
            "exubérant(e) et flamboyant(e)",
            "stratège né(e) à la logique glaciale",
            "curieux(se) jusqu’à l’indiscrétion",
            "moralisateur(trice) à l’écoute sélective",
            "affectueux(se) mais naïf(ve)",
            "désabusé(e) et cynique",
            "perfectionniste à la limite de l’obsession",
            "désinvolte face au danger"
        ]

        objectifs = [
            "veut prouver l’existence d’un monde oublié",
            "cherche à libérer un peuple opprimé",
            "espère réécrire son passé",
            "tente de détruire un artefact interdit",
            "désire retrouver une personne disparue",
            "veut empêcher une prophétie de se réaliser",
            "cherche à échapper à sa destinée toute tracée",
            "veut restaurer l'honneur de sa lignée",
            "aspire à créer une nouvelle société",
            "rêve de devenir une légende vivante",
            "veut comprendre les origines d’un fléau ancien",
            "cherche à guérir une maladie incurable",
            "veut faire tomber un empire corrompu",
            "désire atteindre l’immortalité à tout prix",
            "espère faire la paix avec ses démons",
            "veut transmettre un savoir interdit",
            "rêve de découvrir le secret de l’univers",
            "tente de fuir les responsabilités d’un pouvoir immense",
            "cherche à prouver qu’il/elle est plus qu’un(e) simple outil",
            "espère retrouver une vie simple et paisible"
        ]

        faiblesses = [
            "mais ne sait pas faire confiance",
            "mais est rongé(e) par la culpabilité",
            "mais fuit toute forme d’attachement",
            "mais ignore qu’il/elle est manipulé(e)",
            "mais porte un fardeau qu’il/elle cache aux autres",
            "mais est incapable de se pardonner",
            "mais est terrifié(e) par son propre potentiel",
            "mais refuse de demander de l’aide, même en détresse",
            "mais est obsédé(e) par une personne disparue",
            "mais laisse sa colère guider ses choix",
            "mais est prisonnier(e) d’un pacte oublié",
            "mais nie ses émotions avec violence",
            "mais est dépendant(e) à une substance ou un rituel",
            "mais souffre de visions qui altèrent la réalité",
            "mais est sujet(te) à des crises de panique incontrôlables",
            "mais est paralysé(e) par le doute au moment décisif",
            "mais sacrifie tout pour obtenir l’approbation d’un autre",
            "mais agit toujours trop tard",
            "mais rejette toute autorité, même bienveillante",
            "mais se croit invulnérable malgré les preuves contraires"
        ]


        genre = genre.lower()
        choix_genre = personnages[genre] if genre in personnages else sum(personnages.values(), [])
        description = f"🧬 **Personnage généré** : {random.choice(choix_genre)}, {random.choice(personnalites)}, qui {random.choice(objectifs)}, {random.choice(faiblesses)}."

        await ctx.send(description)

async def setup(bot):
    await bot.add_cog(GenerateurPersonnage(bot))


