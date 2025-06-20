import random
from discord.ext import commands

class GenerateurIntrigue(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def intrigue(self, ctx):
        themes = [
            "la rédemption", "la trahison", "l'ambition", "la liberté", "la vengeance", "le sacrifice", "la survie",
            "le pouvoir", "la destinée", "l'amour interdit", "le mensonge", "l'identité", "la découverte de soi",
            "le devoir", "la résilience", "la loyauté", "la jalousie", "le deuil", "l'illusion", "l'obsession",
            "la justice", "l'honneur", "l'exil", "la peur de l’inconnu", "la corruption", "la mémoire", "le temps", 
            "le chaos", "la folie", "la mémoire", "l'immortalité", "le devoir", "la résistance", "la perte", "la transformation",
            "la peur de l’inconnu", "le secret", "l'obsession", "la métamorphose", "la vérité cachée", "le dépassement de soi",
            "la dualité", "la révolte", "l’héritage", "la corruption", "le temps", "l'honneur", "le pardon"
        ]

        genres = [
            "fantasy", "science-fiction", "historique", "post-apocalyptique", "thriller", "conte magique",
            "romance dystopique", "steampunk", "épopée mythologique", "aventure spatiale", "horreur psychologique",
            "policier", "dark fantasy", "urban fantasy", "drame victorien", "satire politique", "mystère ésotérique",
            "odysée interdimensionnelle", "survival horror", "western occulte", "cyberpunk", "romance",
            "épouvante", "quête mythologique", "road story temporel", "polar futuriste", "aventure épique", "uchronie"
        ]


        personnages = [
            "un ancien soldat désabusé",
            "une orpheline aux pouvoirs cachés",
            "un érudit rongé par l’obsession",
            "une voleuse au grand cœur",
            "un roi déchu cherchant la rédemption",
            "une aventurière cynique mais brillante",
            "un rebelle traqué par l’Empire",
            "un prêtre confronté à une hérésie",
            "une capitaine d’aéronef audacieuse",
            "un mercenaire qui doute de sa mission",
            "une androïde à la recherche d’humanité",
            "un bibliothécaire gardien de secrets interdits",
            "une soigneuse capable de manipuler la vie",
            "un chasseur de reliques maudites",
            "un hacker idéaliste dans une mégacité corrompue",
            "une enquêtrice hantée par son passé",
            "un illusionniste traqué pour ses dons",
            "une mécanicienne de génie aux origines incertaines",
            "un orateur charismatique au sombre dessein",
            "une descendante d’une lignée oubliée",
            "un cartographe explorant les confins du réel",
            "une diplomate prise entre deux mondes",
            "un gladiateur en quête de liberté",
            "un mage enfermé pour avoir défié les dieux",
            "une espionne infiltrée dans la cour ennemie",
            "un musicien dont les notes altèrent le monde",
            "une survivante déterminée d’un monde en ruine",
            "un enfant prophétique échappé du contrôle",
            "une institutrice confrontée à une école démoniaque","un ancien soldat désabusé", "une orpheline aux pouvoirs cachés",
            "un érudit obsessionnel", "un rebelle au grand cœur", "une prêtresse tourmentée",
            "un espion sans passé", "un inventeur incompris", "une androïde en quête d’humanité",
            "un roi déchu", "une mage bannie", "un pirate au coeur tendre", "un chasseur de montres",
            "un monstre qui veut devenir humain"
        ]


        conflits = [
            "doit empêcher l'effondrement d'un royaume", "cherche à venger un proche assassiné", 
            "découvre qu'il est manipulé depuis le début", "doit trahir ses idéaux pour survivre", 
            "tombe amoureux de son ennemi", "est victime d’une prophétie oubliée", 
            "porte un secret pouvant changer le monde", "doit fuir un passé sanglant","doit choisir entre le bien du monde et celui qu'il aime","doit voler un artefact interdit au péril de sa vie", "est confronté à son double venu d'un autre monde",
            "est lié à une ancienne prophétie oubliée",
            "porte un secret capable de tout changer",
            "tente de fuir un passé sanglant",
            "doit choisir entre le bien du monde et celui qu’il aime",
            "doit voler un artefact interdit au péril de sa vie",
            "est confronté à son double venu d’un autre monde",
            "doit briser un pacte ancien pour se libérer",
            "est injustement accusé et traqué comme un monstre",
            "décide de renverser les dieux eux-mêmes",
            "doit infiltrer un ordre dont il partage pourtant les convictions",
            "est hanté par des visions d’un avenir inévitable",
            "doit empêcher une guerre qu’il a lui-même déclenchée",
            "est l’arme vivante qu’il doit combattre",
            "doit sauver un monde qui le rejette",
            "tente d’effacer une vérité trop terrible à admettre",
            "doit faire alliance avec un ennemi juré",
            "doit sacrifier sa mémoire pour atteindre son objectif",
            "est contraint de fuir après avoir brisé un serment sacré",
            "doit contredire une prophétie que tout le monde croit vraie",
            "tente de reconstruire une société détruite par ses propres erreurs"
        ]

        obstacles = [
            "mais est traqué par des fanatiques déterminés",
            "alors que ses alliés deviennent des ennemis",
            "tout en étant rongé par la culpabilité",
            "dans un monde en ruine où chaque pas est un danger",
            "tandis qu'une entité invisible manipule ses choix",
            "malgré une mémoire qui s'efface peu à peu",
            "car les ressources viennent à manquer cruellement",
            "en devant affronter ses propres doubles",
            "sous la pression d’une prophétie déformée",
            "pendant que le temps lui est compté",
            "alors qu’il est maudit sans le savoir",
            "avec une identité qu’on lui refuse",
            "tout en portant une relique dangereuse",
            "mais il est considéré comme un traître par tous",
            "alors que son corps se transforme lentement",
            "sous la menace d’un ultimatum impossible",
            "dans un climat de guerre civile imminente",
            "tout en combattant une voix intérieure destructrice",
            "alors que les règles de la réalité commencent à changer",
            "tout en devant protéger quelqu’un qu’il déteste",
            "mais chaque victoire l’éloigne un peu plus de ce qu’il est",
            "sous l’œil constant d’une intelligence supérieure",
            "en étant condamné à ne jamais dire la vérité",
            "dans un monde où ses rêves se matérialisent contre lui",
            "tandis que les souvenirs des autres s’effacent autour de lui", 
            "alors que son passé le rattrape",
            "malgré une malédiction qui le rend invisible",
            "dans un monde où les lois de la physique sont floues",
            "tout en étant traqué par une organisation secrète", 
            "alors que ses actions ont d'étranges conséquences"
        ]

        tonalites = [
            "tragique", "humoristique", "épique", "mélancolique", "cynique", "lyrique", "absurde",
            "poétique", "sombre", "romantique", "grotesque", "délirante", "philosophique", "ironique",
            "onirique", "héroïque", "surréaliste", "inquiétante", "satirique", "introspective",
            "nihiliste", "émerveillée", "dramatique", "cryptique", "désabusée", "baroque", "mystique", "optimiste",
            "désespérée", "mystérieuse", "érotique", "mélodramatique", "sublime", "tendre", "désenchantée", "désillusionnée"
        ]

        intrigue = f"📖 **({random.choice(tonalites).capitalize()})** Dans un monde {random.choice(genres)}, {random.choice(personnages)} confronté à {random.choice(themes)} {random.choice(conflits)}, {random.choice(obstacles)}."

        await ctx.send(intrigue)

async def setup(bot):
    await bot.add_cog(GenerateurIntrigue(bot))
