from pydantic import ValidationError
from decimal import Decimal
from models.MateriaModel import MateriaModel
from models.Database import Database
from models.schemas import Materia_Schema

class MateriaCtrl:
    def __init__(self):
        self.model = MateriaModel(Database())

    def obtener_data(self, email_usuario: str):
        return self.model.data(email_usuario)

    def crear_materia(self, email_usuario: str, nombre: str, parcial_1, parcial_2, parcial_3):
        try:
            data = Materia_Schema(nombre=nombre, parcial_1=parcial_1, parcial_2=parcial_2, parcial_3=parcial_3)
            return self.model.crear(email_usuario, data.nombre, data.parcial_1, data.parcial_2, data.parcial_3)
        
        except ValidationError as err:
            print(f"Error de validación en crear: {err}")
            if "nombre" in err.errors()[0]['loc']:
                return False, "El nombre de la materia debe ser menor a 255 caracteres"
            
            elif any(p in err.errors()[0]['loc'] for p in ["parcial_1", "parcial_2", "parcial_3"]):
                return False, "Los parciales deben ser números entre 0 y 10, con hasta un decimal"

    def eliminar_materia(self, id: int):
        return self.model.eliminar(id)
    
    def vaciar_materias(self, email_usuario: str):
        return self.model.vaciar(email_usuario)
