from  peewee import *
from connection_POSTGRESQL import *
from BaseModel import *
from CLIENTE import *
from TARJETA import *

class PAGO(BaseModel):
    numero = IntegerField(primary_key=True)
    estado = CharField()
    numeroTarjeta = ForeignKeyField(TARJETA, backref="numero")
    class Meta:
        db_table = "PAGO"