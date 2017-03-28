ENUM_ETAT_LOCATION = ["louée", "disponible", "au garage"]


class Voiture(object) :
    def __init__(self, marque, modle, immatriculation, client = None,
               km = 0, etat = 0) :
        self.marq = marque
        self.modl = modele
        self.imml = immatriculation
        self.km = km

        if etat < 0 or etat > 2 :
            self.etat = 0
        else :
            self.etat = etat

        if self.etat == 0 and client == None :
            raise ValueError("Client non précisé !")
        elif self.etat == 0 :
            self.client = client
        else :
            self.client = None


    def __str__(self) :
        if self.etat == 0 :
            return "{0}[{1} {2}](km {3}) louée par {4}".format(self.imml,
                            self.marq, self.modl, self.kmn, self.client)

        else :
            return "{0}[{1} {2}](km {3}) {4}".format(self.imml,
                                self.marq, self.modl, self.kmn,
                                ENUM_ETAT_LOCATION[self.etat])
