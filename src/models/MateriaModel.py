import mysql.connector
from decimal import Decimal
from models.Database import Database

class MateriaModel:
    def __init__(self, db: Database):
        self.db = db

    def data(self, email_usuario: str):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True) # type: ignore
            
            cursor.execute(f"SELECT * FROM materias WHERE email_usuario = %s", (email_usuario,))
            return cursor.fetchall() # type: ignore
        
        except mysql.connector.Error as err:
            print(f"Error en data: {err}")
            return None
        
        finally:
            cursor.close()
            conn.close() # type: ignore

    def crear(self, email_usuario: str, nombre: str, parcial_1: Decimal, parcial_2: Decimal, parcial_3: Decimal):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor() # type: ignore
            
            cursor.execute(
                """INSERT INTO materias (email_usuario, nombre, parcial_1, parcial_2, parcial_3) 
                VALUES (%s, %s, %s, %s, %s)""", (email_usuario, nombre, parcial_1, parcial_2, parcial_3)
            )
            
            conn.commit() # type: ignore
            return True, ""
        
        except mysql.connector.Error as err:
            print(f"Error en crear: {err}")
            return False, "Hubo un error al intentar crear la materia, inténtalo de nuevo"
        
        finally:
            cursor.close()
            conn.close() # type: ignore

    def eliminar(self, id: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor() # type: ignore
            
            cursor.execute("DELETE FROM materias WHERE id = %s", (id,))
            
            conn.commit() # type: ignore
            return True, ""
        
        except mysql.connector.Error as err:
            print(f"Error en eliminar: {err}")
            return False, "Hubo un error al intentar eliminar la materia, inténtalo de nuevo"
        
        finally:
            cursor.close()
            conn.close() # type: ignore
