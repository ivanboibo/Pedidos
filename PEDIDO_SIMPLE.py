from  peewee import *
from connection_POSTGRESQL import *
from BaseModel import *
from CLIENTE import *
from PEDIDO import *
from CUENTA import *
from PAGO import *

class PEDIDO_SIMPLE(BaseModel):
    numeroPedido = ForeignKeyField(PEDIDO, backref="numero")
    numeroCuenta = ForeignKeyField(CUENTA, backref="numero")
    numeroPago = ForeignKeyField(PAGO, backref="numero")