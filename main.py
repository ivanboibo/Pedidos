from peewee import *
from CLIENTE import *
from BaseModel import *


with pg_db:
    continuar = True
    while continuar:
        print("1.Crear Cliente")
        print("2.Modificar Cliente")
        print("3.Ver Clientes")
        print("4.Eliminar Cliente")
        print("5.Terminar")

        opcion1 = int(input())
        print()

        if opcion1 == 1:
            CLIENTE.alta_cliente()

        elif opcion1 == 2:
            CLIENTE.modificar_cliente()

        elif opcion1 == 3:
            CLIENTE.ver_tabla()

        elif opcion1 == 4:
            CLIENTE.eliminar_cliente()

        elif opcion1 == 5:
            continuar = False