import bcrypt
import mysql.connector
from typing import Literal
from models.Database import Database

class UsuarioModel:
    def __init__(self, db: Database):
        self.db = db
    
    def data(self, email: str, campo: str = "*"):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True) # type: ignore
            
            cursor.execute(f"SELECT {campo} FROM usuarios WHERE email = %s", (email,))
            return cursor.fetchone() # type: ignore
        
        except mysql.connector.Error as err:
            print(f"Error en data: {err}")
            return None
        
        finally:
            cursor.close()
            conn.close() # type: ignore
    
    def iniciar_sesion(self, email: str, passw: str):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True) # type: ignore
            cursor.execute("SELECT passw FROM usuarios WHERE email = %s", (email,))
            user = cursor.fetchone()
            
            if user:
                if bcrypt.checkpw(passw.encode('utf-8'), user['passw'].encode('utf-8')):
                    return True, ""
                else:
                    return False, "La contraseña no coincide"
            else:
                return False, "No se encontró una cuenta con ese correo electrónico"
            
        except mysql.connector.Error as err:
            print(f"Error en iniciar_sesion: {err}")
            return False, "Hubo un error al intentar iniciar sesión"
        
        finally:
            cursor.close()
            conn.close() # type: ignore
    
    def registrar(self, nombres: str, apellidos: str, especialidad: Literal["programacion", "electronica", "contabilidad", "electricidad"], email: str, passw: str):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor() # type: ignore
            
            hashed_passw = bcrypt.hashpw(passw.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
            cursor.execute(
                """INSERT INTO usuarios (nombres, apellidos, especialidad, email, passw)
                VALUES (%s, %s, %s, %s, %s)""", (nombres, apellidos, especialidad, email, hashed_passw)
            )
            
            conn.commit() # type: ignore
            return True, ""
        
        except mysql.connector.Error as err:
            print(f"Error en registrar: {err}")
            return False, "Hubo un error al intentar registrarte"
        
        finally:
            cursor.close()
            conn.close() # type: ignore
    
    def eliminar(self, email: str):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor() # type: ignore
            
            cursor.execute("DELETE FROM usuarios WHERE email = %s", (email,))
            conn.commit() # type: ignore
            return True, ""
        
        except mysql.connector.Error as err:
            print(f"Error en eliminar: {err}")
            return False, "Hubo un error al intentar eliminar tu cuenta, intentalo otra vez"
        
        finally:
            cursor.close()
            conn.close() # type: ignore