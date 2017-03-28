import sqlite3 as sql
import ihm.console as ihm


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
        ihm.afficher("Exécution de {0}".format(req))

    except sql.OperationalError : ihm.afficher("\tERREUR {0} non conforme".format(req))
    except sql.DataError : ihm.afficher("\tERREUR Données invalides")
    except sql.IntegrityError : ihm.afficher("\tERREUR Clé déjà existante ou fausse")


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