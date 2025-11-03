import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    """Il controller mi permette di far interagire il Model (preleva i dati dal database) 
    con la view (interfaccia utente)"""

    def mostra_automobili(self):
        #Idea: devo richiamare una funzione del model che mi restituisca una lista di oggetti Automobile
        print("[DEBUG] sono dentro mostra_automobili nel controller")
        lista_automobili = self._model.get_automobili()
        #lista_auto è un oggetto di tipo flet List View
        self._view.lista_auto.controls.clear() #pulisca la List View
        if lista_automobili is None:
            self._view.show_alert("Errore nel recupero delle automobili.")
        else:
            for auto in lista_automobili:
                print("[DEBUG]: Sono dentro il for per stampare le automobili")
                self._view.lista_auto.controls.append(ft.Text(str(auto))) #Aggiungo le auto dentro la list view
            self._view.update() #aggiorno la pagina
        #NOTA: convertire l'oggetto Auto in una stringa.
        #      Aggiungo alla lista view un elemento ft.Text


    def cerca_automobili_per_modello(self, input_modello_auto):
        print("[DEBUG] Sono nel controller nella fz cerca automobili per modello")
        # pulisco la lista prima di riempirla (altrimenti abbiamo visto a lezione si fa un append)
        self._view.lista_auto_ricerca.controls.clear()

        # recupero le auto dal model (passando il testo del campo)
        lista_ricercata = self._model.cerca_automobili_per_modello(input_modello_auto)

        if lista_ricercata is None or len(lista_ricercata) == 0:
            self._view.show_alert("Nessuna automobile trovata per questo modello.")
        else:
            for auto in lista_ricercata:
                    self._view.lista_auto_ricerca.controls.append(ft.Text(str(auto))) #ricordando che lista ricercata è una lista di oggetti auto
        self._view.update()

