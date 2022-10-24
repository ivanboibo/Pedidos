from  peewee import *
from connection_POSTGRESQL import *
from BaseModel import *
from CLIENTE import *

class CUENTA(BaseModel):
    numero = IntegerField(primary_key=True)
    numeroCliente = ForeignKeyField(CLIENTE, backref="Numero")
    numeroTarjeta = ForeignKeyField(Ta)