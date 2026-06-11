import flet as ft
from controllers.UsuarioCtrl import UsuarioCtrl
from controllers.MateriaCtrl import MateriaCtrl
from views.components.materia import Materia

def dashboard(page: ft.Page):
    btn_modo = ft.IconButton(
        ft.Icons.CHECKLIST_ROUNDED,
        data="lec",
        align=ft.Alignment.CENTER_RIGHT,
        on_click=lambda e: cambiar_modo(e)
    )
    
    materias = ft.Column(
        [
            Materia(
                m["id"],
                m["nombre"],
                m["parcial_1"],
                m["parcial_2"],
                m["parcial_3"],
                m["promedio"],
                lambda e: eliminar_materia(e)
            ) for m in MateriaCtrl().obtener_data(page.session.store.get("user")) # type: ignore
        ],
        height=300,
        margin=ft.Margin(1, 2, 1, 2),
        spacing=5,
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
        label="P1",
        width=93,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    parcial_2 = ft.TextField(
        label="P2",
        width=93,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    parcial_3 = ft.TextField(
        label="P3",
        width=93,
        keyboard_type=ft.KeyboardType.NUMBER
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
    
    alert_añadir = ft.Row(
        [
            ft.Icon(ft.Icons.ERROR_OUTLINE, size=12, color=ft.Colors.ERROR, margin=ft.Margin(top=2)),
            ft.Text("", size=12, color=ft.Colors.ERROR, expand=True)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        margin=ft.Margin(15, bottom=2),
        visible=False
    )
    
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
                                on_click=lambda _: cerrar_shtAñadir()
                            )
                        ],
                        margin=ft.Margin(bottom=5)
                    ),
                    ft.Column(
                        [
                            nombre,
                            alert_nombre,
                            ft.Row(
                                [parcial_1, parcial_2, parcial_3]
                            ),
                            alert_parcial,
                            alert_añadir,
                            ft.FilledButton(
                                "Añadir Materia",
                                width=300,
                                on_click=lambda _: añadir_materia()
                            )
                        ]
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                tight=True
            ),
            padding=5
        ),
        bgcolor=ft.Colors.SURFACE,
        shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(15, 15, 0, 0)),
        dismissible=False
    )
    
    btn_añadir = ft.IconButton(
        ft.Icons.ADD_ROUNDED,
        ft.Colors.WHITE,
        35,
        bgcolor=ft.Colors.DEEP_ORANGE,
        width=325,
        on_click=lambda _: abrir_shtAñadir()
    )
    
    btn_vaciar = ft.FilledButton(
        ft.Text("Vaciar materias", size=25, color=ft.Colors.WHITE),
        style=ft.ButtonStyle(bgcolor=ft.Colors.RED, padding=15),
        width=325,
        on_click=lambda _: abrir_shtEliminar(),
        visible=False
    )
    
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
                    ft.Text(
                        "¿Estas seguro de que quieres vaciar todas tus materias?",
                        size=15,
                        text_align=ft.TextAlign.CENTER,
                        margin=ft.Margin(bottom=25, top=15)
                    ),
                    alert_eliminar,
                    ft.FilledButton(
                        ft.Text("Vaciar mis materias", size=20, color=ft.Colors.WHITE, weight=ft.FontWeight.W_600),
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=15),
                        bgcolor=ft.Colors.RED,
                        width=300,
                        margin=ft.Margin(bottom=10),
                        on_click=lambda _: vaciar_materias()
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                tight=True
            ),
            padding=5
        ),
        bgcolor=ft.Colors.SURFACE,
        shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(20, 20, 0, 0))
    )
    
    def cambiar_modo(e: ft.Event[ft.IconButton]):
        if e.control.data == "del":
            Materia.modo_eliminar = btn_vaciar.visible = False
            btn_añadir.visible = True
            e.control.icon = ft.Icons.CHECKLIST_ROUNDED
            e.control.data = "lec"
            
        elif e.control.data == "lec":
            Materia.modo_eliminar = btn_vaciar.visible = True
            btn_añadir.visible = False
            e.control.icon = ft.Icons.CHECK_ROUNDED
            e.control.data = "del"
            
        for materia in materias.controls:
            materia.actualizar() # type: ignore
        
        page.update()
    
    page.overlay.append(alertSht_eliminar)
    def eliminar_materia(e: ft.Event[ft.IconButton]):
        is_valid, mensaje = MateriaCtrl().eliminar_materia(e.control.data)
        
        if not is_valid:
            txt_eliminar.value = mensaje
            alertSht_eliminar.open = True
        else:
            actualizar_materias()
        
        page.update()
    
    page.overlay.append(sheet_añadir)
    def abrir_shtAñadir():
        sheet_añadir.open = True
        page.update()
    
    def cerrar_shtAñadir():
        sheet_añadir.open = False
        page.update()
    
    def añadir_materia():
        alert_nombre.visible = alert_parcial.visible = alert_añadir.visible = False
        
        if not nombre.value:
            alert_nombre.controls[1].value = "Este campo es obliatorio" # type: ignore
            alert_nombre.visible = True
            
        else:
            is_valid, mensaje = MateriaCtrl().crear_materia(
                page.session.store.get("user"), # type: ignore
                nombre.value,
                parcial_1.value,
                parcial_2.value,
                parcial_3.value
            )
            
            if not is_valid:
                alert_añadir.controls[1].value = mensaje # type: ignore
                alert_añadir.visible = True
            else:
                actualizar_materias()
                cerrar_shtAñadir()
        
        page.update()
    
    page.overlay.append(sheet_eliminar)
    def abrir_shtEliminar():
        sheet_eliminar.open = True
        page.update()
    
    def vaciar_materias():
        alert_eliminar.visible = False
        is_valid, mensaje = MateriaCtrl().vaciar_materias(page.session.store.get("user")) # type: ignore
        
        if not is_valid:
            alert_eliminar.controls[1].value = mensaje # type: ignore
            alert_eliminar.visible = True
        else:
            Materia.modo_eliminar = False
            btn_modo.icon = ft.Icons.CHECKLIST_ROUNDED
            btn_modo.data = "lec"
                
            for materia in materias.controls:
                materia.actualizar() # type: ignore
            
            actualizar_materias()
            sheet_eliminar.open = False
        
        page.update()
    
    def actualizar_materias():
        data = MateriaCtrl().obtener_data(page.session.store.get("user")) # type: ignore
        
        promedio_general = 0.0
        for m in data: # type: ignore
            promedio_general += float(m["promedio"])
        promedio_general = (promedio_general / len(data)) if promedio_general != 0.0 else promedio_general # type: ignore
                
        materias.controls = [
            Materia(
                m["id"],
                m["nombre"],
                m["parcial_1"],
                m["parcial_2"],
                m["parcial_3"],
                m["promedio"],
                lambda e: eliminar_materia(e)
            ) for m in data # type: ignore
        ]
         
        page.update()       
    
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
    
    data = MateriaCtrl().obtener_data(page.session.store.get("user")) # type: ignore
    promedio_general = 0.0
    for m in data: # type: ignore
        promedio_general += float(m["promedio"])
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
                                ft.Icon(icono_perfil, size=125, color=ft.Colors.DEEP_ORANGE_500) 
                                if isinstance(icono_perfil, ft.IconData) else 
                                ft.Image(icono_perfil, width=125, color=ft.Colors.DEEP_ORANGE_500),
                                ft.Column(
                                    [
                                        ft.Text("Promedio General"),
                                        ft.Text(f"{float(promedio_general):g}")
                                    ]
                                )
                            ],
                            margin=ft.Margin(top=2)
                        ),
                        bgcolor=ft.Colors.DEEP_ORANGE,
                        shadow_color=ft.Colors.TRANSPARENT,
                        shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(15, 15, 15, 15))
                    ),
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Mi Senda"),
                                    btn_modo
                                ],
                                expand=True
                            ),
                            ft.Card(
                                materias,
                                bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
                                shadow_color=ft.Colors.TRANSPARENT,
                                shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(15, 15, 15, 15)),
                                expand=True
                            ),
                            ft.Column(
                                [
                                    btn_añadir,
                                    btn_vaciar
                                    # ft.IconButton(
                                    #     ft.Icon(ft.Icons.PERSON_ROUNDED),
                                    #     bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
                                    #     col=2,
                                    #     on_click=lambda _: page.go("/perfil")
                                    # )
                                ]
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0
                    )
                ],
                spacing=0
            )
        ],
        margin=ft.Margin(3),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0
    )