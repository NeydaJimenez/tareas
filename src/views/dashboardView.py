import flet as ft

def dashboardView(page, tarea_controller):
    user = page.session.get("user")

    # Tema azul claro
    page.bgcolor = ft.colors.BLUE_50
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLUE_300,
            secondary=ft.colors.LIGHT_BLUE_300
        )
    )

    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    def refresh():
        lista_tareas.controls.clear()
        for t in tarea_controller.obtener_lista(user['id_usuario']):
            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(t['titulo'], weight="bold"),
                            subtitle=ft.Text(f"{t['descripcion']}\nPrioridad: {t['prioridad']}"),
                            trailing=ft.Badge(
                                content=ft.Text(t['estado']),
                                bgcolor=ft.colors.BLUE_300
                            )
                        ), padding=10
                    )
                )
            )
        page.update()

    txt_titulo = ft.TextField(label="Nueva Tarea", expand=True)

    def add_task(e):
        success, msg = tarea_controller.guardar_nueva(
            user['id_usuario'], 
            txt_titulo.value, 
            "", 
            "media", 
            "trabajo"
        )
        if success:
            txt_titulo.value = ""
            refresh()

    return ft.View("/dashboard", [
        ft.AppBar(
            title=ft.Text(f"Bienvenido, {user['nombre']}"),
            bgcolor=ft.colors.BLUE_300,
            actions=[
                ft.IconButton(
                    ft.icons.EXIT_TO_APP,
                    icon_color=ft.colors.WHITE,
                    on_click=lambda _: page.go("/")
                )
            ],
        ),
        ft.Column([
            ft.Row([
                txt_titulo,
                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    bgcolor=ft.colors.BLUE_300,
                    foreground_color=ft.colors.WHITE,
                    on_click=add_task
                ),
            ]),
            ft.Divider(),
            ft.Text("Mis Tareas Pendientes", size=20, weight="bold"),
            lista_tareas
        ], expand=True, padding=20),
    ], on_open=lambda _: refresh())