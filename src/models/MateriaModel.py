import mysql.connector
from models.Database import Database

class MateriaModel:
    def __init__(self, db: Database):
        self.db = db

    def obtener(self, email_usuario):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True) # type: ignore
            cursor.execute("SELECT * FROM materias WHERE email_usuario = %s", (email_usuario,))
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            cursor.close()
            conn.close() # type: ignore

    def crear(self, email_usuario, nombre, parcial1, parcial2, parcial3, promedio):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor() # type: ignore
            cursor.execute(
                "INSERT INTO materias (email_usuario, nombre, parcial1, parcial2, parcial3, promedio) VALUES (%s, %s, %s, %s, %s, %s)",
                (email_usuario, nombre, parcial1, parcial2, parcial3, promedio)
            )
            conn.commit() # type: ignore
            return cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            cursor.close()
            conn.close() # type: ignore

    def eliminar(self, id):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor() # type: ignore
            cursor.execute("DELETE FROM materias WHERE id = %s", (id,))
            conn.commit() # type: ignore
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            cursor.close()
            conn.close() # type: ignore
