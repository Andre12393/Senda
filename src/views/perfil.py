import flet as ft
from controllers.UsuarioCtrl import UsuarioCtrl

def perfil(page: ft.Page):
    alert_eliminar = ft.Row(
        [
            ft.Icon(ft.Icons.ERROR_OUTLINE, size=12, color=ft.Colors.ERROR, margin=ft.Margin(top=2)),
            ft.Text("", size=12, color=ft.Colors.ERROR, expand=True)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        margin=ft.Margin(15, bottom=2),
        visible=False
    )
    
    sheet_eliminar = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.IconButton(ft.Icons.CLOSE_ROUNDED, align=ft.Alignment.TOP_RIGHT, on_click=lambda _: cerrar_alertD()),
                    ft.Container(
                        ft.Column(
                            [
                                ft.Text(
                                    "¿Estas seguro de que quieres eliminar tu cuenta?",
                                    size=15,
                                    text_align=ft.TextAlign.CENTER,
                                    margin=ft.Margin(bottom=25, top=5)
                                ),
                                alert_eliminar,
                                ft.FilledButton(
                                    ft.Text("Eliminar mi cuenta", size=20, color=ft.Colors.WHITE, weight=ft.FontWeight.W_600),
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=15),
                                    bgcolor=ft.Colors.RED,
                                    width=300,
                                    margin=ft.Margin(bottom=10),
                                    on_click=lambda _: eliminar_cuenta(page.session.store.get("user")) # type: ignore
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                        ),
                        padding=ft.Padding(15, 0, 15, 0)
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                tight=True
            ),
            padding=5
        ),
        bgcolor=ft.Colors.SURFACE,
        shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(20, 20, 0, 0))
    )
    
    page.overlay.append(sheet_eliminar)
    def abrir_alertD():
        sheet_eliminar.open = True
        page.update()
    
    def cerrar_alertD():
        sheet_eliminar.open = False
        page.update()
    
    def cerrar_sesionClick():
        page.session.store.clear()
        page.go("/sesion")
    
    def eliminar_cuenta(email: str):
        alert_eliminar.visible = False
        
        is_valid, mensaje = UsuarioCtrl().eliminar_cuenta(email)
        if not is_valid:
            alert_eliminar.controls[1].value = mensaje # type: ignore
            alert_eliminar.visible = True
        else:
            page.go("/sesion")
        
        page.update()
    
    
    user = UsuarioCtrl().obtener_data(page.session.store.get("user"), "nombres, apellidos, especialidad") # type: ignore
    
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
    
    nombre_usuario = ("Usuario" if not user else f"{user["nombres"]} {user["apellidos"]}").title()
    
    return ft.View(
        route="/perfil",
        controls=[
            ft.Row(
                [
                    ft.IconButton(
                        ft.Icons.ARROW_BACK,
                        align=ft.Alignment.CENTER_LEFT,
                        margin=ft.Margin(top=2),
                        on_click=lambda _: page.go("/dashboard")
                    ),
                    ft.Text(
                        "Perfil",
                        size=20,
                        weight=ft.FontWeight.W_600,
                        align=ft.Alignment.CENTER,
                        expand=True,
                        margin=ft.Margin(right=50)
                    )
                ],
                margin=ft.Margin(bottom=5)
            ),
            ft.Divider(),
            ft.Container(
                ft.Icon(icono_perfil, size=125, color=ft.Colors.SURFACE) 
                if isinstance(icono_perfil, ft.IconData) else 
                ft.Image(icono_perfil, width=125, color=ft.Colors.SURFACE),
                bgcolor=ft.Colors.SURFACE_CONTAINER,
                shape=ft.BoxShape.CIRCLE,
                margin=ft.Margin(top=25),
                padding=20
            ),
            ft.Text(
                nombre_usuario,
                size=25,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.W_600,
                margin=ft.Margin(top=15),
                expand=True
            ),
            ft.TextButton(
                ft.Text("Cerrar sesion", size=20, color=ft.Colors.RED, weight=ft.FontWeight.W_600),
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=15),
                width=300,
                margin=ft.Margin(bottom=10),
                on_click=lambda _: cerrar_sesionClick()
            ),
            ft.FilledButton(
                ft.Text("Eliminar cuenta", size=20, color=ft.Colors.WHITE, weight=ft.FontWeight.W_600),
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=15),
                bgcolor=ft.Colors.RED,
                width=300,
                margin=ft.Margin(bottom=8),
                align=ft.Alignment.BOTTOM_CENTER,
                on_click=lambda _: abrir_alertD()
            )
        ],
        margin=ft.Margin(3),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        spacing=0
    )