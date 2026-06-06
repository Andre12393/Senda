import flet as ft
from controllers.UsuarioCtrl import UsuarioCtrl

def dashboard(page: ft.Page):
    user = UsuarioCtrl().obtener_data(page.session.store.get("user"), "nombres, especialidad")
    
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
            ft.Column()
        ]
    )