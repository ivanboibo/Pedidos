from  peewee import *
from connection_POSTGRESQL import *
from BaseModel import *

class CLIENTE(BaseModel):
    numero = peewee.IntegerField(primary_key=True)
    nombre = peewee.CharField()
    direccion = peewee.CharField()
    telefono = peewee.CharField()
    email = peewee.CharField()

    class Meta:
        db_table = "CLIENTE"
        database = pg_db

    @staticmethod
    def test():
        query = CLIENTE.select()
        for row in query:
            print(row.numero,row.nombre, row.direccion, row.telefono, row.email )


