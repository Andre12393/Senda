import flet as ft
from controllers.UsuarioCtrl import UsuarioCtrl

def sesion(page: ft.Page):
    email = ft.TextField(label="Correo Electronico", keyboard_type=ft.KeyboardType.EMAIL)
    alert_email = ft.Row(
        [
            ft.Icon(ft.Icons.ERROR_OUTLINE, size=12, color=ft.Colors.ERROR, margin=ft.Margin(top=2)),
            ft.Text("", size=12, color=ft.Colors.ERROR, expand=True)
        ],
        width=300,
        margin=ft.Margin(15, 2, bottom=5),
        visible=False
    )
    
    passw = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, margin=ft.Margin(top=10))
    alert_passw = ft.Row(
        [
            ft.Icon(ft.Icons.ERROR_OUTLINE, size=12, color=ft.Colors.ERROR, margin=ft.Margin(top=2)),
            ft.Text("", size=12, color=ft.Colors.ERROR, expand=True)
        ],
        width=300,
        margin=ft.Margin(15, 2),
        visible=False
    )
    
    def entrarClick():
        alert_email.visible = alert_passw.visible = False
        
        if not email.value:
            alert_email.controls[1].value = "Este campo es obligatorio" # type: ignore
            alert_email.visible = True
        
        if not passw.value:
            alert_passw.controls[1].value = "Este campo es obligatorio" # type: ignore
            alert_passw.visible = True
        
        if email.value and passw.value:
            is_valid, mensaje = UsuarioCtrl().iniciar_sesion(email.value, passw.value) # type: ignore
            if not is_valid:
                if "correo" in mensaje:
                    alert_email.controls[1].value = mensaje # type: ignore
                    alert_email.visible = True
                elif "contraseña" in mensaje:
                    alert_passw.controls[1].value = mensaje # type: ignore
                    alert_passw.visible = True
                else:
                    alert_email.controls[1].value = alert_passw.controls[1].value = mensaje # type: ignore
                    alert_email.visible = alert_passw.visible = True
            else:
                page.session.store.set("user", email.value)
                page.go("/perfil")
            
        page.update()
    
    return ft.View(
        route="/sesion",
        controls=[
            ft.Text("Iniciar Sesión", size=20, weight=ft.FontWeight.W_600, margin=ft.Margin(bottom=20)),
            email,
            alert_email,
            passw,
            alert_passw,
            ft.FilledButton(
                ft.Text("Entrar", size=16, weight=ft.FontWeight.W_700, color=ft.Colors.WHITE),
                bgcolor=ft.Colors.DEEP_ORANGE,
                width=300,
                style=ft.ButtonStyle(padding=15, shape=ft.RoundedRectangleBorder(radius=10)),
                margin=ft.Margin(top=30),
                on_click=lambda _: entrarClick()
            ),
            ft.TextButton(
                ft.Text("Crear una cuenta", size=16, weight=ft.FontWeight.W_600, color=ft.Colors.ON_SURFACE),
                width=300,
                style=ft.ButtonStyle(padding=15, shape=ft.RoundedRectangleBorder(radius=10)),
                margin=ft.Margin(top=5),
                on_click=lambda _: page.go("/registro")
            )
        ],
        margin=ft.Margin(3),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        spacing=0
    )