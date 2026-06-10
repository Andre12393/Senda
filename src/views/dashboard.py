import flet as ft
from controllers.UsuarioCtrl import UsuarioCtrl
from controllers.MateriaCtrl import MateriaCtrl
from views.components.materia import Materia

def dashboard(page: ft.Page):
    data = MateriaCtrl().obtener_data(page.session.store.get("user")) # type: ignore
    
    materias = ft.Column(
        [
            Materia(m.id, m.nombre, m.parcial_1, m.parcial_2, m.parcial_3, m.promedio, lambda e: eliminar_materia(e))
            for m in data # type: ignore
        ],
        height=600,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO
    )
    
    txt_eliminar = ft.Text("")
    alertSht_eliminar = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    txt_eliminar
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True
            ),
            padding=15
        ),
        shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(15, 15, 0, 0))
    )
    
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
    
    sheet_añadir = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(
                                "Añadir Materia",
                                size=20,
                                weight=ft.FontWeight.W_600,
                                align=ft.Alignment.CENTER,
                                expand=True,
                                margin=ft.Margin(right=50)
                            ),
                            ft.IconButton(
                                ft.Icons.CLOSE,
                                align=ft.Alignment.CENTER_RIGHT,
                                margin=ft.Margin(top=2),
                                on_click=lambda _: page.go("/dashboard")
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
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True
            ),
            padding=15
        ),
        shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(15, 15, 0, 0))
    )
    
    page.overlay.append(alertSht_eliminar)
    def eliminar_materia(e: ft.Event[ft.IconButton]):
        is_valid, mensaje = MateriaCtrl().eliminar(e.control.data)
        if not is_valid:
            txt_eliminar.value = mensaje
            alertSht_eliminar.open = True
            
        else:
            materias.controls = [
                Materia(m.id, m.nombre, m.parcial_1, m.parcial_2, m.parcial_3, m.promedio, lambda e: eliminar_materia(e))
                for m in MateriaCtrl().obtener(page.session.store.get("user")) # type: ignore
            ]
        
        page.update()
    
    def calcular_promedio():
        promedio.value = f"{((float(parcial_1.value) + float(parcial_2.value) + float(parcial_3.value)) / 3):g}"
        page.update()
    
    def guardarClick():
        return
    
    user = UsuarioCtrl().obtener_data(page.session.store.get("user"), "especialidad") # type: ignore
    
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
    
    promedio_general = 0.0
    for m in data: # type: ignore
        promedio_general += m.promedio
    promedio_general = (promedio_general / len(data)) if promedio_general != 0.0 else promedio_general # type: ignore
    
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
                bgcolor=ft.Colors.SURFACE_CONTAINER_LOW
            ),
            ft.Column(
                [
                    ft.Card(
                        ft.Stack(
                            [
                                ft.Icon(icono_perfil, size=125, color=ft.Colors.DEEP_ORANGE_50) 
                                if isinstance(icono_perfil, ft.IconData) else 
                                ft.Image(icono_perfil, width=125, color=ft.Colors.DEEP_ORANGE_50),
                                ft.Column(
                                    [
                                        ft.Text("Promedio General"),
                                        ft.Text(f"{float(promedio_general):g}")
                                    ]
                                )
                            ]
                        ),
                        bgcolor=ft.Colors.DEEP_ORANGE,
                        shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(15, 15, 15, 15))
                    ),
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Mi Senda"),
                                    ft.IconButton(ft.Icons.CHECKLIST_ROUNDED)
                                ]
                            ),
                            ft.Container(
                                materias,
                                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGH
                            ),
                            ft.ResponsiveRow(
                                [
                                    ft.FilledButton(
                                        icon=ft.Icon(ft.Icons.ADD, color=ft.Colors.WHITE),
                                        bgcolor=ft.Colors.DEEP_ORANGE,
                                        width=300,
                                        col=10
                                    ),
                                    ft.FilledButton(
                                        icon=ft.Icon(ft.Icons.PERSON),
                                        bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
                                        width=300,
                                        col=2
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        ],
        margin=ft.Margin(3),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        spacing=0
    )