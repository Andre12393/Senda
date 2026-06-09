import flet as ft
from controllers.UsuarioCtrl import UsuarioCtrl

def dashboard(page: ft.Page):
    materias = ft.Column(
        []
    )
    
    user = UsuarioCtrl().obtener_data(page.session.store.get("user"), "nombres, especialidad") # type: ignore
    
    icono_perfil: ft.IconData | str
    if user:
        if user["especialidad"] == "programacion":
            icono_perfil = "assets/icons/code_xml.svg"
            
        elif user["especialidad"] == "electronica":
            icono_perfil = ft.Icons.MEMORY_ROUNDED
            
        elif user["especialidad"] == "contabilidad":
            icono_perfil = ft.Icons.BALANCE_ROUNDED
            
        elif user["especialidad"] == "electricidad":
            icono_perfil = ft.Icons.ELECTRIC_BOLT_ROUNDED
    
    nombre_usuario = ("Usuario" if not user else user["nombres"]).title()
    
    return ft.View(
        route="/dashboard",
        controls=[
            ft.AppBar(
                title=ft.Text(
                    spans=[
                        ft.TextSpan("S", ft.TextStyle(size=30, color=ft.Colors.DEEP_ORANGE, weight=ft.FontWeight.BOLD)),
                        ft.TextSpan("enda", ft.TextStyle(size=25, weight=ft.FontWeight.W_500))
                    ]
                ),
                center_title=True,
                shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(15, 15, 15, 15)),
                bgcolor=ft.Colors.SURFACE
            ),
            ft.Stack(
                [
                    ft.Column(
                        [
                            ft.Column(
                                [
                                    ft.Text(),
                                    ft.Stack(
                                        [
                                            ft.Icon(icono_perfil, size=125, color=ft.Colors.SURFACE) 
                                            if isinstance(icono_perfil, ft.IconData) else 
                                            ft.Image(icono_perfil, width=125, color=ft.Colors.SURFACE),
                                            ft.Text()
                                        ]
                                    ),
                                    ft.Text()
                                ]
                            ),
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Text(),
                                            ft.IconButton()
                                        ]
                                    ),
                                    materias
                                ]
                            )
                        ]
                    ),
                    ft.Row(
                        [
                            ft.FloatingActionButton(),
                            ft.FloatingActionButton()
                        ]
                    )
                ]
            )
        ]
    )