# Description: Programme qui permet de déterminer le département d'un numéro de téléphone

class indicTelephonique:
    
    def __init__(self, listeInfo, indicatif):
        self.listeInfo = listeInfo
        self.indicatif = indicatif

    def appelNombre_Villes_Indicatif(self):
        listeDept = (
                        (1,(75,77,78,91,92,93,94,95)),
                        (2,(14,18,22,27,28,29,35,36,37,41,44,45,49,50,53,56,61,72,76,85,974,976)),
                        (3,(2,8,10,21,25,39,51,52,54,55,57,58,59,60,62,67,68,70,71,80,88,89,90)),
                        (4,(1,3,4,5,6,7,11,13,15,"2A","2B",26,30,34,38,42,43,48,63,66,69,73,74,83,84)),
                        (5,(9,12,16,17,19,23,24,31,32,33,40,46,47,64,65,79,81,82,86,87,971,972,973,975,977,978))
                    )
        if self.indicatif == 1:
            nbVilles = extract_villes_depart_indicatif(listeDept[0], self.listeInfo)
        elif self.indicatif == 2:
            nbVilles = extract_villes_depart_indicatif(listeDept[1], self.listeInfo)
        elif self.indicatif == 3:
            nbVilles = extract_villes_depart_indicatif(listeDept[2], self.listeInfo)
        elif self.indicatif == 4:
            nbVilles = extract_villes_depart_indicatif(listeDept[3], self.listeInfo)
        elif self.indicatif == 5:
            nbVilles = extract_villes_depart_indicatif(listeDept[4], self.listeInfo)
        
        print(f"Nombre de villes ayant l'indicatif téléphonique 0{self.indicatif} est de {nbVilles}")
    
def extract_villes_depart_indicatif(val, listeInfo):

    nbVilles = 0
    if val[0] == 1:
        file_name = "PARIS.txt"
    elif val[0] == 2:
        file_name = "NO02.txt"
    elif val[0] == 3:
        file_name = "NE03.txt"
    elif val[0] == 4:
        file_name = "SE04.txt"
    elif val[0] == 5:
        file_name = "SO05.txt"
        
    with open(file_name, "w", encoding="utf-8") as file:
        for element in listeInfo:
            if element[0] in val[1]:
                nbVilles += 1
                file.write(f"{element[2]} {element[1]}({element[0]})" + "\n")
    
    return nbVilles

