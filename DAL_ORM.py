from peewee import *
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

    @staticmethod
    def altaCliente():
        print("Ingrese Número de Cliente: ")
        numero = int(input())
        print()

        print("Ingrese Nombre de Cliente: ")
        nombre = input()
        print()

        print("Ingrese Dirección de Cliente: ")
        direccion = input()
        print()

        print("Ingrese Teléfono de Cliente: ")
        telefono = input()
        print()

        print("Ingrese Email de Cliente: ")
        email = input()
        print()

        print(f"{numero} {nombre} {direccion} {telefono} {email}")

        CLIENTE.create(numero = numero, nombre = nombre, direccion = direccion, telefono = telefono, email = email)




class PRODUCTO(BaseModel):
    numero = IntegerField(primary_key=True)
    stock = IntegerField()
    tipo = CharField()

    class Meta:
        db_table = "PRODUCTO"


class TARJETA(BaseModel):
    numero = IntegerField(primary_key=True)
    banco = CharField()
    tipo = CharField()

    class Meta:
        db_table = "TARJETA"


class CUENTA(BaseModel):
    numero = IntegerField(primary_key=True)
    numeroCliente = ForeignKeyField(CLIENTE, backref="numero")
    numeroTarjeta = ForeignKeyField(TARJETA, backref="numero")

    class Meta:
        db_table = "CUENTA"


class PAGO(BaseModel):
    numero = IntegerField(primary_key=True)
    estado = CharField()
    numeroTarjeta = ForeignKeyField(TARJETA, backref="numero")
    class Meta:
        db_table = "PAGO"


class PEDIDO(BaseModel):
    numero = IntegerField(primary_key=True)
    numeroCliente = ForeignKeyField(CLIENTE, backref="numero")
    estado = CharField()

    class Meta:
        db_table = "PEDIDO"


class PEDIDO_COMPUESTO(BaseModel):
    numeroPedido = ForeignKeyField(PEDIDO, backref="numero")
    numeroPedidoHijo = ForeignKeyField(PEDIDO, backref="numero")

    class Meta:
        db_table = "PEDIDO_COMPUESTO"


class PEDIDO_SIMPLE(BaseModel):
    numeroPedido = ForeignKeyField(PEDIDO, backref="numero")
    numeroCuenta = ForeignKeyField(CUENTA, backref="numero")
    numeroPago = ForeignKeyField(PAGO, backref="numero")

    class Meta:
        db_table = "PEDIDO_SIMPLE"


class CONTIENE_PROD(BaseModel):
    numeroPedidoSimple = ForeignKeyField(PEDIDO, backref="numero")
    numeroProducto = ForeignKeyField(PRODUCTO, backref="numero")

    class Meta:
        db_table = "CONTIENE_PROD"