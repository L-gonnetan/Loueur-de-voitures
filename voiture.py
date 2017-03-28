ENUM_ETAT_LOCATION = ["louée", "disponible", "au garage"]


class Voiture(object) :
    def __init__(self, marque, modele, immatriculation, client = None,
               km = 0, etat = 1) :
        self._marq = marque
        self._modl = modele
        self._imml = immatriculation
        self._km = km

        if etat < 0 or etat > 2 :
            self._etat = 0
        else :
            self._etat = etat

        if self._etat == 0 and client == None :
            raise ValueError("Client non précisé !")
        elif self._etat == 0 :
            self._client = client
        else :
            self._client = None


    def __str__(self) :
        if self._etat == 0 :
            return "{0} {1}({2}) \tkm = {3}\n\tlouée par {4}".format(self._marq,
                                    self._modl, self._imml, self._km, self._client)

        else :
            return "{0} {1}({2}) \tkm = {3}\n\t{4}".format(self._marq,
                                        self._modl, self._imml, self._km,
                                        ENUM_ETAT_LOCATION[self._etat])




if __name__ == "__main__" :
    v = Voiture("Cooper", "Mini", "AZ-804-TD")
    print(v)
    v._etat = 0
    v._client = "Erwan"
    print(v)