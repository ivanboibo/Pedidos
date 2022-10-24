from  peewee import *
from connection_POSTGRESQL import *
from BaseModel import *
from CLIENTE import *
from PEDIDO import *

class PEDIDO_COMPUESTO(BaseModel):
    numeroPedido = ForeignKeyField(PEDIDO, backref="numero")
    numeroPedidoHijo = ForeignKeyField(PEDIDO, backref="numero")