from matplotlib.pyplot import title
import unidecode 



class Title:

    titles = {1: "Maitre de la Flémalle, Vierge à l’écran d’osier, 1425-30", 2: "Hendrick Goltzius, Sainte Marie madeleine, 1614, huile sur panneau",
3 : "Jan Gossaert, portrait d’un homme, 1515-1520", 4 : "Gossaert, Vénus, 1521, huile sur bois",
5: "Jan Gossaert, Danaé, 1527, huile sur panneau",6: "Maarten Van Heemskerck, Autoportrait devant le Colisée de Rome, 1553, huile sur bois", 
7: "Jan van Scorel, Twelve members of the Haarlem Brotherhood of Jerusalem Pilgrims, 1528",
8: "Jan Van Scorel, Le baptême du Christ, vers 1530",
9: "Goltzius, Les compagnons de Cadmus dévorés par le dragon, 1588, gravure au burin ",
10: "Cornelis van Haarlem, Les compagnons de Cadmus dévorés par le dragon 1588, huile sur toile"}

    def transformer(titles):

        titles= titles.lower()

        titles = titles.replace(" ", "")

        titles = titles.replace("-", "")

        titles = titles.replace(",", "")

        titles = titles.replace("_", "")

        titles = titles.replace("’", "")

        titles = titles.replace("'", "")

        titles = unidecode.unidecode(titles)
        return titles

class img:

    img = {1: "data/image/1.png", 2: "data/image/2.png", 3 : "data/image/3.png", 4 : "data/image/4.png", 5 : "data/image/5.png",
    6: "data/image/6.png", 7: "data/image/7.png", 8 : "data/image/8.png", 9 : "data/image/9.png", 10 :"data/image/10.png" }

    