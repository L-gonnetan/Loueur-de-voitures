import sqlite3 as sql



def ouvrir_connexion(db_name) :
    """ Ouvrir une connexion vers une base de données

    ARG :
        + db_name [path] : Chemin de la base de données

    RETURN :
        - connexion vers la base de données
        - curseur de la base de données """

    conn = sql.connect(db_name)
    return conn, conn.cursor()


def executer_requete(cur, req, variables = ()) :
    """ Exécuter une requête avec des variables

    ARG :
        + cur [curseur] : Curseur de la base de données
        + req [requête] : Requête à exécuter

    EFFET : Mettre à jour le curseur

    EXCEPT :
        - Requête invalide
        - Données incompatibles avec la bdd
        - Clé déjà existante"""

    try :
        cur.execute(req, variables)
        print("Exécution de {0}".format(req))

    except sql.OperationalError : print("\tERREUR {0} non conforme".format(req))
    except sql.DataError : print("\tERREUR Données invalides")
    except sql.IntegrityError : print("\tERREUR Clé déjà existante ou fausse")


def valider_modifs(conn) :
    """ Exécuter une requête avec des variables

    ARG :
        + cur [curseur] : Curseur de la base de données
        + req [requête] : Requête à exécuter """

    conn.commit()


def fermer_connexion(cur, conn) :
    """ Fermeture de la connexion

    ARG :
        + cur [curseur] : curseur de la base de données
        + conn [connexion] : connexion vers la base de données """

    cur.close()
    conn.close()
