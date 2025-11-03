import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab06"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        # Elementi UI
        self.txt_titolo = None
        self.txt_responsabile = None

        # Non obbligatorio mettere già qui tutti gli elementi UI

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        """ Imposta il controller alla pagina """
        self.controller = controller

    def update(self):
        print(" [DEBUG] Sto facendo update")
        self.page.update()


    def mostra_auto_clicked(self, e):
        #Una volta cliccato il pulsante mostra auto viene scatenata questa funzione che gestisce l'evento e
        #Questo evento deve rimandarmi al controller dopo creo e stampo una lista di automobili
        print("[DEBUG] mostra_automobili() chiamata")
        self.controller.mostra_automobili()

    def cerca_modello_clicked(self, e):
        #Una volta cliccato il pulsante mostra auto per modello
        #viene scatenata questa funzione che gestisce l'evento e
        #Questo evento deve rimandarmi al controller
        # dopo creo e stampo una lista di automobili ricercata per modello inserito dall'utente
        print("[DEBUG] è stato premuto il pulsante della ricerca per modello")
        self.controller.cerca_automobili_per_modello(self.input_modello_auto.value)  #devo passare il valore dell'input perchè è un textfield

    def load_interface(self):
        """ Crea e aggiunge Elementi di UI alla pagina e la aggiorna. """
        self.txt_titolo = ft.Text(value=self.controller.get_nome(), size=38, weight=ft.FontWeight.BOLD)
        self.txt_responsabile = ft.Text(
            value=f"Responsabile: {self.controller.get_responsabile()}",
            size=16,
            weight=ft.FontWeight.BOLD
        )

        # TextField per responsabile
        self.input_responsabile = ft.TextField(value=self.controller.get_responsabile(), label="Responsabile")

        # ListView per mostrare la lista di auto aggiornata
        self.lista_auto = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # TextField per ricerca auto per modello
        self.input_modello_auto = ft.TextField(label="Modello")

        # ListView per mostrare il risultato della ricerca auto per modello
        self.lista_auto_ricerca = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # --- PULSANTI e TOGGLE associati a EVENTI ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)
        pulsante_conferma_responsabile = ft.ElevatedButton("Conferma", on_click=self.controller.conferma_responsabile)

        # Altri Pulsanti da implementare (es. "Mostra" e "Cerca")
        #questo pulsante richiama una funzione prensente nel controller
        """pulsante_mostra_auto = ft.ElevatedButton("Automobili", on_click=self.controller.mostra_automobili(self.lista_auto))
        pulsante_cerca_per_modello= ft.ElevatedButton("Cerca", on_click=self.controller.cerca_automobili_per_modello(self.lista_auto_ricerca, self.input_modello_auto))"""

        pulsante_mostra_auto = ft.ElevatedButton("Mostra Automobili", on_click=self.mostra_auto_clicked)
        pulsante_cerca_per_modello = ft.ElevatedButton("Cerca", on_click=self.cerca_modello_clicked)

        # --- LAYOUT ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            self.txt_responsabile,
            ft.Divider(),

            # Sezione 2
            ft.Text("Modifica Informazioni", size=20),
            ft.Row(spacing=200,
                   controls=[self.input_responsabile, pulsante_conferma_responsabile],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3
            ft.Text(value="Automobili", size=20),
            ft.Row(spacing=200,
                   controls=[pulsante_mostra_auto],
                   alignment=ft.MainAxisAlignment.CENTER),
            self.lista_auto,
            ft.Divider(),

            # Sezione 4
            ft.Text(value="Cerca Automobile", size=20),
            ft.Row(spacing=200,
                   controls=[self.input_modello_auto, pulsante_cerca_per_modello],
                   alignment=ft.MainAxisAlignment.CENTER),
            self.lista_auto_ricerca,
        )

    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
