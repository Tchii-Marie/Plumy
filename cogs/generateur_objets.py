import random
from discord.ext import commands

class GenerateurObjet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def objet(self, ctx, *, genre: str = "fantasy"):
        objets = {
            "fantasy": [
                ("Lame de Brume", "rend invisible sous la pleine lune"),
                ("Grimoire d’Écaille", "contient les souvenirs d’un dragon mort"),
                ("Anneau de Cendre", "brûle les promesses non tenues"),
                ("Voile de Chêne", "permet de parler aux forêts anciennes"),
                ("Clé des Douze Nuits", "ouvre les portes des rêves"),
                ("Orbe du Silence", "étouffe toute magie dans un rayon donné"),
                ("Tiare d’Équinoxe", "commande l’équilibre entre ombre et lumière"),
                ("Harpe de Lierre", "calme les tempêtes et fait pleurer les pierres"),
                ("Masque de Poussière", "permet de prendre l’apparence du dernier visage croisé"),
                ("Manteau d’Ombre Pure", "rend invisible à tout être né de lumière"),
                ("Cristal des Lointains Soupirs", "amplifie les souvenirs oubliés"),
                ("Dague des Sept Vérités", "révèle une vérité profonde à chaque victime"),
                ("Flacon d’Air Perdu", "contient le dernier souffle d’un royaume disparu"),
                ("Boussole d’Argile Vivante", "pointe vers ce que l’on nie en soi"),
                ("Sandales de Poussière d’Aurore", "tracent des chemins là où il n’en existe aucun"),
                ("Livre-Miroir", "montre ce que le lecteur refuse de voir"),
                ("Bracelet d’Éclats de Nuits", "confère la vitesse des rêves"),
                ("Lanterne de l’Hibernacle", "attire les esprits errants pour les guider"),
                ("Cor de l’Éveil Ancien", "réveille des entités qui n’ont jamais eu de nom"),
                ("Fragment de Lune Froide", "gèle l’espace autour quand le porteur doute"),
                ("Tapis Volant de Soie Sereine", "ne vole que quand on le persuade par un poème"),
                ("Ceinturon de Roc Boiteux", "fait trembler la terre à chaque pas du porteur"),
                ("Aiguille de l’Instant Déchiré", "coud le passé au présent pour altérer le destin")
            ],
            "science-fiction": [
                ("Nexus-9", "permet de sauter dans des lignes temporelles parallèles"),
                ("Holo-Clé Sigma", "déverrouille tout système de sécurité connu"),
                ("Cortex Lytique", "absorbe temporairement la mémoire d’un individu"),
                ("Rayon Écho", "analyse et reconstitue la matière"),
                ("Gantelet CRX", "contrôle par impulsion mentale des machines"),
                ("Gemme Quantique", "influence les probabilités autour de soi"),
                ("Module Voilé", "rend une zone indétectable aux radars"),
                ("Plume à Neutrinos", "écrit des souvenirs qui n'ont jamais existé"),
                ("Spirale de Kelon", "déploie une bulle temporelle de 3 secondes autour du porteur"),
                ("Injecteur Sigma", "implante temporairement une capacité surhumaine"),
                ("Tissu Spectral", "rend visible toute entité interdimensionnelle"),
                ("Lunettes d’Éclipse Fantôme", "détectent les failles dans l'espace-temps"),
                ("Mémoire Fractale V15", "stocke l’esprit d’un être vivant pendant 12 heures"),
                ("Baguier d’Ancrage Gravitationnel", "permet de marcher sur n’importe quelle surface"),
                ("Perle Chrono-Inversée", "annule les 10 dernières secondes d’un événement une fois"),
                ("Module Échotex", "recrée les dernières paroles prononcées dans une pièce vide"),
                ("Cœur-Miroir Synaptique", "synchronise les émotions entre deux êtres"),
                ("Vortex de poche ZN-7", "absorbe un objet de petite taille dans un mini trou noir personnel"),
                ("SymbioCartouche", "fusionne temporairement ADN et IA pour un accès total à une base de données vivante"),
                ("Puce Mnésique Icare", "déclenche un rêve lucide partagé entre plusieurs utilisateurs"),
                ("Anneau de Vecteur", "projette un hologramme de soi-même quelques secondes dans le futur"),
                ("Casque Panoptique", "perçoit tous les systèmes connectés dans un rayon de 5 km"),
                ("Fiole de Résonance", "déclenche un souvenir enfoui chez ceux qui l’inhalent")

            ],
            "historique": [
                ("Miroir de la Grande Comtesse", "révèle la vérité derrière les mensonges"),
                ("Pointe de Fer Sacré", "ne rate jamais sa cible"),
                ("Carnet d’Opale", "contient des révélations codées d’un espion royal"),
                ("Clavessin Noir", "hante quiconque joue une certaine mélodie"),
                ("Médaillon de l’Édit Perdu", "accuse les traîtres par simple proximité"),
                ("Lampe de l’Exil", "s’allume pour guider les fugitifs"),
                ("Couronne de Sang-Froid", "donne la lucidité en période de chaos"),
                ("Scarabée de Sekhmet", "protège le porteur des malédictions en échange d’un souvenir"),
                ("Stèle des Douze Souffles", "révèle les secrets enfouis sous le sable lors des tempêtes"),
                ("Ankh d’Obscurité", "confère la vie éternelle… mais sans lumière"),
                ("Sistrum de Bastet", "fait danser les serpents ou les esprits, selon l’intention"),
                ("Lyre d’Apollodore", "apaise les conflits à condition de ne jouer qu’une seule mélodie"),
                ("Toge d’Hermès", "donne l’éloquence divine pendant une audience ou un procès"),
                ("Diadème d’Arès", "rend invincible au combat tant qu’on ne regarde pas en arrière"),
                ("Fragment d’Olympe", "permet de poser une question à un dieu, une fois seulement"),
                ("Masque de Xibalba", "permet de voir les morts marcher au crépuscule"),
                ("Calendrier de Jade Fendu", "prophétise les événements liés au sang et au soleil"),
                ("Dent du Serpent Céleste", "ouvre les portes entre les mondes en cas de sacrifice"),
                ("Amulette de Copal", "révèle la vérité lorsqu’elle brûle en présence de trahison"),
                ("Chasquis d’Or", "transmet un message sans qu’il soit jamais écrit"),
                ("Bracelet du Soleil Caché", "réchauffe celui qui le porte dans les lieux sacrés"),
                ("Cape de Quipu Vivant", "enregistre les actions du porteur sous forme de nœuds mouvants"),
                ("Tumi Silencieux", "soigne toute blessure, mais efface un souvenir en échange"),
                ("Hématite du Légat", "rend insensible aux interrogatoires"),
                ("Médaillon d’Alexandrie", "confère la compréhension de n’importe quelle langue ancienne"),
                ("Boussole d’Orient Perdu", "mène toujours là où le cœur ment"),
                ("Sceau de l’Archiviste", "verrouille un secret dans l’esprit de son porteur")
            ]
        }

        genre = genre.lower()
        objets_genre = objets.get(genre, sum(objets.values(), []))
        nom, pouvoir = random.choice(objets_genre)

        message = f"🧳 **Objet généré** ({genre if genre in objets else 'aléatoire'}) : *{nom}*, {pouvoir}."
        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(GenerateurObjet(bot))
