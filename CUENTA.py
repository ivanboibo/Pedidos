from  peewee import *
from connection_POSTGRESQL import *
from BaseModel import *
from CLIENTE import *
from TARJETA import *

class CUENTA(BaseModel):
    numero = IntegerField(primary_key=True)
    numeroCliente = ForeignKeyField(CLIENTE, backref="numero")
    numeroTarjeta = ForeignKeyField(TARJETA, backref="numero")

    class Meta:
        db_table = "CUENTA"