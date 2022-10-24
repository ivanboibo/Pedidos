from  peewee import *
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
    def ver_tabla():
        query = CLIENTE.select()
        for row in query:
            print(row.numero,row.nombre, row.direccion, row.telefono, row.email)
        print()

    @staticmethod
    def alta_cliente():
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

        CLIENTE.create(numero=numero, nombre=nombre, direccion=direccion, telefono=telefono, email=email)
        pg_db.commit()
        print("Cliente creado con éxito")
        print()

    @staticmethod
    def eliminar_cliente():
        print("Ingrese el Número del Cliente a eliminar: ")
        numero = int(input())
        print()

        CLIENTE.delete().where(CLIENTE.numero == numero).execute()
        pg_db.commit()
        print("Cliente eliminado con éxito")
        print()

    @staticmethod
    def modificar_cliente():
        print("1.Modificar Tupla entera")
        print("2.Modificar un Atributo")

        opcion1 = int(input())

        if opcion1 == 1:
            print()
            print("Ingrese el Número del Cliente que desea modificar: ")
            numero = int(input())

            print("Ingrese nuevo Nombre: ")
            nuevo_nombre = input()
            print()

            print("Ingrese nueva Dirección: ")
            nueva_direccion = input()
            print()

            print("Ingrese nuevo Teléfono: ")
            nuevo_telefono = input()
            print()

            print("Ingrese nuevo Email: ")
            nuevo_email = input()
            print()

            nuevo_cliente = CLIENTE(numero = numero, nombre = nuevo_nombre, direccion = nueva_direccion, telefono = nuevo_telefono, email = nuevo_email)
            nuevo_cliente.save()

        elif opcion1 == 2:
            print()
            print("Ingrese el Número del Cliente que desea modificar: ")
            numero = int(input())
            print()

            print("1.Modificar Nombre")
            print("2.Modificar Dirección")
            print("3.Modificar Teléfono")
            print("4.Modificar Email")

            opcion2 = int(input())
            print()

            if opcion2 == 1:
                print("Ingrese nuevo Nombre: ")
                nuevo_nombre = input()
                print()
                CLIENTE.update({CLIENTE.nombre: nuevo_nombre}).where(CLIENTE.numero == numero).execute()

            elif opcion2 == 2:
                print("Ingrese nueva Dirección: ")
                nueva_direccion = input()
                print()
                CLIENTE.update({CLIENTE.direccion: nueva_direccion}).where(CLIENTE.numero == numero).execute()

            elif opcion2 == 3:
                print("Ingrese nuevo Teléfono: ")
                nuevo_telefono = input()
                print()
                CLIENTE.update({CLIENTE.telefono: nuevo_telefono}).where(CLIENTE.numero == numero).execute()

            elif opcion2 == 4:
                print("Ingrese nuevo Email: ")
                nuevo_email = input()
                print()
                CLIENTE.update({CLIENTE.email: nuevo_email}).where(CLIENTE.numero == numero).execute()

        pg_db.commit()
        print("Cliente modificado con éxito")
        print()


