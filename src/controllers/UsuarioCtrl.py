from pydantic import ValidationError
from models.UsuarioModel import UsuarioModel
from models.Database import Database
from models.schemas import UsuarioBase_Schema, UsuarioRegistro_Schema

class UsuarioCtrl:
    def __init__(self):
        self.model = UsuarioModel(Database())
    
    def obtener_data(self, email, campo):
        return self.model.data(email, campo)
    
    def iniciar_sesion(self, email, passw):
        try:
            data = UsuarioBase_Schema(email=email, passw=passw)
            is_valid, mensaje = self.model.iniciar_sesion(data.email, data.passw)
            return is_valid, mensaje
            
        except ValidationError as err:
            print(f"Error de validación en iniciar_sesion: {err}")
            if "email" in err.errors()[0]['loc']:
                return False, "El correo electrónico debe tener @ y un dominio válido"
            
            elif "passw" in err.errors()[0]['loc']:
                return False, "La contraseña debe tener entre 8 y 255 caracteres"
    
    def registrar(self, nombre_completo, apellidos, especialidad, email, passw):
        try:
            data = UsuarioRegistro_Schema(
                nombre_completo=nombre_completo,
                apellidos=apellidos,
                especialidad=especialidad,
                email=email,
                passw=passw
            )
            
            is_valid, mensaje = self.model.registrar(
                data.nombre_completo,
                data.apellidos,
                data.especialidad,
                data.email,
                data.passw
            )
            
            return is_valid, mensaje
            
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
    
    def eliminar_cuenta(self, email):
        return self.model.eliminar(email)