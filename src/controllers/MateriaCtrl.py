from models.MateriaModel import MateriaModel
from models.Database import Database

class MateriaCtrl:
    def __init__(self):
        self.model = MateriaModel(Database())

    def obtener(self, email):
        return self.model.obtener(email)

    def crear(self, email, nombre, parcial1, parcial2, parcial3, promedio):
        return self.model.crear(email, nombre, parcial1, parcial2, parcial3, promedio)

    def eliminar(self, id):
        return self.model.eliminar(id)
