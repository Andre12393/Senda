import flet as ft
from controllers.UsuarioCtrl import UsuarioCtrl

def dashboard(page: ft.Page):
    # user = UsuarioCtrl().obtener_data(page.session.store.get("user"), "nombre")
    # nombre_usuario = "Usuario" if not user else user["nombre"] # type: ignore
    # nombre_usuario = nombre_usuario if len(nombre_usuario) <= 10 else nombre_usuario[:7] + "..."
    
    return ft.View(
        route="/dashboard",
        controls=[
            ft.AppBar(
                ft.Text("S", color=ft.Colors.DEEP_ORANGE),
                title="enda",
                bgcolor=ft.Colors.SURFACE_CONTAINER
            ),
            ft.Column()
        ],
        bgcolor=ft.Colors.SURFACE_CONTAINER_LOWEST
    )