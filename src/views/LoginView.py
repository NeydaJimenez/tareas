import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesión"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    usuario_valido = "admin"
    password_valido = "12345"

    correo = ft.TextField(
        label="Correo electrónico",
        width=280,
        border_color="pink200"
    )

    contraseña = ft.TextField(
        label="Introduzca su contraseña",
        password=True,
        can_reveal_password=True,
        width=280,
        border_color="pink100"
    )

    mensaje = ft.Text("", color="pink100")

    contenido = ft.Container()

    pagina_inicio = ft.Column(
        [
            ft.Text("Bienvenido al Sistema", size=28, weight=ft.FontWeight.BOLD, color="pink100"),
            ft.Text("Has iniciado sesión correctamente", color="pink100")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    pagina_explorar = ft.Column(
        [
            ft.Icon(ft.Icons.EXPLORE, size=60, color="pink100"),
            ft.Text("Explorar contenido", size=25, color="pink100")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    pagina_perfil = ft.Column(
        [
            ft.Icon(ft.Icons.PERSON, size=60, color="pink100"),
            ft.Text("Perfil del usuario", size=25, color="pink100"),
            ft.Text("admin@gmail.com", color="pink100")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    def cambiar_pagina(e):
        if e.control.selected_index == 0:
            contenido.content = pagina_inicio
        elif e.control.selected_index == 1:
            contenido.content = pagina_explorar
        elif e.control.selected_index == 2:
            contenido.content = pagina_perfil

        page.update()

    def login(e):

        if correo.value == "" or contraseña.value == "":
            mensaje.value = "Error: Debes llenar todos los campos"
            mensaje.color = "pink200"
            page.update()
            return

        if correo.value == usuario_valido and contraseña.value == password_valido:

            page.clean()

            contenido.content = pagina_inicio

            page.add(
                ft.Column(
                    [
                        contenido
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )

            page.navigation_bar = ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(
                        icon=ft.Icons.HOME,
                        label="Inicio"
                    ),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.EXPLORE,
                        label="Explorar"
                    ),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.PERSON,
                        label="Perfil"
                    ),
                ],
                on_change=cambiar_pagina
            )

            page.update()

        else:
            mensaje.value = "Correo o contraseña incorrectos"
            mensaje.color = "pink200"
            page.update()

    sesion = ft.Container(
        width=350,
        padding=30,
        border_radius=10,
        bgcolor="white",
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            controls=[
                ft.Text("Iniciar sesión", size=30, weight="bold", color="pink200"),
                correo,
                contraseña,
                ft.ElevatedButton(
                    content=ft.Text("Ingresar"),
                    width=200,
                    bgcolor="pink200",
                    color="white",
                    on_click=login
                ),
                mensaje,
                ft.TextButton(
                    content=ft.Text("¿Olvidaste tu contraseña?", color="pink200")
                )
            ]
        )
    )

    page.add(sesion)

ft.app(target=main)