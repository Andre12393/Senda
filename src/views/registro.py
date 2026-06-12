import flet as ft
from controllers.UsuarioCtrl import UsuarioCtrl

def registro(page: ft.Page):
    nombres = ft.TextField(label="Nombre Completo")
    alert_nombres = ft.Row(
        [
            ft.Icon(ft.Icons.ERROR_OUTLINE, size=12, color=ft.Colors.ERROR, margin=ft.Margin(top=2)),
            ft.Text("", size=12, color=ft.Colors.ERROR, expand=True)
        ],
        width=300,
        margin=ft.Margin(15, 2, bottom=5),
        visible=False
    )
    
    apellidos = ft.TextField(label="Apellidos", margin=ft.Margin(top=10))
    alert_apellidos = ft.Row(
        [
            ft.Icon(ft.Icons.ERROR_OUTLINE, size=12, color=ft.Colors.ERROR, margin=ft.Margin(top=2)),
            ft.Text("", size=12, color=ft.Colors.ERROR, expand=True)
        ],
        width=300,
        margin=ft.Margin(15, 2, bottom=5),
        visible=False
    )
    
    especialidad = ft.Dropdown(
        label="Especialidad",
        options=[
            ft.DropdownOption("programacion", "Programación"),
            ft.DropdownOption("electronica", "Electrónica"),
            ft.DropdownOption("contabilidad", "Contabilidad"),
            ft.DropdownOption("electricidad", "Electricidad")
        ],
        editable=True,
        width=300,
        margin=ft.Margin(top=10)
    )
    
    alert_especialidad = ft.Row(
        [
            ft.Icon(ft.Icons.ERROR_OUTLINE, size=12, color=ft.Colors.ERROR, margin=ft.Margin(top=2)),
            ft.Text("", size=12, color=ft.Colors.ERROR, expand=True)
        ],
        width=300,
        margin=ft.Margin(15, 2, bottom=5),
        visible=False
    )
    
    email = ft.TextField(label="Correo Electrónico", keyboard_type=ft.KeyboardType.EMAIL, margin=ft.Margin(top=10))
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
        margin=ft.Margin(15, 2, bottom=5),
        visible=False
    )
    
    def registrateClick():
        alert_nombres.visible = alert_apellidos.visible = alert_especialidad.visible = alert_email.visible = alert_passw.visible = False
        
        if not nombres.value:
            alert_nombres.controls[1].value = "Este campo es obligatorio" # type: ignore
            alert_nombres.visible = True
            
        if not apellidos.value:
            alert_apellidos.controls[1].value = "Este campo es obligatorio" # type: ignore
            alert_apellidos.visible = True
            
        if not especialidad.value:
            alert_especialidad.controls[1].value = "Este campo es obligatorio" # type: ignore
            alert_especialidad.visible = True
            
        if not email.value:
            alert_email.controls[1].value = "Este campo es obligatorio" # type: ignore
            alert_email.visible = True
        
        if not passw.value:
            alert_passw.controls[1].value = "Este campo es obligatorio" # type: ignore
            alert_passw.visible = True
        
        if nombres.value and apellidos.value and especialidad.value and email.value and passw.value:
            is_valid, mensaje = UsuarioCtrl().registrar(nombres.value, apellidos.value, especialidad.value, email.value, passw.value) # type: ignore
            
            if not is_valid:
                if "nombre" in mensaje:
                    alert_nombres.controls[1].value = mensaje # type: ignore
                    alert_nombres.visible = True
                    
                elif "apellidos" in mensaje:
                    alert_apellidos.controls[1].value = mensaje # type: ignore
                    alert_apellidos.visible = True
                    
                elif "especialidad" in mensaje:
                    alert_especialidad.controls[1].value = mensaje # type: ignore
                    alert_especialidad.visible = True
                    
                elif "correo" in mensaje:
                    alert_email.controls[1].value = mensaje # type: ignore
                    alert_email.visible = True
                    
                elif "contraseña" in mensaje:
                    alert_passw.controls[1].value = mensaje # type: ignore
                    alert_passw.visible = True
            
            else:
                page.go("/sesion")
            
        page.update()
    
    return ft.View(
        route="/registro",
        controls=[
            ft.Text("Registrate", size=20, weight=ft.FontWeight.W_600, margin=ft.Margin(bottom=20)),
            nombres,
            alert_nombres,
            apellidos,
            alert_apellidos,
            especialidad,
            alert_especialidad,
            email,
            alert_email,
            passw,
            alert_passw,
            ft.FilledButton(
                ft.Text("Registrarme", size=16, weight=ft.FontWeight.W_600, color=ft.Colors.WHITE),
                bgcolor=ft.Colors.DEEP_ORANGE,
                width=300,
                style=ft.ButtonStyle(padding=15, shape=ft.RoundedRectangleBorder(radius=10)),
                margin=ft.Margin(top=28),
                on_click=lambda _: registrateClick()
            ),
            ft.TextButton(
                ft.Text("Ya tengo una cuenta", size=16, weight=ft.FontWeight.W_600, color=ft.Colors.ON_SURFACE),
                width=300,
                style=ft.ButtonStyle(padding=15, shape=ft.RoundedRectangleBorder(radius=10)),
                margin=ft.Margin(top=5),
                on_click=lambda _: page.go("/sesion")
            )
        ],
        margin=ft.Margin(3),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        spacing=0
    )