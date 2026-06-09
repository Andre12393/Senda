import flet as ft
from decimal import Decimal

class Materia(ft.Card):
    def __init__(self, nombre: str, parcial_1: Decimal, parcial_2: Decimal, parcial_3: Decimal, promedio: Decimal):
        super().__init__(
            content=ft.Row(
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
                    ft.Text(f"{float(promedio):g}", size=16, weight=ft.FontWeight.W_600, color=ft.Colors.DEEP_ORANGE)
                ]
            )
        )