import random
from discord.ext import commands

class GenerateurDeclencheurs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def catalyseur_idee(self, ctx):
        catalyseurs = [
            "Et si le personnage principal n’était pas réel, mais nécessaire à l’équilibre d’un autre personnage ?",
            "Et si l’antagoniste racontait en fait une version honnête de l’histoire ?",
            "Et si le décor était vivant et faisait partie du complot narratif ?",
            "Et si l’histoire était en train d’être réécrite à l’insu des personnages ?",
            "Et si ton héros n’était pas dans la bonne temporalité… mais croyait l’être ?", 
            "Et si l’univers punissait les personnages dès qu’ils doutaient d’eux-mêmes ?",
            "Et si chaque souvenir effacé devenait une créature tapie dans l’ombre ?",
            "Et si la scène d’ouverture était en fait la fin… vécue à l’envers ?",
            "Et si un personnage refusait d’évoluer, mais que l’univers le changeait malgré lui ?",
            "Et si l’événement déclencheur n’était pas arrivé — mais que tout le monde croyait l’avoir vécu ?",
            "Et si un sentiment collectif (peur, euphorie, foi) devenait un personnage actif du récit ?",
            "Et si chaque acte du héros déclenchait une catastrophe dans un autre monde lié à son subconscient ?",
            "Et si un livre écrit dans le futur dictait les choix présents ?",
            "Et si l’auteur fictif de l’histoire intervenait dans la narration… puis disparaissait ?",
            "Et si la fin avait déjà été racontée… mais codée dans une chanson, un motif ou un lieu ?",
            "Et si un oubli volontaire créait une faille dans le monde ?",
            "Et si la promesse du récit était volontairement trahie par le narrateur lui-même ?", 
            "Et si le personnage principal découvrait qu’il est dans la mauvaise histoire ?",
            "Et si l’ennemi avait raison… mais pour de mauvaises raisons ?",
            "Et si le décor n’était pas un lieu, mais un être vivant très discret ?",
            "Et si ce qui semblait perdu n’avait jamais existé ?",
            "Et si la fin était déjà arrivée mais que personne ne l’avait remarqué ?"
        ]
        idée = random.choice(catalyseurs)
        await ctx.send(f"⚡ **Catalyseur narratif** : {idée}")

    @commands.command()
    async def twist(self, ctx):
        twists = [
            "Le personnage principal est en fait le descendant de son propre antagoniste.",
            "L’histoire se déroule dans un rêve collectif créé pour apaiser une entité cosmique.",
            "Le méchant est une IA formée à partir des souvenirs de l’héroïne.",
            "Toute la quête n’était qu’une distraction organisée par une force supérieure.",
            "Le personnage principal a déjà échoué, et vit une illusion de succès depuis.",
            "Le mentor du héros est en fait la cause de tout.",
            "Le personnage principal n’existe que dans la mémoire d’un autre.",
            "Le but poursuivi n’a jamais été réel, mais maintenait l’équilibre du monde.",
            "Tout était une simulation orchestrée par un personnage secondaire.",
            "La prophétie concernait l’antagoniste, pas le héros.",
            "Le héros n’a jamais quitté l’endroit où tout a commencé… il vit une boucle mentale.",
            "L’antagoniste agit en réalité pour préserver un secret que le héros ne pourrait pas supporter.",
            "Le personnage secondaire était l’observateur du récit depuis le début et décide enfin d’intervenir.",
            "L’objet qu’on croyait essentiel n’a aucune utilité… mais tout le monde y croit, et c’est ce qui le rend dangereux.",
            "L’univers dans lequel évoluent les personnages est une reconstitution basée sur des souvenirs altérés.",
            "Le héros est l’héritier direct de la catastrophe qu’il cherche à empêcher.",
            "Chaque personnage est en fait un aspect d’une même personne éclatée dans plusieurs corps ou mondes.",
            "La quête réussit… mais détruit le seul lien qui rendait les personnages humains.",
            "Ce que les personnages croyaient être l’ennemi était en fait une illusion collective projetée par la peur.",
            "La mémoire des personnages est réinitialisée à chaque fin d’histoire – et celle-ci n’est que l'une parmi d'autres.",
            "Le narrateur ment intentionnellement depuis le début — et il commence à en avoir honte.",
            "Les héros sont déjà morts, et toute l’histoire est leur tentative de comprendre pourquoi.",
            "Le monde est en fait une entité vivante qui se nourrit de la peur des personnages.",
            "Le héros est en fait le double d'un autre personnage, et il ne s'en souvient pas"
        ]
        idée = random.choice(twists)
        await ctx.send(f"🔄 **Twist narratif** : {idée}")

    @commands.command()
    async def elementdeclencheur(self, ctx):
        declencheurs = [
            "Un message oublié refait surface au mauvais moment.",
            "Quelqu’un brise une règle que personne ne connaissait.",
            "Un objet enterré depuis des siècles se réveille subitement.",
            "Une vérité scientifique est prouvée… puis effacée aussitôt.",
            "Un enfant ouvre une porte que personne n’avait le droit de voir.",
            "Un inconnu remet un objet sans explication.",
            "Un rêve devient réalité, mais personne ne s’en souvient sauf le héros.",
            "Une cérémonie tourne mal et réveille un fragment du passé.",
            "Quelqu’un brise une règle que personne ne connaissait.",
            "Un message codé est trouvé dans un objet oublié.",
            "Un vieil ennemi refait surface avec une version altérée du passé.",
            "Le ciel change de couleur et personne ne veut en parler.",
            "Un personnage rêve d’un lieu qu’il n’a jamais visité… jusqu’à ce qu’il le trouve.",
            "Un objet réputé perdu depuis des siècles apparaît dans un lieu banal.",
            "Une personne revient d’entre les morts mais ne reconnaît personne.",
            "Une fête locale est interrompue par un phénomène inexplicable.",
            "Un enfant affirme avoir vu quelque chose que personne d’autre ne perçoit.",
            "Une bibliothèque ou un système s’effondre, révélant des données ou secrets effacés.",
            "Un ordre est donné… mais tout le monde l'entend différemment.",
            "Un animal adopte un comportement anormal et guide un personnage vers un lieu interdit.",
            "Le monde oublie progressivement un mot, un souvenir, ou une personne.", 
            "Un personnage se réveille avec une cicatrice inexplicable."
        ]
        idée = random.choice(declencheurs)
        await ctx.send(f"🎬 **Événement déclencheur** : {idée}")

    @commands.command()
    async def evolutions(self, ctx):
        arcs = [
            "De serviteur invisible à déclencheur d’une révolution mondiale.",
            "De gardien loyal à traître par conviction personnelle.",
            "De victime à créateur de chaos.",
            "De chasseur de vérité à protecteur du mensonge.",
            "D’oublié·e à mémoire vivante du monde.",
            "De suiveur silencieux à leader inattendu",
            "De victime résignée à provocateur du changement",
            "De croyant dévot à révolutionnaire désabusé",
            "De confident loyal à traître justifié",
            "De puissant en chute à fragile éclairé",
            "De suiveur silencieux à voix qui renverse l’ordre établi",
            "De porteur de lumière à gardien des ténèbres par nécessité",
            "D’orphelin apeuré à protecteur d’un peuple entier",
            "D’idéaliste sincère à cynique redoutable… puis à rêveur lucide",
            "De messager effacé à mémoire incarnée d’un monde disparu",
            "De guerrier furieux à artisan de paix insoupçonné",
            "D’ombre dans l’histoire d’un autre à héros de sa propre légende",
            "De gardien de l’ordre à artisan d’un chaos fécond",
            "D’imposteur paniqué à figure d’inspiration assumée",
            "De cœur de pierre à créateur de liens sincères",
            "De disciple convaincu à briseur de dogme",
            "De maître du contrôle à embrasseur du chaos"
        ]
        idée = random.choice(arcs)
        await ctx.send(f"📈 **Évolution potentielle** : {idée}")

async def setup(bot):
    await bot.add_cog(GenerateurDeclencheurs(bot))
