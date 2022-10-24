from peewee import *
from connection_POSTGRESQL import *

class BaseModel(Model):
    class Meta:
        database = pg_db
        order_by = id
