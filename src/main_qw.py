import flet as ft


def main(page: ft.Page):
    page.title = "Tablero de Ajedrez y Análisis"
    page.window_width = 820  # Ancho de la ventana
    page.window_height = 620 # Alto de la ventana
    page.padding = 10      # Espacio alrededor del contenido
    
    # menubar
    appbar_text_ref = ft.Ref[ft.Text]()
    
    page.appbar = ft.AppBar(
        title=ft.Text("Menus", ref=appbar_text_ref),
        center_title=True,
        bgcolor=ft.Colors.BLUE,
    )

	menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.Colors.RED_300,
            mouse_cursor={
                ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
            },
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("File"),
                on_open=handle_submenu_open,
                on_close=handle_submenu_close,
                on_hover=handle_submenu_hover,
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("About"),
                        leading=ft.Icon(ft.Icons.INFO),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=handle_menu_item_click,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Save"),
                        leading=ft.Icon(ft.Icons.SAVE),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=handle_menu_item_click,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Quit"),
                        leading=ft.Icon(ft.Icons.CLOSE),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=handle_menu_item_click,
                    ),
                ],
            ),
            ft.SubmenuButton(
                content=ft.Text("View"),
                on_open=handle_submenu_open,
                on_close=handle_submenu_close,
                on_hover=handle_submenu_hover,
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("Zoom"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Magnify"),
                                leading=ft.Icon(ft.Icons.ZOOM_IN),
                                close_on_click=False,
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.HOVERED: ft.Colors.PURPLE_200
                                    }
                                ),
                                on_click=handle_menu_item_click,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Minify"),
                                leading=ft.Icon(ft.Icons.ZOOM_OUT),
                                close_on_click=False,
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.HOVERED: ft.Colors.PURPLE_200
                                    }
                                ),
                                on_click=handle_menu_item_click,
                            ),
                        ],
                    )
                ],
            ),
        ],
    )
    
    # funcions del menu
    
    def handle_menu_item_click(e):
        print(f"{e.control.content.value}.on_click")
        page.open(ft.SnackBar(content=ft.Text(f"{e.control.content.value} was clicked!")))
        appbar_text_ref.current.value = e.control.content.value
        page.update()

    def handle_submenu_open(e):
        print(f"{e.control.content.value}.on_open")

    def handle_submenu_close(e):
        print(f"{e.control.content.value}.on_close")

    def handle_submenu_hover(e):
        print(f"{e.control.content.value}.on_hover")



    # --- Funciones Auxiliares (NUEVO) ---

    def get_piece_image(row, col):
        """Devuelve la ruta de la imagen para una casilla, o None si no hay pieza."""

        # Ejemplo simple:  Rey blanco en A1, peón negro en A7
        if row == 0 and col == 0:
            return "../assets/pieces/bk.png"  # Ruta relativa a tu imagen
        elif row == 3 and col == 4:
            return "../assets/pieces/wp.png"
        elif row == 6 and col == 0:
            return "../assets/pieces/wk.png"
        # ... Agrega más lógica aquí para otras piezas ...
        return None  # Si no hay pieza en esta casilla


    # --- Columna Izquierda (Tablero y Área de Análisis) ---

    # 1. Tablero de Ajedrez
    tablero = ft.Column(
        controls=[],
        spacing=0,  # Sin espacio entre las filas del tablero
        width=400,    #ancho del tablero
        height = 400   #alto del tablero
    )

    # Crear las 8 filas del tablero
    for fila in range(8):
        fila_controles = []
        for columna in range(8):
            # Alternar colores:  (fila + columna) par = blanco, impar = negro
            color = ft.Colors.BLUE_100 if (fila + columna) % 2 == 0 else ft.Colors.BLUE_900
            
            # --- Obtener la imagen (si hay) ---
            image_path = get_piece_image(fila, columna)
            
            # --- Crear la casilla ---
            if image_path:
                # Casilla CON imagen
                casilla = ft.Container(
                    content=ft.Image(
                        src=image_path,
                        width=50,  # Asegúrate de que el tamaño coincida con la casilla
                        height=50,
                        fit=ft.ImageFit.CONTAIN,  # Centrar y mantener proporciones
                    ),
                    width=50,
                    height=50,
                    bgcolor=color,
                    border=ft.border.all(1, ft.Colors.BLACK),
                    alignment=ft.alignment.center,  # Centrar la imagen *dentro* del contenedor
                )
            else:
                # Casilla SIN imagen (vacía)
                casilla = ft.Container(
                    width=50,
                    height=50,
                    bgcolor=color,
                    border=ft.border.all(1, ft.Colors.BLACK),
                )
            fila_controles.append(casilla)
        # Añadir la fila completa al tablero
        tablero.controls.append(ft.Row(controls=fila_controles, spacing=0))


    # 2. Área de Análisis 1
    area_analisis_1 = ft.Container(
        content=ft.Text("Área de Análisis 1", size=16, color=ft.Colors.WHITE), #Texto en blanco
        bgcolor=ft.Colors.BLUE_GREY_700,
        padding=10,
        border_radius=5,
        alignment=ft.alignment.top_left, #alineacion centrada
        height = 100,   #Ancho del recuadro de analisis
        width = 400
    )
    
    # 2. Área de Análisis 2
    area_analisis_2 = ft.Container(
        content=ft.Text("Área de Análisis 2", size=16, color=ft.Colors.WHITE), #Texto en blanco
        bgcolor=ft.Colors.BLUE_GREY_700,
        padding=10,
        border_radius=5,
        alignment=ft.alignment.top_left, #alineacion centrada
        height = 100,   #Ancho del recuadro de analisis
        width = 400
    )

    # Contenedor principal de la columna izquierda
    columna_izquierda = ft.Column(
        controls=[tablero, area_analisis_1, area_analisis_2],
        spacing=10, # Separación vertical entre tablero y área de análisis
    )


    # --- Columna Derecha (Recuadros de Texto) ---
    recuadro_azul = ft.Container(
        content=ft.Text("Texto Azul", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE,
        padding=10,
        border_radius=5,
        height = 200,
        width = 400
    )

    recuadro_verde = ft.Container(
        content=ft.Text("Texto Verde", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.GREEN,
        padding=10,
        border_radius=5,
        height = 200,
        width= 400
    )

    recuadro_rojo = ft.Container(
        content=ft.Text("Texto Rojo", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.RED,
        padding=10,
        border_radius=5,
        height = 200,
        width= 400
    )
    columna_derecha = ft.Column(
        controls=[recuadro_azul, recuadro_verde, recuadro_rojo],
        spacing=10,  # Separación entre los recuadros
        width = 400
    )

    # --- Contenedor Principal (Row) ---
    contenido_principal = ft.Row(
        controls=[columna_izquierda, columna_derecha],
        spacing=10,         # Separación entre las columnas
        alignment=ft.MainAxisAlignment.SPACE_AROUND  #Distribucion uniforme
    )

	page.add(ft.Row([menubar]))
    page.add(contenido_principal)


if __name__ == "__main__":
    ft.app(target=main)
