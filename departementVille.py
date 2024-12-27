import matplotlib.pyplot as plt

class Departement:
    def __init__(self, numDep, listeVilles):
        self.numDep = numDep
        self.villes = listeVilles
        self.depVilles = []

    def ajouter_ville(self):
        for ville in self.villes:
            if self.numDep == ville[0]:
                self.depVilles.append(ville)
        
    def appelNombre_Villes_Departement(self):
        nbVilles = len(self.depVilles)
        print(f"Nombre de villes dans le département {self.numDep} est de {nbVilles}")
        file_name = f"DEP{self.numDep}.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            for element in self.depVilles:
                file.write(f"{element}" + "\n")
        print(f"Les villes du département {self.numDep} sont dans le fichier {file_name}")
    
    def MinMax(self):
        minmax = []
        with open(f"Top5Villes_{self.numDep}.txt", "r", encoding="utf-8") as file:
            for i in range(5):
                element = file.readline()
                minmax.append(element)
        
        with open(f"Min5Villes_{self.numDep}.txt", "r", encoding="utf-8") as file:
            for i in range(5):
                element = file.readline()
                minmax.append(element)
                
        
        with open(f"MinMax5Villes_{self.numDep}.txt", "w", encoding="utf-8") as file:
            for element in minmax:
                file.write(str(element))
    
    def Max5(self):
        maxi = []
        count = 0
        for element in self.depVilles[::-1]:
            if count < 5:
                maxi.append(element)
            count += 1
        with open(f"Top5Villes_{self.numDep}.txt", "w", encoding="utf-8") as file:
            for element in maxi:
                file.write(str(element) + "\n")

    def Min5(self):
        mini = []
        count = 0
        for element in self.depVilles:
            if count < 5:
                mini.append(element)
            count += 1
        with open(f"Min5Villes_{self.numDep}.txt", "w", encoding="utf-8") as file:
            for element in mini:
                file.write(str(element) + "\n")
    
    def MinMax10Accroissement(self):
        """
        Recherche des 10 villes ayant la plus forte baisse et le plus fort accroissement de population
        entre 1999 et 2012 dans un département donné, en utilisant le tri à bulles.
        """
        noms = []
        croissances = []

        # Lecture du fichier et extraction des données
        with open(f"DEP{self.numDep}.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    val = eval(line.strip())  # Convertir la chaîne en liste
                    nom, croissance1, croissance2 = str(val[1]), int(val[4]), int(val[5])
                    noms.append(nom)
                    croissances.append(croissance2 - croissance1)  # Calcul de la croissance
        # Tri à bulles basé sur les croissances
        n = len(croissances)
        for i in range(n):
            for j in range(0,n-i-1):
                if croissances[j] > croissances[j+1]:
                    croissances[j], croissances[j+1] = croissances[j+1], croissances[j]
                    noms[j], noms[j+1] = noms[j+1], noms[j]
        
        min_noms = noms[:10]
        min_croissances = croissances[:10]
        max_noms = noms[-10:]
        max_croissances = croissances[-10:]

        # Écriture des fichiers de sortie
        with open(f"TopAcc10Villes_{self.numDep}.txt", "w", encoding="utf-8") as file:
            for i in range(len(max_noms)):
                file.write(f"{self.numDep},{max_noms[i]},{max_croissances[i]}\n")

        with open(f"MinAcc10Villes_{self.numDep}.txt", "w", encoding="utf-8") as file:
            for i in range(len(min_noms)):
                file.write(f"{self.numDep},{min_noms[i]},{min_croissances[i]}\n")
        
    def traceHistoVilles(self):
        moyenne = 0
        for ville in self.depVilles:
            moyenne += ville[3]
        moyenne = moyenne / len(self.depVilles) 
        
        somme_ecarts_carres = 0
        for ville in self.depVilles:
            somme_ecarts_carres += (ville[3] - moyenne) ** 2 
        variance = somme_ecarts_carres / len(self.depVilles)
        ecart_type = variance ** 0.5

        print(f"Moyenne : {moyenne:.3f}")
        print(f"Écart-type : {ecart_type:.3f}")
        
        noms_villes = []  # Noms des villes
        for ville in self.depVilles:
            noms_villes.append(ville[1])
        populations = []  # Populations des villes
        for ville in self.depVilles:
            populations.append(ville[3])

        # Création du graphique à bâtons
        plt.figure(figsize=(12, 6))
        plt.hist(populations, bins='auto', color="blue", edgecolor='red')
        plt.title(f"Dépt {self.numDep} Nombre de villes en fonction des Habitants")
        plt.xlabel("Nombre d'habitants")
        plt.ylabel("Nombre de villes")
        plt.tight_layout()
        plt.show()
    
    

def MinMax5_villes_Habitants(dep:Departement):
    """
    :param numDept:
    :param lstVillesDepart ou listeInfo:

        recherche de 5 villes ayant le MOINS d'habitants dans un tableau
        recherche de 5 villes ayant le PLUS d'habitants dans un tableau
        on peut trier la liste par ordre croissant
        *** On IMPOSE le TRI BULLE vu au TP7 ****
        puis extraire les 5 premières valeurs
    """
    
    for i in range(len(dep.depVilles)):
        # Parcourir la liste jusqu'à n-i-1 (les derniers éléments sont déjà triés)
        for j in range(0, len(dep.depVilles)-i-1):
            # Si l'élément actuel est plus grand que le suivant, on les échange
            if dep.depVilles[j][3] > dep.depVilles[j+1][3]:
                dep.depVilles[j], dep.depVilles[j+1] = dep.depVilles[j+1], dep.depVilles[j]
    
    dep.Max5()
    dep.Min5()
    dep.MinMax()
    print("creation des fichiers Top5Villes et Min5Villes et MinMax5Villes")
    
    return dep.depVilles
    
    
    