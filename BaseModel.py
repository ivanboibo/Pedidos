from peewee import *
from connection_POSTGRESQL import *

class BaseModel(Model):
    class Meta:
        database = pg_db
        schema = "Pedidos"
        order_by = id
