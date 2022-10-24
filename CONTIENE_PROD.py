from  peewee import *
from connection_POSTGRESQL import *
from BaseModel import *
from CLIENTE import *
from PEDIDO import *
from CUENTA import *
from PAGO import *
from PRODUCTO import *

class CONTIENE_PROD(BaseModel):
    numeroPedidoSimple = ForeignKeyField(PEDIDO, backref="numero")
    numeroProducto = ForeignKeyField(PRODUCTO, backref="numero")