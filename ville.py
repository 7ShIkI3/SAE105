import math

class France:
    def __init__(self, ville1, ville2, listeInfo, rayon):
        self.ville1 = ville1
        self.ville2 = ville2
        self.listeInfo = listeInfo
        self.rayon = rayon

    def get_ville1(self):
        return self.ville1
    
    def get_ville2(self):
        return self.ville2
    
    def get_rayon(self):
        return self.rayon

    def get_listeInfo(self):
        return self.listeInfo

    def dist_Euclidienne(self, ville1, ville2):
        # Récupération des coordonnées des deux villes
        lat1, lon1 = math.radians(ville1[8]), math.radians(ville1[9])  # Convertir en radians
        lat2, lon2 = math.radians(ville2[8]), math.radians(ville2[9])  # Convertir en radians
        
        # Rayon moyen de la Terre en kilomètres
        R = 6371  
        
        # Calcul de la différence de coordonnées
        x = (lon2 - lon1) * math.cos((lat1 + lat2) / 2)
        y = lat2 - lat1
        
        # Calcul de la distance
        d = math.sqrt(x * x + y * y) * R
        return d

    
def isInDisque(villes:France, uneVille):
    resultat = False
    for ville in villes.get_listeInfo():
        val = villes.dist_Euclidienne(uneVille, ville[1])
        if val <= villes.get_rayon():
            resultat = True
    return resultat

def ensembleVilles(name, ville:France):
    VillesTrouvees = []
    essais = 0
    info_name = rechercheVille(name, ville)  # Fetch complete city info
    
    if info_name == "La ville n'existe pas":
        print(f"{name} is not found in the list.")
        return []

    while len(VillesTrouvees) < 10 * ville.get_rayon() and essais < len(ville.get_listeInfo()):
        current_city = ville.get_listeInfo()[essais]
        val = ville.dist_Euclidienne(info_name, current_city)
        if val <= ville.get_rayon():
            VillesTrouvees.append(current_city)
            print(f"Between {name} and {current_city[1]}, distance is {val:.3f}km")
        essais += 1
    return VillesTrouvees

    
def rechercheVille(name, ville:France):
    """
    :param name: nom de la ville recherchée doit être en MAJUSCULE
    :param listeVilles: liste de toutes les villes
    :return: listeVilles[i] : la ville recherchée
    """
    i = 0
    resultat = ""
    while i < len(ville.get_listeInfo()) and name != ville.get_listeInfo()[i][1]:
        i += 1
    if i < len(ville.get_listeInfo()):
        resultat = ville.get_listeInfo()[i]
    else:
        resultat = "La ville n'existe pas"
    return resultat

def plusProche(ville_ref, ville2, ville:France,):
    """
    Trouve la ville la plus proche de 'ville_ref' parmi toutes les villes de 'ville'.
    """
    liste = []
    listeMin = []
    for v in ville_ref:
        val = ville.dist_Euclidienne(v, ville2)
        liste.append((v, val))
    listeMin.append(liste[0])
    for element in liste:
        if element[1] < listeMin[0][1]:
            listeMin = [element]
    return listeMin[0][0] 

def parcoursVilles(ville:France):
    compteur = 0
    info_ville_depart = rechercheVille(ville.get_ville1(), ville)
    info_ville_arrivee = rechercheVille(ville.get_ville2(), ville)

    if info_ville_depart == "La ville n'existe pas":
        print("Ville de départ non trouvée!")
        return

    liste_parcours_ville = [info_ville_depart]
    visited_cities = {info_ville_depart[1]}  # Utiliser un set pour éviter les doublons

    while info_ville_depart[1] != ville.get_ville2():
        ensemble_ville = ensembleVilles(info_ville_depart[1], ville)  # Ensemble de villes à vérifier

        # Trouver la ville la plus proche
        ville_proche = None
        if ensemble_ville:
            ville_proche = plusProche(ensemble_ville, info_ville_arrivee, ville) 

        if not ville_proche or ville_proche[1] in visited_cities:
            print("Aucune ville valide suivante.")
            break

        visited_cities.add(ville_proche[1])
        compteur += 1
        info_ville_depart = ville_proche
        liste_parcours_ville.append(info_ville_depart)

        if compteur > 1000:
            print("Trop d'itérations, arrêt du processus.")
            break

    print(f"Nombre d'étapes: {compteur}")

    # Sauvegarder dans un fichier
    with open("parcoursVilles.txt", "w", encoding="utf-8") as file:
        for ville in liste_parcours_ville:
            file.write(f"{ville}\n")
