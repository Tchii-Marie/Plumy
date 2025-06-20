import random
from discord.ext import commands

class GenerateurElement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def idee(self, ctx):
        themes = [
            "rébellion oubliée", "magie incontrôlable", "pacte dangereux",
            "mutation de masse", "souvenir volé", "prophétie faussée",
            "enfermement mental", "métamorphose involontaire",
            "fragment de vérité", "sacrifice inutile", 
            "dérèglement cosmique","vengeance déguisée", 
            "mutation de masse", "souvenir volé", 
            "résurrection accidentelle",
            "effacement de mémoire collective",
            "trahison programmée",
            "héritage incontrôlable",
            "oubli volontaire",
            "refus de la destinée",
            "culte détourné",
            "transmission interdite",
            "le silence devenu une arme",
            "le rêve qui colonise le réel",
            "la mémoire devenue marchandise",
            "la vérité interdite à nommer",
            "la mort qui ne vient pas"
        ]

        personnages = [
            "un(e) enfant qui refuse de dormir",
            "un(e) espion(ne) piégé(e) dans son propre mensonge",
            "un(e) bibliothécaire qui sait trop de choses",
            "un(e) ancien(ne) héros qui a tout oublié",
            "un(e) robot curieux(se) de la mort",
            "un(e) sorcier(e) qui ne croit plus à sa magie",
            "un(e) pilote hanté(e) par une chanson",
            "un(e) oracle condamné(e) à ne prédire que des erreurs",
            "un(e) bibliothécaire qui sait trop de choses",
            "un(e) roi/reine détesté(e) de son propre reflet",
            "un(e) immortel(le) qui cherche à mourir",
            "un(e) bâtisseur(se) de ponts qui ne mène nulle part",
            "un(e) cartographe qui invente des territoires inconnus",
            "un(e) voyageur(se) qui n’a plus de corps",
            "un(e) peintre qui capture les souvenirs d’autrui",
            "un(e) messager(ère) incapable de lire",
            "un(e) archiviste qui entend les voix des parchemins",
            "un(e) monarque gouverné(e) par un animal-conseiller",
            "un(e) guerrier(ère) qui entend les pensées de son épée",
            "un(e) scientifique qui perçoit les rêves comme données brutes",
            "un(e) musicien(ne) dont chaque note modifie la réalité",
            "un(e) cartographe qui dessine des territoires qui n’existent que la nuit",
            "un(e) survivant(e) persuadé(e) d’avoir rêvé l’apocalypse",
            "un(e) horloger(ère) capable d’arrêter le temps mais jamais deux fois au même endroit",
            "un(e) acrobate fantôme qui rejoue sa dernière chute en boucle",
            "un(e) dresseur(se) de monstres intérieurs",
            "un(e) mage en exil dont la voix déclenche des catastrophes naturelles",
            "un(e) ancien(ne) roi/reine désormais mendiant(e) de sagesse",
            "un(e) peintre d’émotions interdites",
            "un(e) veilleur(se) d’un phare cosmique oublié",
            "un(e) colporteur(se) d’histoires qu’il/elle ne comprend pas",
            "un(e) automate doté(e) d’un seul souvenir humain",
            "un(e) rêveur(se) lucide prisonnier(e) d’un monde mental collectif",
            "un(e) voleur(se) d'identités pris(e) à son propre piège",
            "un(e) sculpteur(se) de néant qui laisse des traces invisibles",
            "un(e) exorciste allergique aux fantômes",
            "un(e) vétérinaire pour créatures mythiques qui ne croit pas en la magie",
            "un(e) capitaine de navire n’ayant jamais vu la mer",
            "un(e) chanteur(se) dont chaque note tue un souvenir",
            "un(e) archiviste du futur qui relit les jours à venir",
            "un(e) tisseur(se) de liens entre les âmes fatiguées"
        ]

        lieux = [
            "un monastère englouti visible à marée basse",
            "une plateforme spatiale qui tourne à contre-temps",
            "un désert où chaque pas produit une illusion différente",
            "un champ de ruines qui pousse la nuit",
            "une ville où les portes ne s’ouvrent plus",
            "un temple inversé suspendu dans le ciel",
            "un théâtre désert qui rejoue sans fin la même scène",
            "une forêt sans oiseaux ni vent",
            "une bibliothèque suspendue entre deux falaises",
            "un pont sans extrémité visible",
            "une auberge construite sur les dos de bœufs géants endormis",
            "un théâtre abandonné hanté par des applaudissements sans public",
            "un champ de statues à moitié enfouies qui tournent la tête la nuit",
            "un phare inversé planté dans la terre au milieu d’un désert gelé",
            "un jardin souterrain aux fleurs carnivores chantantes",
            "un monolithe sculpté par une pluie acide éternelle",
            "une plage où chaque vague efface une émotion",
            "un temple en orbite lentement désaligné de la réalité",
            "une île mobile uniquement visible au coucher du soleil",
            "un marché cosmique accessible seulement pendant les rêves",
            "un escalier en colimaçon qui remonte le temps à chaque marche",
            "une tour faite d’os appartenant à une créature inconnue",
            "une gare ferroviaire où les trains ne s’arrêtent jamais",
            "un puits infini empli d’échos contradictoires",
            "une oasis lunaire maintenue en vie par un vœu",
            "un aquarium déserté rempli d’air solide",
            "une cathédrale abandonnée où pousse une forêt entière",
            "un tunnel qui ne mène qu’à des souvenirs oubliés"
        ]
        creatures = [
            "un chat ailé qui parle en énigmes",
            "un ver translucide qui se nourrit de secrets",
            "un cheval spectral qui n’apparaît qu’aux rêveurs blessés",
            "une nuée de lucioles mémorielles portant des souvenirs volés",
            "un cerf aux ramures d’obsidienne qui efface les pas derrière lui",
            "un golem de papier animé par des textes oubliés",
            "une méduse flottante faite d’hologrammes instables",
            "un dragon aveugle guidé par le chant des échos",
            "un enfant de brume qui grandit à chaque mensonge prononcé",
            "un corbeau tricéphale qui annonce trois futurs différents",
            "une mante-oracle qui lit l’avenir dans les battements du cœur",
            "une araignée d’or tisseuse de pactes impossibles",
            "un chien sans ombre qui garde les portes de l’insomnie",
            "un poisson céleste qui nage dans les silences des gens",
            "un ours de pierre portant un jardin miniature sur son dos"
        ]

        emotions = [
            "une peur ancestrale qui rôde",
            "une joie artificielle persistante",
            "une mélancolie douce mais contagieuse",
            "une colère partagée par tous sans raison",
            "un espoir fragile tapi dans les coins"
        ]
        objets = [
            "une montre arrêtée qui prédit les morts",
            "un masque qui ne peut être retiré sans perdre un souvenir",
            "une clé sans serrure, mais essentielle à l’intrigue"
        ]

        tons = [
            "absurde et poétique", "tragique mais lumineux", "étrangement comique",
            "épique et désenchanté", "intime et fantastique"
        ]

        temps = [
            "pendant une nuit qui dure un an",
            "au lendemain d’un événement effacé des mémoires",
            "dans un futur reconstruit à partir de rêves anciens",
            "lors d’un hiver sans fin"
        ]
        
        catégories = {
            "thème": ("🎯", themes),
            "personnage": ("🧍", personnages),
            "lieu": ("📍", lieux),
            "créature": ("🐾", creatures),
            "émotion": ("💭", emotions),
            "ton": ("🎭", tons),
            "temps": ("⏳", temps),
            "objet": ("🗝️", objets)
        }

        catégorie, (emoji, liste) = random.choice(list(catégories.items()))
        résultat = random.choice(liste)

        await ctx.send(f"{emoji} **{catégorie.capitalize()}** : {résultat}")

async def setup(bot):
    await bot.add_cog(GenerateurElement(bot))