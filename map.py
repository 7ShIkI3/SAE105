import folium, branca

class Map1:
    def __init__(self, depatements):
        self.numDep = depatements
    
    
    def mapTenVilles(self):
        """
        :param numDept: numéro du département pour générer la carte
        """
        longitude = []
        latitude = []
        surface = []
        habitant = []
        
        # Lecture des villes avec forte densité
        with open(f"Top5Villes_{self.numDep}.txt", "r", encoding="utf-8") as Top5Villes:
            for ligne in Top5Villes:
                ville = eval(ligne.strip())  # Convertit la chaîne en liste
                longitude.append(ville[8])  # Coordonnée longitude
                latitude.append(ville[9])  # Coordonnée latitude
                surface.append(ville[7])   # Surface ou densité
                habitant.append(ville[5])   # Nombre d'habitants

        # Lecture des villes avec faible densité
        with open(f"Min5Villes_{self.numDep}.txt", "r", encoding="utf-8") as Min5Villes:
            for ligne in Min5Villes:
                ville = eval(ligne.strip())
                longitude.append(ville[8])
                latitude.append(ville[9])
                surface.append(ville[7])
                habitant.append(ville[5])

        map = folium.Map(location=(latitude[0], longitude[0]), tiles='OpenStreetMap', zoom_start=10)
        cm = branca.colormap.LinearColormap(['blue', 'red'], vmin=min(habitant), vmax=max(habitant))
        map.add_child(cm)

        # Ajout des marqueurs
        for lat, lng, size, color in zip(latitude, longitude, surface, habitant):
            folium.CircleMarker(
                location=[lat, lng],
                radius=size,  # Ajustez le facteur pour une taille réaliste
                color=cm(color),
                fill=True,
                fill_color=cm(color),
                fill_opacity=0.6
            ).add_to(map)

        # Sauvegarde de la carte
        map.save(outfile=f"map_{self.numDep}.html")
        print("Traitement terminé")
    
class Map2:
    
    def __init__(self, rayon):
        self.rayon = rayon   
    
    
    def map_trajet(self, ville1, ville2):
        """
        :param ville1: nom de la ville de départ
        :param ville2: nom de la ville d'arrivée
        """
        points = []
        with open("parcoursVilles.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    data = eval(line.strip())  # Convertir la chaîne en liste
                    points.append((data[9], data[8]))  # Latitude, Longitude
        
        # Création de la carte
        map = folium.Map(location=[46.539758, 2.430331], tiles='OpenStreetMap', zoom_start=6)
        
        
        # Ajout des marqueurs
        for lat, lng in points:
            folium.CircleMarker(
                location=[lat, lng],
                radius=self.rayon/2,  # Ajustez le facteur pour une taille réaliste
                color="blue",
                fill=True,
                fill_color="blue",
                fill_opacity=0.6
            ).add_to(map)

        # Sauvegarde de la carte
        map.save(f"map_Trajet_{ville1}_{ville2}.html")
        print("Traitement terminé")