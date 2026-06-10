import flet as ft
from typing import Callable
from decimal import Decimal

class Materia(ft.Card):
    modo_eliminar = False
    
    def __init__(self, id: int, nombre: str, parcial_1: Decimal, parcial_2: Decimal, parcial_3: Decimal, promedio: Decimal, onClick: ft.ControlEventHandler[ft.IconButton]):
        self.txt_promedio = ft.Text(
            f"{float(promedio):g}",
            size=20,
            weight=ft.FontWeight.W_500,
            visible=not Materia.modo_eliminar
        )
        
        self.btn_eliminar = ft.IconButton(
            ft.Icons.DELETE,
            data=id,
            visible=Materia.modo_eliminar,
            on_click=onClick
        )
        
        super().__init__(
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(nombre, size=18, weight=ft.FontWeight.W_500),
                            ft.Row(
                                [
                                    ft.Text(f"{float(parcial_1):g}", size=14),
                                    ft.Text(f"{float(parcial_2):g}", size=14),
                                    ft.Text(f"{float(parcial_3):g}", size=14),
                                ]
                            )
                        ]
                    ),
                    ft.Row(
                        [
                            self.txt_promedio,
                            self.btn_eliminar
                        ]
                    )
                ]
            )
        )
        
        self.variant = ft.CardVariant.OUTLINED
    
    def cambiar_modo(self):
        self.txt_promedio.visible = not Materia.modo_eliminar
        self.btn_eliminar.visible = Materia.modo_eliminar
        self.update()