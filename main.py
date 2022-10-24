from peewee import *
from CLIENTE import *
from BaseModel import *




with pg_db:

    test = CLIENTE.create(numero = 1658, nombre = 'test', direccion = "blanes", telefono = "2132132", email = "adasd")
