import flet as ft
from controllers.MateriaCtrl import MateriaCtrl

def materias(page: ft.Page):
    ctrl = MateriaCtrl()
    email = page.session.store.get("user")
    materias_lista = ft.Column(spacing=8, scroll=ft.ScrollMode.AUTO, expand=True)

    nombre = ft.TextField(label="Materia", expand=True)
    p1 = ft.TextField(label="Parcial 1", width=100, keyboard_type=ft.KeyboardType.NUMBER)
    p2 = ft.TextField(label="Parcial 2", width=100, keyboard_type=ft.KeyboardType.NUMBER)
    p3 = ft.TextField(label="Parcial 3", width=100, keyboard_type=ft.KeyboardType.NUMBER)
    error = ft.Text("", color=ft.Colors.ERROR, size=12)

    def hacer_card(m):
        califs = [c for c in [m["parcial1"], m["parcial2"], m["parcial3"]] if c is not None]
        color = ft.Colors.GREEN if m["promedio"] >= 6 else ft.Colors.ERROR
        card = ft.Card()
        card.content = ft.ListTile(
            title=ft.Text(m["nombre"], weight=ft.FontWeight.W_600),
            subtitle=ft.Text("  ".join([f"P{i+1}: {c}" for i, c in enumerate(califs)])),
            trailing=ft.Row(
                [
                    ft.Text(f"Prom: {m['promedio']:.1f}", color=color, weight=ft.FontWeight.W_700),
                    ft.IconButton(
                        ft.Icons.DELETE_OUTLINE,
                        icon_color=ft.Colors.ERROR,
                        data=(m["id"], card),
                        on_click=lambda e: borrar(e.control.data)
                    )
                ],
                spacing=0,
                tight=True
            )
        )
        
        return card

    def borrar(data):
        id, card = data
        ctrl.eliminar(id)
        materias_lista.controls.remove(card)
        page.update()

    def agregar(_):
        if not nombre.value:
            error.value = "Ingresa el nombre de la materia."
            page.update()
            return

        try:
            califs = [float(p.value) for p in [p1, p2, p3] if p.value]
        except ValueError:
            error.value = "Las calificaciones deben ser números."
            page.update()
            return

        if not califs:
            error.value = "Ingresa al menos una calificación."
            page.update()
            return

        promedio = sum(califs) / len(califs)
        vals = [float(p.value) if p.value else None for p in [p1, p2, p3]]
        id = ctrl.crear(email, nombre.value, vals[0], vals[1], vals[2], promedio)

        if id:
            materias_lista.controls.append(hacer_card({
                "id": id, "nombre": nombre.value,
                "parcial1": vals[0], "parcial2": vals[1], "parcial3": vals[2],
                "promedio": promedio
            }))
            nombre.value = ""
            p1.value = ""
            p2.value = ""
            p3.value = ""
            error.value = ""
        else:
            error.value = "Error al guardar la materia."

        page.update()

    # Cargar materias existentes
    for m in ctrl.obtener(email):
        materias_lista.controls.append(hacer_card(m))

    return ft.View(
        route="/materias",
        controls=[
            ft.AppBar(
                title=ft.Text("Materias y Calificaciones", weight=ft.FontWeight.W_600),
                bgcolor=ft.Colors.SURFACE_CONTAINER,
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/dashboard"))
            ),
            ft.Container(
                ft.Column(
                    [
                        ft.Row([nombre], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([p1, p2, p3], alignment=ft.MainAxisAlignment.CENTER),
                        error,
                        ft.ElevatedButton("Agregar Materia", icon=ft.Icons.ADD, on_click=agregar),
                        ft.Divider(),
                        materias_lista,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                    expand=True
                ),
                padding=20,
                expand=True
            )
        ],
        bgcolor=ft.Colors.SURFACE_CONTAINER_LOWEST
    )
