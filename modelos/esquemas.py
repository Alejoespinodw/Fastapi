
from pydantic import BaseModel,Field,model_validator
from datetime import datetime

from pydantic import BaseModel


class Cotizar(BaseModel):
    anio:str
    iva: str
    ceroKM:str
    fechaVigencia:str = Field(datetime.now().strftime('%d/%m/%Y'))
    codInfoAuto: str
    codigoPostal: str
    gnc: str
    modalidad: str
    productor:str
    uso: str
    modelo: str
    marca:str
    version:str


class Emitir(BaseModel):
    presupuesto:str 
    productor:str 
    apellido:str 
    nombres:str 
    tipoDocumento:str 
    numeroDocumento:str
    sexo:str   
    fechaNacimiento: str 
    posicionIva:str 
    email:str 
    prefijo:str 
    telefono:str 
    calle:str 
    numero:str 
    piso:str
    departamento:str
    codigoPostal:str
    identificador:str
    plan:str 
    patente:str 
    chasis:str
    motor:str 
    fechaVigencia:str = Field(datetime.now().strftime('%d/%m/%Y'))
    ddjj:str 
    porcentajeModalidad:str
    pep:str 
#---------------formaCobro-------------------#    
    formaCobro: str | None = None 
    titular: str | None = None
    gestor:str | None = None 
    cbu: str |None = None
    tarjeta: str |None = None 
    nroTarjeta:str |None = None
    fechaVencimiento: str | None = None

    @model_validator(mode='after')
    def check(cls, values):
        for k, v in values:
            if not v:
                delattr(values, k)
        return values
    
