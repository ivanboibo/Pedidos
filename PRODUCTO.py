from  peewee import *
from connection_POSTGRESQL import *
from BaseModel import *
from CLIENTE import *

class PRODUCTO(BaseModel):
    numero = IntegerField(primary_key=True)
    stock = IntegerField()
    tipo = CharField()

    class Meta:
        db_table = "PRODUCTO"