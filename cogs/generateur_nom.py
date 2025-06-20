from discord.ext import commands
import random

class GenerateurNom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nom(self, ctx, genre: str = "masculin", style: str = "réel"):
        genre = genre.lower()
        style = style.lower()

        base_noms = {
            "réel": {
                "masculin": [
                    "Julien", "Arthur", "Samuel", "Leo", "Omar", "Nino", "Raphaël", "Lucas", "Enzo", "Théo",
                    "Noah", "Nathan", "Hugo", "Gabriel", "Ethan", "Jules", "Louis", "Paul", "Mathis", "Léo",
                    "Axel", "Sacha", "Tom", "Nolan", "Timeo", "Eliott", "Adam", "Aaron", "Kylian", "Milan",
                    "Maxime", "Antoine", "Simon", "Victor", "Rayan", "Ilhan", "Ilyes", "Amir", "Adrien",
                    "Téo", "Gaspard", "Baptiste", "Clément", "Yanis", "Maël", "Benjamin", "Valentin", "Noé",
                    "Tristan", "Corentin", "Émile", "Robin", "Thierry", "Lenny", "Cyril"
                ],
                "féminin": [
                    "Clara", "Élise", "Sophie", "Maya", "Salomé", "Isaline", "Noémie", "Emma", "Léa", "Chloé",
                    "Manon", "Camille", "Alice", "Inès", "Anna", "Lina", "Lucie", "Juliette", "Sarah", "Lou",
                    "Zoé", "Eva", "Ambre", "Jeanne", "Agathe", "Rose", "Nina", "Louna", "Ava", "Romane",
                    "Charlotte", "Iris", "Maëlys", "Capucine", "Océane", "Victoria", "Alix", "Garance",
                    "Mila", "Clémence", "Jade", "Léonie", "Adèle", "Lila", "Héloïse", "Margaux", "Aurélie",
                    "Élina", "Elsa", "Théa", "Yasmine", "Anaëlle", "Amandine"
                ]
            },
            "fantasy": {
                "masculin": [
                    "Thamior", "Kael", "Eldan", "Gorath", "Vaelor", "Darik", "Azran", "Fenric", "Zephor",
                    "Althar", "Korian", "Malrick", "Tavion", "Rygar", "Dalan", "Brellan", "Faeron", "Harkun",
                    "Talden", "Zareth", "Vaelros", "Kendric", "Othorion", "Nymor", "Grathar", "Elion", "Drakos",
                    "Tarven", "Maelor", "Iskarn", "Veyric", "Cylor", "Rowain", "Ashor", "Fenwick", "Mordrek",
                    "Lucan", "Karvik", "Jareth", "Branik", "Eldrak", "Taren", "Solamir", "Orvand", "Tyran",
                    "Voren", "Merion", "Zalrick", "Ithor", "Braemyn", "Calion", "Velkar", "Galanor", "Thorne",
                    "Kaelor", "Fendric", "Morwyn", "Grevan"
                ],
                "féminin": [
                    "Lyra", "Elyndra", "Faelwen", "Isil", "Thalia", "Nymeria", "Orwenn", "Aelira", "Sylwen",
                    "Miriel", "Ariseth", "Ysolde", "Lirael", "Thirya", "Narella", "Vaelria", "Xalara", "Elaria",
                    "Seraphyne", "Calithra", "Aeris", "Melwen", "Illiara", "Zephira", "Nalira", "Evandra",
                    "Myrrha", "Talindra", "Norilys", "Elaneth", "Ishara", "Virelle", "Lorina", "Shaelis", "Adalyn",
                    "Nyrielle", "Velwen", "Daelya", "Saphyra", "Yvonnel", "Celistra", "Amrielle", "Thalara",
                    "Keiralei", "Zirelle", "Alirae", "Liraenya", "Vaelina", "Sylphae", "Irithyl"
                ]
            },
            "science-fiction": {
                "masculin": [
                    "Zarik", "Orion", "T-Kal", "Synex", "Jorax", "Arvyn", "Caden", "Nexar", "Vortan", "Kairo",
                    "Xelion", "Dravik", "Zentor", "Lyrix", "Omrek", "Tyrion", "Sarnax", "Elonox", "Jaxor", "Kalren",
                    "Vaedric", "Nyron", "Rylos", "Tharn", "Xevor", "Velan", "Urik", "Mekron", "Sorak", "Zyros",
                    "Dexen", "Lorvek", "Trask", "Eryl", "Quoril", "Kirel", "Zerith", "Nirak", "Yorak", "Talvon",
                    "Sylon", "Revon", "Obrik", "Fexar", "Halek", "Xyron", "Drinor", "Solvak", "Torenn", "Karnex"
                ],
                "féminin": [
                    "Nyxa", "Alira", "Sorea", "Yliane", "X-47", "Zemrah", "Lunessa", "Kaelith", "Velora", "Aeryn",
                    "Syra", "Zoraya", "Mei'na", "Nova", "Talys", "Rivena", "Quenya", "Eryss", "Saphyx", "Iverra",
                    "Celes", "Thalya", "Ornexa", "Kyna", "Jynari", "Aelira", "Vireya", "Myrixa", "Tiraya", "Lureth",
                    "Zayra", "Nelya", "Qira", "Ixen", "Soraya", "Xendra", "Astra", "Nyvora", "Kallis", "Xyliah",
                    "Drasya", "Oralei", "Teysha", "Lysera", "Zenara", "Miralyn", "Synera", "Olyna", "Elexia", "Isyra"
                ]
            },
            "historique": {
                "masculin": [
                    "Marcus", "Guillaume", "Anatole", "Hector", "Lucien", "Théodore", "Octave", "Bertrand",
                    "Sigismond", "Enguerrand", "Alaric", "Basile", "Amaury", "Isidore", "Lothaire", "Armand",
                    "Constantin", "Fulbert", "Balthazar", "Éloi", "Maxence", "Géraud", "Thibault", "Anselme",
                    "Florent", "Godefroy", "Benoît", "Blaise", "Honoré", "Clovis", "Rodolphe", "Achille",
                    "Ulysse", "Venceslas", "Amaël", "Isambard", "Barthélémy", "Eusèbe", "Abélard", "Gustave",
                    "Fernand", "Eugène", "Marceau", "Henri", "Émeric", "Quentin", "Alphonse", "Napoléon", "Jean-Baptiste", "Évariste"
                ],
                "féminin": [
                    "Aliénor", "Isabeau", "Hildegarde", "Agnès", "Constance", "Marguerite", "Éléonore", "Bertille",
                    "Pétronille", "Adélaïde", "Jehanne", "Blanche", "Gisèle", "Clotilde", "Radegonde", "Sybille",
                    "Béatrix", "Hermine", "Mathilde", "Olympe", "Cunégonde", "Séréna", "Honorine", "Ambroisine",
                    "Théophanie", "Céleste", "Gaëtane", "Joséphine", "Victoire", "Amélie", "Antoinette", "Émilienne",
                    "Désirée", "Philomène", "Madeleine", "Léontine", "Odile", "Eudoxie", "Lison", "Euphrosine",
                    "Lucienne", "Édith", "Flavie", "Roseline", "Célestine", "Arsinoé", "Bathilde", "Héloïse", "Sibylle", "Violette"
                ]
            }
        }

        if style not in base_noms or genre not in base_noms[style]:
            await ctx.send("🧭 Utilisation : `!nom [genre] [style]`\nGenres : masculin / féminin\nStyles : réel, fantasy, science-fiction, historique")
            return

        nom_tiré = random.choice(base_noms[style][genre])
        await ctx.send(f"🔮 **Nom généré** ({style.title()} • {genre}) : **{nom_tiré}**")

async def setup(bot):
    await bot.add_cog(GenerateurNom(bot))
