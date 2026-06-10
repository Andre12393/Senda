from pydantic import ValidationError
from typing import Literal
from models.UsuarioModel import UsuarioModel
from models.Database import Database
from models.schemas import UsuarioBase_Schema, UsuarioRegistro_Schema

class UsuarioCtrl:
    def __init__(self):
        self.model = UsuarioModel(Database())
    
    def obtener_data(self, email: str, campo: str):
        return self.model.data(email, campo)
    
    def iniciar_sesion(self, email: str, passw: str):
        try:
            data = UsuarioBase_Schema(email=email, passw=passw)
            return self.model.iniciar_sesion(data.email, data.passw)
            
        except ValidationError as err:
            print(f"Error de validación en iniciar_sesion: {err}")
            if "email" in err.errors()[0]['loc']:
                return False, "El correo electrónico debe tener @ y un dominio válido"
            
            elif "passw" in err.errors()[0]['loc']:
                return False, "La contraseña debe tener entre 8 y 255 caracteres"
    
    def registrar(self, nombres: str, apellidos: str, especialidad: Literal["programacion", "electronica", "contabilidad", "electricidad"], email: str, passw: str):
        try:
            data = UsuarioRegistro_Schema(
                nombres=nombres,
                apellidos=apellidos,
                especialidad=especialidad,
                email=email,
                passw=passw
            )
            
            return self.model.registrar(data.nombres, data.apellidos, data.especialidad, data.email, data.passw)
            
        except ValidationError as err:
            print(f"Error de validación en registrar: {err}")
            if "nombre_completo" in err.errors()[0]['loc']:
                return False, "El nombre completo debe tener entre 3 y 255 caracteres"
            
            elif "apellidos" in err.errors()[0]['loc']:
                return False, "Los apellidos deben tener entre 3 y 255 caracteres"
            
            elif "especialidad" in err.errors()[0]['loc']:
                return False, "Selecciona una especialidad existente"
            
            elif "email" in err.errors()[0]['loc']:
                return False, "El correo electrónico debe tener @ y un dominio válido"
            
            elif "passw" in err.errors()[0]['loc']:
                return False, "La contraseña debe tener entre 8 y 255 caracteres"
    
    def eliminar_cuenta(self, email: str):
        return self.model.eliminar(email)