import os
import platform

#Functions
#---
users = {}
id = 0

def clear_sys():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")


def create_users():
    clear_sys()
    u = []
    name = input("Ingresa tu nombre: ").title()
    u.append(name)
    age = input("Ingresa tu edad: ")
    age+=" años"
    u.append(age)
    email = input("Ingresa tu email: ")
    u.append(email)
    global id
    id+=1
    global users
    users[id] = u
    print("Usuario creado exitosamente!!")


def read_users():
    clear_sys()
    for _,val in users.items():
        for i in val:
            print(i,sep=",")
        print("")
    print("Listado Exitoso!!")


def update_users():
    clear_sys()
    email = input("Ingresa el email de usuario: ")
    global users
    u = []
    for k,values in users.items():
        for value in values:
            if value == email:
                name = input("Ingresa tu nombre: ").title()
                u.append(name)
                age = input("Ingresa tu edad: ")
                age+=" años"
                u.append(age)
                email = input("Ingresa tu email: ")
                u.append(email)
                users[k]=u
                print("Usuario actualizado exitosamente")
                break
    if len(u) == 0:
        print("No se encontro a ese usuario!!")


def delete_users():
    clear_sys()
    email = input("Ingresa el email de usuario: ")
    global users
    for k,values in users.items():
        for value in values:
            if value == email:
                ru = users[k]
                del ru
                print("Usuario eliminado exitosamente!!")
                break
    if len(ru) == 0:
        print("No se encontro a ese usuario!!")


#MAIN
#----
# print("1.Crear Usuario\n2.Mostrar Usuarios\n3.Actualizar Usuario\n4.Borrar Usuario\n5.Salir")
# desition = int(input("Que deseas realizar?: "))

while True:
    print("1.Crear Usuario\n2.Mostrar Usuarios\n3.Actualizar Usuario\n4.Borrar Usuario\n5.Salir")
    desition = input("Que deseas realizar?: ").lower()
    if desition == "1" or  desition.startswith("c"):
        create_users()
        print("")
    elif desition == "2"  or desition.startswith("m"):
        read_users()
        print("")
    elif desition == "3"  or desition.startswith("a"):
        update_users()
        print("")
    elif desition == "4"  or desition.startswith("b"):
        delete_users()
        print("")
    elif desition == "5"  or desition.startswith("s"):
        break
    else:
        print("Opcion no valida")

