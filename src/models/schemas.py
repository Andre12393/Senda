from typing import Literal
from pydantic import BaseModel, EmailStr, Field

class UsuarioBase_Schema(BaseModel):
    email: EmailStr = Field(max_length=255)
    passw: str = Field(min_length=8, max_length=255)
    
class UsuarioRegistro_Schema(UsuarioBase_Schema):
    nombre_completo: str = Field(min_length=3, max_length=255)
    apellidos: str = Field(min_length=3, max_length=255)
    especialidad: Literal["programacion", "electronica", "contabilidad", "electricidad"]