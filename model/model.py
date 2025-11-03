import mysql
from httpx import options

import database
from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self):
        """Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None """

        #Faccio la connessione con il DATABASE
        #Se la connessione è andata a buon fine, allora eseguo una query che i prende le automobili del db,
        # li converto in oggetti Python della classe Automobili e poi aggiungo ogni oggetto alla lista
        print("[DEBUG] Sto per fare la connection")
        cnx = get_connection()
        print("[DEBUG] Ho fatto la connessione con il database")
        lista_automobili = []

        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)   #prendo i dati considerando i vari campi all'interno di una riga come per un dizionario
            cursor.execute("SELECT * FROM automobili")
            for row in cursor:
                lista_automobili.append(Automobile(codice=row["codice"],
                                                   marca=row["marca"],
                                                   modello=row["modello"],
                                                   anno=row["anno"],
                                                   posti=row["posti"],
                                                   disponibile=row["disponibile"]))

            cursor.close()
            cnx.close()
            return lista_automobili #questa lista viene passata al controller
        else:
            print("Nessuna connessione con il database")
            return None


    def cerca_automobili_per_modello(self, modello):
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # STESSA LOGICA DI QUELLO DI PRIMA DELLA FUNZIONE GET_AUTOMOBILI
        cnx = get_connection()
        lista_automobili_modello = []
        if cnx is not None:
            try:
                cursor = cnx.cursor(dictionary=True)
                query = "SELECT * FROM automobili WHERE modello = %s"
                cursor.execute(query, (modello,))

                for row in cursor:
                    lista_automobili_modello.append(Automobile(
                        codice=row["codice"],
                        marca=row["marca"],
                        modello=row["modello"],
                        anno=row["anno"],
                        posti=row["posti"],
                        disponibile=row["disponibile"]
                    ))
                cursor.close()
                cnx.close()
                return lista_automobili_modello

            except Exception as e:
                print("Errore durante la lettura delle automobili:", e)
                return None

        else:
            print("Nessuna connessione con il database.")
            return None