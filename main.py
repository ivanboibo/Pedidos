from peewee import *
from CLIENTE import *
from BaseModel import *




with pg_db:
    test = CLIENTE.create(numero = 16588, nombre = 'test2', direccion = "blanes2", telefono = "21321323", email = "adasd2")
