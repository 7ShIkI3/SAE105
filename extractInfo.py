class InfoVilles:
    
    @staticmethod
    def set_info(liste):
    
        L= []
        temp = []
        for i in liste:
            temp.append(i.split(','))

        for i in temp:
            # eval(..) transforme "Annecy" en Annecy, et "18.59" en 18.59 donc une chaîne de caractères sans les "..."
            # ensuite il faut transformer le type str() en int() ou float()
            # Pour tous les départements sauf la Corse 2A et 2B
            # et les territoires d'Outre-Mer : les derniers champs sont à 'NULL'
            if ((eval(i[1]) != '2A') and (eval(i[1]) != '2B')) and i[25] != 'NULL':
                L.append([int(eval(i[1])),      # numéro du Département
                        eval(i[3]),             # Nom de la ville en MAJUSCULE
                        eval(i[8]),             # Code postal
                        int(eval(i[14])),       # population en 2010
                        int(eval(i[15])),       # population en 1999
                        int(eval(i[16])),       # population en 2012
                        float(eval(i[17])),     # densité
                        float(eval(i[18])),     # surface
                        float(eval(i[19])),     # longitude
                        float(eval(i[20])),     # latitude
                        int(eval(i[25])),       # altitude min
                        int(eval(i[26]))])      # altitude max
            elif i[13] == 'NULL': # pour gérer les départements et territoires d'Outre-Mer : 971, 972, 974, ...
                L.append([int(eval(i[1])),
                        eval(i[3]),
                        eval(i[8]),
                        int(eval(i[14])),
                        int(eval(i[15])),
                        int(eval(i[16])),
                        float(eval(i[17])),
                        float(eval(i[18])),
                        float(eval(i[19])),
                        float(eval(i[20])),
                        "NULL",
                        "NULL"])
            else:
                L.append([eval(i[1]),
                        eval(i[3]),
                        eval(i[8]),
                        int(eval(i[14])),
                        int(eval(i[15])),
                        int(eval(i[16])),
                        float(eval(i[17])),
                        float(eval(i[18])),
                        float(eval(i[19])),
                        float(eval(i[20])),
                        i[25],
                        i[26]])
        return L
    
    