import flet as ft
from typing import Callable
from decimal import Decimal

class Materia(ft.Card):
    modo_eliminar = False
    
    def __init__(self, id: int, nombre: str, parcial_1: Decimal, parcial_2: Decimal, parcial_3: Decimal, promedio: Decimal, onClick: ft.ControlEventHandler[ft.IconButton]):
        self.txt_promedio = ft.Text(
            f"{float(promedio):g}",
            size=45,
            weight=ft.FontWeight.W_500,
            color=ft.Colors.DEEP_ORANGE,
            visible=not Materia.modo_eliminar
        )
        
        self.btn_eliminar = ft.IconButton(
            ft.Icons.DELETE,
            ft.Colors.RED,
            40,
            data=id,
            visible=Materia.modo_eliminar,
            on_click=onClick
        )
        
        super().__init__(
            ft.Container(
                ft.ResponsiveRow(
                    [
                        ft.Column(
                            [
                                ft.Text(
                                    nombre,
                                    size=25,
                                    weight=ft.FontWeight.W_500,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                    tooltip=nombre
                                ),
                                ft.Row(
                                    [
                                        ft.Text(f"{float(parcial_1):g}", size=15, color=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                                        ft.Text(f"{float(parcial_2):g}", size=15, color=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                                        ft.Text(f"{float(parcial_3):g}", size=15, color=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                                    ],
                                    ft.MainAxisAlignment.SPACE_EVENLY,
                                    margin=ft.Margin(bottom=5)
                                )
                            ],
                            ft.MainAxisAlignment.CENTER,
                            col=9,
                            spacing=0
                        ),
                        ft.Row(
                            [
                                self.txt_promedio,
                                self.btn_eliminar
                            ],
                            ft.MainAxisAlignment.CENTER,
                            col=3,
                            align=ft.Alignment.CENTER_RIGHT
                        )
                    ]
                ),
                padding=ft.Padding(10, 0, 10, 0)
            )
        )
        
        self.variant = ft.CardVariant.OUTLINED
    
    def actualizar(self):
        self.txt_promedio.visible = not Materia.modo_eliminar
        self.btn_eliminar.visible = Materia.modo_eliminar
        self.update()