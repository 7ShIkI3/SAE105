# main.py
from reader import CsvReader  # Import de la classe CsvReader
from extractInfo import InfoVilles  # Import de la classe InfoVilles
from departementVille import Departement, MinMax5_villes_Habitants  # Import de la classe Departement
from indicTelephonique import indicTelephonique  # Import de la classe indicTelephonique
from map import Map1, Map2  # Import de la classe Map
from ville import France, parcoursVilles  # Import de la classe France

# Création d'une instance de CsvReader
csv_reader = CsvReader()

# Lecture du fichier CSV
csv_reader.set_data('villes_france.csv')  # Remplacez 'villes.csv' par votre fichier CSV réel

# Récupération des données lues
data = csv_reader.get_data()

# Création d'une instance de InfoVilles pour gérer les informations des villes
info_villes = InfoVilles()

# Traitement des données et affichage des résultats
villes_info = info_villes.set_info(data)

# Affichage des villes traitées
# for ville in villes_info:
#     print(ville)
print(len(villes_info), "villes traitées")

def indicatif_telephonique():
    nb_indicatif = int(input("Entrez l'indicatif téléphonique(01,02,03,04,05) : "))
    indicatif = indicTelephonique(villes_info, nb_indicatif)
    indicatif.appelNombre_Villes_Indicatif()
    
def departement():
    nb_dep = int(input("Entrez le numéro du département : "))
    depart = Departement(nb_dep, villes_info)
    depart.ajouter_ville()
    depart.appelNombre_Villes_Departement()

def minmax():
    nb_dep = int(input("Entrez le numéro du département : "))
    depart = Departement(nb_dep, villes_info)
    depart.ajouter_ville()
    MinMax5_villes_Habitants(depart)

def mapRegion():
    nb_dep = int(input("Entrez le numéro du département : "))
    depart = Departement(nb_dep, villes_info)
    depart.ajouter_ville()
    MinMax5_villes_Habitants(depart)
    map = Map1(nb_dep)
    map.mapTenVilles()

def minmaxaccroissement():
    nb_dep = int(input("Entrez le numéro du département : "))
    depart = Departement(nb_dep, villes_info)
    depart.ajouter_ville()
    depart.MinMax10Accroissement()

def histo():
    nb_dep = int(input("Entrez le numéro du département : "))
    depart = Departement(nb_dep, villes_info)
    depart.ajouter_ville()
    depart.traceHistoVilles()

def parcourvilleappelle():
    ville1 = str(input("Entrez le nom de la ville 1 : "))
    ville2 = str(input("Entrez le nom de la ville 2 : "))
    rayon = int(input("Entrez le rayon de la ville : "))
    france = France(ville1.upper(), ville2.upper(), villes_info, rayon)
    map = Map2(rayon)
    parcoursVilles(france)
    map.map_trajet(france.get_ville1(), france.get_ville2())
    

def menu():
    print("1. Afficher les villes d'un département")
    print("2. Afficher les villes d'un indicatif téléphonique")
    print("3. Afficher les villes Max et Min d'un derpartement")
    print("4. Afficher la map d'une région et d'un département")
    print("5. Afficher letaux d'accroissement des villes d'une région entre 1999 et 2012")
    print("6. Afficher l'histograme d'un département")
    print("7. Afficher le parcours d'une ville a une autre")
    print("8. Quitter")
    choix = input("Entrez votre choix: ")
    if choix == "1":
        print("Afficher les villes d'un département")
        departement()
    elif choix == "2":
        print("Afficher les villes d'un indicatif téléphonique")
        indicatif_telephonique()
    elif choix == "3":
        print("Afficher les villes Max et Min d'un derpartement")
        minmax()
    elif choix == "4":
        print("Afficher la map d'une région et d'un département")
        mapRegion()
    elif choix == "5":
        print("Afficher letaux d'accroissement des villes d'une région entre 1999 et 2012")
        minmaxaccroissement()
    elif choix == "6":
        print("Afficher l'histograme d'un département")
        histo()
    elif choix == "7":
        print("Afficher le parcours d'une ville a une autre")
        parcourvilleappelle()
    elif choix == "8":
        print("Au revoir")
        exit(0)
    menu()

if __name__ == "__main__":
    menu()