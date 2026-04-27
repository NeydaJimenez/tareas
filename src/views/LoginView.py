import flet as ft

def main(page: ft.Page):
    page.title = "INICIO DE SESION"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    usuario_valido = "admin"
    password_valido = "12345"

    correo = ft.TextField(
        label="Correo electrónico",
        width=280,
        border_color="blue200"
    )

    contraseña = ft.TextField(
        label="Introduzca su contraseña",
        password=True,
        can_reveal_password=True,
        width=280,
        border_color="blue200"
    )

    mensaje = ft.Text("", color="blue200")

    contenido = ft.Container()

    pagina_inicio = ft.Column(
        [
            ft.Text("Bienvenido al Sistema", size=28, weight=ft.FontWeight.BOLD, color="blue200"),
            ft.Text("Has Iniciado Sesión Correctamente", color="blue200")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    pagina_explorar = ft.Column(
        [
            ft.Icon(ft.Icons.EXPLORE, size=60, color="blue200"),
            ft.Text("Explorar Contenido", size=25, color="blue200")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    pagina_perfil = ft.Column(
        [
            ft.Icon(ft.Icons.PERSON, size=60, color="blue200"),
            ft.Text("Perfil del usuario", size=25, color="blue200"),
            ft.Text("admin@gmail.com", color="blue200")
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
            mensaje.color = "blue200"
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
            mensaje.color = "blue200"
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
                ft.Text("INICIO DE SESION", size=30, weight="bold", color="blue200"),
                correo,
                contraseña,
                ft.ElevatedButton(
                    content=ft.Text("Ingresar"),
                    width=200,
                    bgcolor="blue200",
                    color="white",
                    on_click=login
                ),
                mensaje,
                ft.TextButton(
                    content=ft.Text("¿Olvidaste tu contraseña?", color="blue200")
                )
            ]
        )
    )

    page.add(sesion)

ft.app(target=main)