import flet as ft

class FinUI:
    def __init__(self, page:ft.Page):
        self.page = page

        self.esque= ft.Container(
            bgcolor= "#222222",
            border_radius= 10,
            col = 4,
            padding= 10,
            content= ft.Column(
                controls=[
                    ft.Row( #caixa d'eines
                        controls= [
                            ft.TextButton(
                                text="Cargar",
                                icon=ft.Icons.SAVE,
                                icon_color= "white"
                            ),
                            ft.TextButton(
                                text="Guardar",
                                icon=ft.Icons.SAVE,
                                icon_color= "white"
                            )
                        ]
                    ),
                    ft.TextField(
                        bgcolor=ft.Colors.BLUE_900,
                        label= "Stockfish display",
                        height= 100,
                        width = 500
                    )
                ]
            )
        )

        self.dreta = ft.Container(
            bgcolor= "#222222",
            border_radius= 10,
            col = 8,
            content= ft.Column(
                controls= [
                    ft.TextField(
                        bgcolor=ft.Colors.RED,
                        label= "PGN display",
                        height= 100,
                        width = 500
                    ),
                    ft.TextField(
                        bgcolor=ft.Colors.BLUE_100,
                        label= "Info display",
                        height= 100,
                        width = 500
                    )
                ]
            )
        )

        self.conent= ft.ResponsiveRow(
                controls=[
                self.esque,
                self.dreta
            ],
            expand= True
        )


    def build(self):
        return self.conent



def main(page: ft.Page):
    page.title= "Exemple d'esquema tauler"
    page.bgcolor= "black"
    page.window_min_width= 1100
    page.window_min_height= 500
    form_instance = FinUI(page)
    page.add(form_instance.build())


if __name__ == '__main__':
    ft.app(main)
