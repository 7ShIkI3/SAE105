# Classe permettant de lire un fichier CSV
class CsvReader:

    def __init__(self):
        self.data = []

    def set_data(self, file):
        # Lecture du fichier CSV
        with open(file, 'r') as fich:
            self.data = fich.readlines()
        print("Fin de l'Extraction des infos du fichier", file)

    def get_data(self):
        # Retourner les données lues
        return self.data

    def print_data(self):
        # Afficher les données lues
        print(self.data)
