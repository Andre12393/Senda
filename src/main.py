import flet as ft
from views.sesion import sesion
from views.registro import registro
from views.dashboard import dashboard
from views.perfil import perfil
from views.materias import materias

def main(page: ft.Page):
    page.title = "Senda"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 350
    page.window.height = 650
    page.window.resizable = False
    page.window.maximizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    
    def route_change():
        page.views.clear()
        if page.route == "/sesion" or page.route == "/":
            page.views.append(sesion(page))
        
        elif page.route == "/registro":
            page.views.append(registro(page))
        
        elif page.route == "/dashboard":
            page.views.append(dashboard(page))
        
        elif page.route == "/perfil":
            page.views.append(perfil(page))
        
        elif page.route == "/materias":
            page.views.append(materias(page))
            
        page.update()

    page.on_route_change = lambda _: route_change()
    page.go("/materias")

ft.app(main)