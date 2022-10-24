from  peewee import *
from connection_POSTGRESQL import *
from BaseModel import *
from CLIENTE import *

class TARJETA(BaseModel):
     numero = IntegerField(primary_key=True)
     banco = CharField()
     tipo = CharField()

     class Meta:
          db_table = "TARJETA"

