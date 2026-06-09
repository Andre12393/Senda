import flet as ft
from controllers.MateriaCtrl import MateriaCtrl

def materias(page: ft.Page):
    nombre = ft.TextField(label="Nombre de la Materia", width=300)
    alert_nombre = ft.Row(
        [
            ft.Icon(ft.Icons.ERROR_OUTLINE, size=12, color=ft.Colors.ERROR, margin=ft.Margin(top=2)),
            ft.Text("", size=12, color=ft.Colors.ERROR, expand=True)
        ],
        width=300,
        margin=ft.Margin(15, 2, bottom=5),
        visible=False
    )
    
    parcial_1 = ft.TextField(
        label="Parcial 1",
        width=75,
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=lambda _: calcular_promedio()
    )

    parcial_2 = ft.TextField(
        label="Parcial 2",
        width=75,
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=lambda _: calcular_promedio()
    )

    parcial_3 = ft.TextField(
        label="Parcial 3",
        width=75,
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=lambda _: calcular_promedio()
    )
    
    alert_parcial = ft.Row(
        [
            ft.Icon(ft.Icons.ERROR_OUTLINE, size=12, color=ft.Colors.ERROR, margin=ft.Margin(top=2)),
            ft.Text("", size=12, color=ft.Colors.ERROR, expand=True)
        ],
        width=300,
        margin=ft.Margin(15, 2, bottom=5),
        visible=False
    )

    promedio = ft.Text("0", size=20, weight=ft.FontWeight.W_600, align=ft.Alignment.CENTER)
    
    def calcular_promedio():
        promedio.value = f"{((float(parcial_1.value) + float(parcial_2.value) + float(parcial_3.value)) / 3):g}"
        page.update()
    
    def guardarClick():
        return
    
    return ft.View(
        route="/materias",
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
                        "Añadir Materia",
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
            ft.Column(
                [
                    nombre,
                    alert_nombre,
                    ft.Row(
                        [parcial_1, parcial_2, parcial_3]
                    ),
                    alert_parcial,
                    promedio,
                    ft.FilledButton(
                        "Guardar",
                        width=300,
                        on_click=lambda _: guardarClick()
                    )
                ]
            )
        ],
        margin=ft.Margin(3),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        spacing=0
    )