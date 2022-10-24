from  peewee import *
from connection_POSTGRESQL import *
from BaseModel import *
from CLIENTE import *

class PEDIDO(BaseModel):
    numero = IntegerField(primary_key=True)
    numeroCliente = ForeignKeyField(CLIENTE, backref="numero")
    estado = CharField()

    class Meta:
        db_table = "PEDIDO"