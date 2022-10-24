import peewee
from peewee import *

pg_db = PostgresqlDatabase('Pedidos', user='postgres', password='099529033',
                           host='localhost', port=5433)