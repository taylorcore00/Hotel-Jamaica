from opcode import hasjabs
from string import punctuation
import numpy as np
from logging import handlers
from tabnanny import check
import os  #! cl
from datetime import date
import time
from tqdm import tqdm
from time import sleep
import sys

dia = date.today()
day = dia.day
mes = dia.month
año = dia.year

#dni de administracion = 777
# clave de administracion = "jamaica"
def crear_pila(pila): #! este
    pila = []
    return  None


def apilar(pila, s): #! este
    error = False
    pila.append(s.copy())

    return error

def desapilar(pila): #! este
    s = np.empty(1,dtype=servicio)
    if not pila_vacia(pila):
        ultimo = len(pila) - 1
        elemento = pila.pop(ultimo)
        error = False
    else:
        error = True
    return (elemento, error)


def pila_vacia(pila): #! este
    if len(pila)==0:
        vacia = True
    else:
        vacia = False
    return vacia


def mostrarPila(pila, pilaux): #! este
    while not pila_vacia(pila):
        s, error = desapilar(pila)
        print("Numero de habitacion",("  "), "Codigo de servicio",("  "),"Cantidad solicitada")
        print("----------------------------------------------------------------------")

        print(s[0]["nro_hab"],"\t\t\t\t\t\t",s[0]["cods"],"\t\t\t\t\t\t",s[0]["cant"])

        apilar(pilaux, s)
    reapilar(pila, pilaux)


def reapilar(pila, pilaux): #! este
    while not pila_vacia(pilaux):
        s, error = desapilar(pilaux)
        if not error:
            apilar(pila, s)

def existe_servicio(pila, pilaux, nrohab, codserv, cant): #! este
    B = 0
    while B == 0 and not pila_vacia(pila):
        s, error = desapilar(pila)
        if s[0]['nro_hab'] == nrohab and s[0]['cods'] == codserv:
            s[0]['cant'] += cant
            B = 1
        apilar(pilaux, s)
    reapilar(pila, pilaux)
    return B

def carga_pila(ej, op, s, pila, pilaux): #! este
    if op == 1:
        print("")
        print("Eligió la opción del gimnasio, por favor, ingrese su número de habitación")
        nrohab = int(input(">"))
        codserv = 1
        cantserv = int(input("Cantidad deseada >"))
        B = existe_servicio(pila, pilaux, nrohab, codserv, cantserv)
        if B == 0:
            s[0]['nro_hab'] = nrohab
            s[0]['cods'] = codserv
            s[0]['cant'] = cantserv
            apilar(pila, s)
    if op == 2:
        print("")
        print("Eligió la opción del spa, por favor, ingrese su número de habitación")
        nrohab = int(input(">"))
        codserv = 2
        cantserv = int(input("Cantidad deseada >"))
        B = existe_servicio(pila, pilaux, nrohab, codserv, cantserv)
        if B == 0:
            s[0]['nro_hab'] = nrohab
            s[0]['cods'] = codserv
            s[0]['cant'] = cantserv
            apilar(pila, s)

    if op == 3:
        print("")
        print("Eligió el Room-Service, por favor, ingrese su número de habitación")
        nrohab = int(input(">"))
        codserv = 3
        cantserv = int(input("Cantidad deseada >"))
        B = existe_servicio(pila, pilaux, nrohab, codserv, cantserv)
        if B == 0:
            s[0]['nro_hab'] = nrohab
            s[0]['cods'] = codserv
            s[0]['cant'] = cantserv
            apilar(pila, s)

    if op == 4:
        print("")
        print("Eligió la opción del bar, por favor, ingrese su número de habitación")
        nrohab = int(input(">"))
        codserv = 4
        cantserv = int(input("Cantidad deseada >"))
        B = existe_servicio(pila, pilaux, nrohab, codserv, cantserv)
        if B == 0:
            s[0]['nro_hab'] = nrohab
            s[0]['cods'] = codserv
            s[0]['cant'] = cantserv
            apilar(pila, s)

    if op == 5:
        print("")
        print("Eligió la opción del Frigobar, por favor, ingrese su número de habitación")
        nrohab = int(input(">"))
        codserv = 5
        cantserv = int(input("Cantidad deseada >"))
        B = existe_servicio(pila, pilaux, nrohab, codserv, cantserv)
        if B == 0:
            s[0]['nro_hab'] = nrohab
            s[0]['cods'] = codserv
            s[0]['cant'] = cantserv
            apilar(pila, s)

    if op == 6:
        print("")
        print("Eligió la opción de la lavandería, por favor, ingrese su número de habitación")
        nrohab = int(input(">"))
        codserv = 6
        cantserv = int(input("Cantidad deseada >"))
        B = existe_servicio(pila, pilaux, nrohab, codserv, cantserv)
        if B == 0:
            s[0]['nro_hab'] = nrohab
            s[0]['cods'] = codserv
            s[0]['cant'] = cantserv
            apilar(pila, s)

    if op == 7:
        mostrarPila(pila, pilaux)

    if op == 8:
        ej = False
    return ej
servicio = np.dtype(
    [
        ('nro_hab', int),
        ('cods', int),
        ('cant', int)
    ]
)
pila = []
pilaux = []

s = np.empty(1, dtype=servicio)

nh = 1000 #seria 1000 huspedes por mes, y el jefe del hotel debera actualizar este dato por mes
fecha = np.dtype(
    [
        ("dia", "U20"),
        ("mes", "U20"),
        ("anio", int)
    ]
)
acompañantes = np.dtype(
    [
        ("dni", int), #!dni del husped a cargo
        ("nom_acomp", "U20"),
        ("ap_acomp", "U20"),
        ("fecha_acomp", fecha)
    ]
)
ac = np.empty(4,dtype=acompañantes)

dirc = np.dtype(
    [
        ("calle", "U20"),
        ("nro", int),
        ("localidad", "U20")#agregar ciudad y provincia en el mismo lugar

    ]
)
tarjeta = np.dtype(
    [
        ("nrot", "int64"),
        ("fechavencimiento", int),
        ("cod", int)
    ]
)
tc = np.dtype(tarjeta)
fecha_desde = np.dtype( 
    [
        ("dia", int),
        ("mes", int),
        ("anio", int)
    ]
)
fecha_hasta = np.dtype(
    [
        ("dia", int),
        ("mes", int),
        ("anio", int)
    ]
)
Huespedes = np.dtype(
    [
        ("dni", int),
        ("clave","U20"),
        ("nombre", "U20"),
        ("apellido", "U20"),
        ("fechanacimiento", fecha),
        ("direccion", dirc),
        ("nro_habitacion", int),
        ("tarjeta", tarjeta),
        ("checkin", fecha_desde),
        ("checkout", fecha_hasta)
    ]
)
h = np.empty(nh,dtype=Huespedes)

multashuesped = np.dtype(
    [
        ("dni",int),
        ("monto",int),
        ("fecha",fecha)
    ]
)
mh = np.empty(nh,dtype=multashuesped)
fecha_desde = np.dtype(
    [
        ("dia", int),
        ("mes", int)
    ]
)
fecha_hasta = np.dtype(
    [
        ("dia", int),
        ("mes", int)
    ]
)


#Estatico
#10 dobles, 8 triples y  7 cuádruples
room = np.dtype(
    [
        ("nro_h", int),
        ("tipo", "U1"),
        ("precio", float),
        ("est_d", np.ndarray),  # np.ndarray es el tipo array de numpy
        ("est_h", "U15")
    ]
)


ocupacion = np.dtype(
    [
        ("nroh", "U20"),
        ("dni", int),
        ("checkin", fecha_desde),
        ("checkout", fecha_hasta)
    ]   
)
o = np.empty(nh,dtype=ocupacion)

#Cuadruples
N = 7
C = np.empty(N, dtype=room)
M = 30
C[0] = (113, "C", 2000, np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
C[1] = (114, "C", 2000, np.array(["D", "O", "R", "D", "D", "D", "D", "D", "D", "D","D", "O", "R", "D", "D", "D", "D", "D", "D", "D","D", "O", "R", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
C[2] = (115, "C", 2000, np.array(["D", "D", "D", "O", "O", "O", "O", "D", "D", "D","D", "D", "D", "O", "O", "O", "O", "D", "D", "D","D", "D", "D", "O", "O", "O", "O", "D", "D", "D"]), "Habilitada")
C[3] = (116, "C", 2000, np.array(["R", "R", "R", "R", "R", "D", "D", "D", "D", "D","R", "R", "R", "R", "R", "D", "D", "D", "D", "D","R", "R", "R", "R", "R", "D", "D", "D", "D", "D"]), "Habilitada")
C[4] = (117, "C", 2000, np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
C[5] = (118, "C", 2000, np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
C[6] = (119, "C", 2000, np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")

#Triples
O = 8
T = np.empty(O, dtype=room)
M = 30

T[0] = (120, "T", 1500, np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
T[1] = (121, "T", 1500, np.array(["D", "O", "R", "D", "D", "D", "D", "D", "D", "D","D", "O", "R", "D", "D", "D", "D", "D", "D", "D","D", "O", "R", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
T[2] = (122, "T", 1500, np.array(["D", "D", "D", "O", "O", "O", "O", "D", "D", "D","D", "D", "D", "O", "O", "O", "O", "D", "D", "D","D", "D", "D", "O", "O", "O", "O", "D", "D", "D"]), "Habilitada")
T[3] = (123, "T", 1500, np.array(["R", "R", "R", "R", "R", "D", "D", "D", "D", "D","R", "R", "R", "R", "R", "D", "D", "D", "D", "D","R", "R", "R", "R", "R", "D", "D", "D", "D", "D"]), "Habilitada")
T[4] = (124, "T", 1500, np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
T[5] = (125, "T", 1500, np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
T[6] = (126, "T", 1500, np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
T[7] = (127, "T", 1500, np.array(["D", "D", "D", "O", "O", "O", "O", "D", "D", "D","D", "D", "D", "O", "O", "O", "O", "D", "D", "D","D", "D", "D", "O", "O", "O", "O", "D", "D", "D"]), "Habilitada")

#Dobles
P = 10
D = np.empty(P, dtype=room)
M = 30
D[0] = (128, "D", 1000, np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
D[1] = (129, "D", 1000, np.array(["D", "O", "R", "D", "D", "D", "D", "D", "D", "D", "D", "O", "R", "D", "D", "D", "D", "D", "D", "D","D", "O", "R", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
D[2] = (130, "D", 1000, np.array(["D", "D", "D", "O", "O", "O", "O", "D", "D", "D", "D", "D", "D", "O", "O", "O", "O", "D", "D", "D","D", "D", "D", "O", "O", "O", "O", "D", "D", "D"]), "Habilitada")
D[3] = (131, "D", 1000, np.array(["R", "R", "R", "R", "R", "D", ":", "D", "D", "D", "R", "R", "R", "R", "R", "D", "D", "D", "D", "D","R", "R", "R", "R", "R", "D", "D", "D", "D", "D"]), "Habilitada")
D[4] = (132, "D", 1000, np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
D[5] = (133, "D", 1000, np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
D[6] = (134, "D", 1000, np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D","D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
D[7] = (135, "D", 1000, np.array(["D", "D", "D", "O", "O", "O", "O", "D", "D", "D", "D", "D", "D", "O", "O", "O", "O", "D", "D", "D","D", "D", "D", "O", "O", "O", "O", "D", "D", "D"]), "Habilitada")
D[8] = (136, "D", 1000, np.array(["D", "O", "R", "D", "D", "D", "D", "D", "D", "D", "D", "O", "R", "D", "D", "D", "D", "D", "D", "D","D", "O", "R", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
D[9] = (137, "D", 1000, np.array(["D", "O", "R", "D", "D", "D", "D", "D", "D", "D", "D", "O", "R", "D", "D", "D", "D", "D", "D", "D","D", "O", "R", "D", "D", "D", "D", "D", "D", "D"]), "Habilitada")
hab = np.empty(nh,dtype=room)


def loginadmin():
    print(" ")
    print(" 🔒【LOG IN ADMINISTRACION】")
    print(" ")
    print(" ")
    idd = int(input(" ID > "))
    clave = input(" Clave > ")
    if idd == 777:
        if clave == "jamaica":
            accesadmin = "valido"
            return(accesadmin)
        else:
            print(" ACCESO INVALIDO ")
            accesadmin = "invalido"
            return(accesadmin)
    else:
        print(" ACCESO INVALIDO ")
        accesadmin = "invalido"
        return(accesadmin)

def validacion (h,nh,b):
    b=0
    while b == 0:
        print(" ")
        print(" ━ Es obligatorio ser mayor de edad para registrarte dentro del sistema 🔞 ━ ")
        print(" ")
        doc=int (input (" Dni > "))
        if doc > 10000000 and doc < 99999999:
            aux= int(doc/1000000)
            b=1
        else:
            print ("dni invalido", "por favor, ingrese un dni valido")
    return doc


def registro_sistema(h,hab, nh, dni_valido,p): #caja negra
    b = 0
    i = 0
    while i < 1:
        print(" ")
        h[p]["dni"] = dni_valido
        o[p]["dni"] = dni_valido
        h[p]["clave"] = input(" Contraseña > ")
        print(" ")
        h[p]["nombre"] = input(" Nombre > ")
        h[p]["apellido"] = input(" Apellido > ")
        print(" ")
        print("🏠 【Domicilio】 ")  
        print(" ")
        h[p]["direccion"]["calle"] = input("Calle > ")
        h[p]["direccion"]["nro"] = int(input("Numeracion > "))
        h[p]["direccion"]["localidad"] = input("Localidad > ")
        print(" ")
        print("📅 Fecha de nacimiento", "<", h[p]["nombre"], ">")
        print(" ")
        h[p]["fechanacimiento"]["dia"] = int(input("Dia > "))
        h[p]["fechanacimiento"]["mes"] = int(input("Mes > "))
        h[p]["fechanacimiento"]["anio"] = int(input("Año >  "))
        # if (dia.year - h[p]["fechanacimiento"]["anio"]) < 18:
        #     clear()
        #     print(" ")
        #     print("🔞 Debes ser mayor de edad para registrarte en nuestro sistema 🔞")
        #     b = 1
        # else:
        i = i + 1
        p = p + 1
        clear()

def reserva(h, hab,dni):
    for i in range(0,nh):
        if dni == h[i]["dni"]:
            posr = i
            print(" ")
            dimr = int(input(" ¿Cuantas veces desea reservar? > "))
            print(" ")
            if dimr > 0:
                for ñ in range(0,dimr):
                    print("Cantidad de acompañantes","reserva","[",ñ+1,"]")
                    canta = int(input(" > "))
                    print(" ")
                    print(" 【CHECK IN】 ")
                    print(" ")
                    h[posr]["checkin"]["dia"] = int(input("Dia > "))
                    check_in = h[posr]["checkin"]["dia"]
                    o[posr]["checkin"] = check_in
                    h[posr]["checkin"]["mes"] = int(input("Mes > "))
                    o[posr]["checkin"]["mes"] = h[posr]["checkin"]["mes"]
                    p = check_in
                    pcancel = check_in
                    print(" ")
                    print(" 【CHECK OUT】 ")
                    print(" ")

                    check_out = int(input("Dia > "))
                    total = check_out - check_in
                    h[posr]["checkout"]["dia"] = check_out
                    o[posr]["checkout"]["dia"] = check_out
                    h[posr]["checkout"]["mes"] = int(input("Mes > "))
                    o[posr]["checkout"]["mes"] = h[posr]["checkout"]["mes"]
                    k = check_out

                    print(" ")
                    print(" 【TIPOS DE HABITACIONES】 ")
                    print(" ")
                    print(" ➠ Doble")
                    print(" ➠ Triples")
                    print(" ➠ Cuadruples")
                    print(" ")
                    print("Ingrese el tipo de habitacion con la inicial de la letra")
                    x = input(" > ")
                    i = 0
                    if x == T[i]["tipo"]:
                        factura = "Habitación Triple"
                        precio = 1500
                        tipo = "T"
                        if canta > 3:
                            print("Superaste la cantidad de huspedes para la habitacion disponibles, Vuelva a elegir un tipo de habitacion correspondiente al nro de huspedes ")
                        else:
                            i = 0
                            while i < 8:
                                B = 0
                                if x == T[i]["tipo"]:
                                    j = 0
                                    while j < 30:
                                        if T[i]["est_d"][j] != "D":
                                            B = 1
                                        j = j + 1
                                if B == 1:
                                    print(" ")
                                else:
                                    """print("dia", j + 1, "08", "2022")"""
                                    print("Habitacion disponible > ", "[", T[i]["nro_h"], "]", end=" ")
                                    print("")
                                    print("------------------------------------")
                                i = i + 1

                            nnrohab = int(input("Nro de habitacion > "))
                            h[posr]["nro_habitacion"] = nnrohab
                            o[posr]["nroh"] = nnrohab
                            i = 0
                            while i < 8:
                                if T[i]["nro_h"] ==  nnrohab:
                                    pos = i
                                    if x == T[i]["tipo"]:
                                        while p <= k:
                                            if T[pos]["est_d"][p] == "D":
                                                T[pos]["est_d"][p] = "R"
                                            p = p + 1
                                i = i + 1                                  
                    i = 0
                    if x == C[i]["tipo"]:
                        factura = "Habitación Cuadruple"
                        precio = 2000
                        tipo = "C"
                        if canta > 4:
                            print("Superaste la cantidad de huspedes para la habitacion disponibles, Vuelva a elegir un tipo de habitacion correspondiente al nro de huspedes ")
                        else:
                            i = 0
                            while i < 7:
                                B = 0
                                if x == C[i]["tipo"]:
                                    j = 0
                                    while j < 30:
                                        if C[i]["est_d"][j] != "D":
                                            B = 1
                                        j = j + 1
                                if B == 1:
                                    print(" ")
                                else:
                                    """print("dia", j + 1, "08", "2022")"""
                                    print("Habitacion disponible > ", "[", C[i]["nro_h"], "]", end=" ")
                                    print("")
                                    print("------------------------------------")
                                i = i + 1
                                
                            nnrohab = int(input("Nro de habitacion > "))
                            h[posr]["nro_habitacion"] = nnrohab
                            o[posr]["nroh"] = nnrohab         
                            i = 0
                            while i < 7:
                                if C[i]["nro_h"] ==  nnrohab:
                                    pos = i
                                    if x == C[i]["tipo"]:
                                        while p <= k:
                                            if C[pos]["est_d"][p] == "D":
                                                C[pos]["est_d"][p] = "R"
                                            p = p + 1
                                i = i + 1

                    i = 0
                    if x == D[i]["tipo"]:
                        factura = "Habitación Doble"
                        precio = 1000
                        tipo = "D"
                        if canta > 2:
                            print("Superaste la cantidad de huspedes para la habitacion disponibles, Vuelva a elegir un tipo de habitacion correspondiente al nro de huspedes ")
                        else:
                            i = 0
                            while i < 10:
                                B = 0
                                if x == D[i]["tipo"]:
                                    j = 0
                                    while j < 30:
                                        if D[i]["est_d"][j] != "D":
                                            B = 1
                                        j = j + 1
                                if B == 1:
                                    print(" ")
                                else:
                                    """print("dia", j + 1, "08", "2022")"""
                                    print("Habitacion disponible > ", "[", D[i]["nro_h"], "]", end=" ")
                                    print("")
                                    print("------------------------------------")
                                i = i + 1
                                
                            nnrohab = int(input("Nro de habitacion > "))
                            h[posr]["nro_habitacion"] = nnrohab
                            o[posr]["nroh"] = nnrohab
                            i = 0
                            while i < 10:
                                if D[i]["nro_h"] ==  nnrohab:
                                    pos = i
                                    if x == D[i]["tipo"]:
                                        while p <= k:
                                            if D[pos]["est_d"][p] == "D":
                                                D[pos]["est_d"][p] = "R"
                                            p = p + 1
                                i = i + 1  
            
            else:
                print(" No puede ingresar 0 ")
            print(" ")
            print("💳 【Detalles de pago】 ")  
            print(" ")
            nrotarjeta = int(input("Numero de tarjeta > "))
            if nrotarjeta > 1000000000000000 and nrotarjeta < 9999999999999999:
                contdim = 0
                h[posr]["tarjeta"]["nrot"] = nrotarjeta
                h[posr]["tarjeta"]["fechavencimiento"] = int(input("Fecha de vencimiento MM/YY > "))
                h[posr]["tarjeta"]["cod"] = int(input("CVV > "))
                print(" ")
                print("Espera mientras procesamos el pago ...")
                print(" ")
                for kl in tqdm(range(20)):
                    sleep(.1)
                clear()
                print(" ")
                print(h[posr]["nombre"], h[posr]["apellido"],"¡Su pago fue acreditado con exito! Espere unos minutos para terminar con la reserva.")
                print(" ")
                print("Lo esperamos el dia",check_in,"/",check_out,"Muchas gracias por elegirnos")
                contdim = contdim + 1
            else:
                print("El numero de tarjeta no es valida, intente nuevamente")
            return check_in,canta,p,k,x,pcancel,total,factura,precio,contdim,tipo
                
def checkin(h,hab,nh,check_in,canta,x,dni,k):

    #retornar en el modulo reserva la cant de acompañantes
    print(" ")
    hab = int(input("Ingrese el numero de habitacion que elegiste al hacer la reserva > "))
    # if check_in == day:
    i = 0
    b = 0
    while i < nh and b == 0:
        if h[i]["dni"] == dni:
            pos = i
            hab = h[i]["nro_habitacion"]
            print(" ")
            print("Hola,",h[pos]["nombre"],h[pos]["apellido"])
            print(" ")
            p = check_in
            if canta == 0:
                print(" ")
                print("Diríjase a su habitacion nro: ",hab,"para acceder solo scanee el CodigoQr que le saldrá en la pantalla de su puerta")
                for i in range(0,10):
                    if D[i]["nro_h"] ==  hab:
                        pos = i
                        print(pos)
                        if x == D[i]["tipo"]:
                            while p <= k:
                                if D[pos]["est_d"][p] == "R":
                                    D[pos]["est_d"][p] = "O"
                                p = p + 1
                for i in range(0,7):
                    if C[i]["nro_h"] ==  hab:
                        pos = i
                        if x == C[i]["tipo"]:
                            while p <= k:
                                if C[pos]["est_d"][p] == "R":
                                    C[pos]["est_d"][p] = "O"
                                p = p + 1
                for i in range(0,8):
                    if T[i]["nro_h"] ==  hab:
                        pos = i
                        if x == T[i]["tipo"]:
                            while p <= k:
                                if T[pos]["est_d"][p] == "R":
                                    T[pos]["est_d"][p] = "O"
                                p = p + 1
            else:
                print(" Por favor inserte los datos de sus acompañantes ")
                for i in range(0,canta):
                    ac[i]["dni"] = dni
                    ac[i]["nom_acomp"] = str(input("Nombre >  "))
                    ac[i]["ap_acomp"] = str(input("Apellido > "))
                    print(" ")
                    print("📅 Fecha de nacimiento", "<", ac[i]["nom_acomp"], ">")
                    print(" ")
                    ac[i]["fecha_acomp"]["dia"] = input("Dia > ")
                    ac[i]["fecha_acomp"]["mes"] = input("Mes > ")
                    ac[i]["fecha_acomp"]["anio"] = input("Año > ")
                for i in range(0,10):
                    if D[i]["nro_h"] ==  hab:
                        pos = i
                        print(pos)
                        if x == D[i]["tipo"]:
                            while p <= k:
                                if D[pos]["est_d"][p] == "R":
                                    D[pos]["est_d"][p] = "O"
                                p = p + 1
                for i in range(0,7):
                    if C[i]["nro_h"] ==  hab:
                        pos = i
                        if x == C[i]["tipo"]:
                            while p <= k:
                                if C[pos]["est_d"][p] == "R":
                                    C[pos]["est_d"][p] = "O"
                                p = p + 1
                for i in range(0,8):
                    if T[i]["nro_h"] ==  hab:
                        pos = i
                        if x == T[i]["tipo"]:
                            while p <= k:
                                if T[pos]["est_d"][p] == "R":
                                    T[pos]["est_d"][p] = "O"
                                p = p + 1
                clear()
                print("")
                print("¡Datos cargados con exito!")
                print(" ")
                print("Diríjase a su habitacion nro: ",hab," para acceder solo scanee el CodigoQr que le saldrá en la pantalla de su puerta")
            b = 1
        i = i + 1
          
    

def clear(): #! este
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def cancelar_reserva(h,hab,nh,p,k,mh,day,pcancel,dni):
    print(" ")
    print("Opcion【 Si 】 ","|","Opcion【 No 】 ")
    print(" ")
    print("Al cancelar la reserva, ud debe tener en cuenta que si canceló antes o el mismo dia del check in, recibirá una multa")
    print(" ")
    print("¿Esta seguro de cancelar su reserva?")
    opcancel = str(input(" > "))
    i = 0
    if opcancel == "si":
        print("Para continuar, ingrese su numero de habitacion >  ")
        nroh = int(input("nroh > "))
        b = 0
        while i < nh and b == 0:
            if h[i]["nro_habitacion"] == nroh:
                poscancel = i
                print(" ")
                print("¡Habitación encontrada con exito!",h[poscancel]["nro_habitacion"])
                print(" ")
                print("Aguarde un momento mientras verificamos sus datos para continuar ...")
                for i in tqdm(range(20)):
                    sleep(.1)
                for i in range(0,8):
                    if T[i]["nro_h"] ==  nroh:
                        pos = i
                        if nroh == T[i]["nro_h"]:
                            while p <= k:
                                if T[pos]["est_d"][p] == "R":
                                    T[pos]["est_d"][p] = "D"
                                p = p + 1
                for i in range(0,7):
                    if C[i]["nro_h"] ==  nroh:
                        pos = i
                        if nroh == C[i]["nro_h"]:
                            while p <= k:
                                if C[pos]["est_d"][p] == "R":
                                    C[pos]["est_d"][p] = "D"
                                p = p + 1
                for i in range(0,10):
                    if D[i]["nro_h"] ==  nroh:
                        pos = i
                        if nroh == D[i]["nro_h"]:
                            while p <= k:
                                if D[pos]["est_d"][p] == "R":
                                    D[pos]["est_d"][p] = "D"
                                p = p + 1
                
                calculomulta = pcancel - day
                if calculomulta < 2:
                    mh[poscancel]["monto"] = 5000
                    mh[poscancel]["fecha"]["dia"] = day
                elif day == pcancel:
                    mh[poscancel]["monto"] = 5000
                    mh[poscancel]["fecha"]["dia"] = day
                else:
                    mh[poscancel]["monto"] = 0
                print(" ")
                clear()
                print(" ")
                print(" ¡Reserva cancelada con exito! ")
                b = 1
            i = i + 1
    else:
        clear()

def check_out(h,nh,dni,total,factura,precio):
    B=0
    i=0
    while i < nh and B==0:
        if dni == h[i]["dni"]:
            pos=i
            print(" ")
            print ("Hola",h[pos]["nombre"],"",h[pos]["apellido"])
            print(" ")
            print("¿Desea imprimir la factura?")
            print("【 Si 】 ","|","【 No 】 ")
            print(" ")
            op = str(input(" > "))
            if op == "si":
                clear()
                print("----------------------------------------------------------------------")
                print("Hotel California","                        ","Factura B               ")
                print("Cuit: 20-98786564-3","                                                ")
                print("I.V.A. RESPONSABLE INSCRIPTO                                          ")
                print("----------------------------------------------------------------------")
                print("                                                ","Fecha:", format(dia.day),"/",format(dia.month),"/",format(dia.year))
                print("----------------------------------------------------------------------")
                print("Señor:",h[pos]["nombre"],h[pos]["apellido"],"    ","DNI:", h[pos]["dni"])
                print("----------------------------------------------------------------------")
                print("Domicilio", h[pos]["direccion"]["calle"], h[pos]["direccion"]["nro"],"-", h[pos]["direccion"]["localidad"])
                print("----------------------------------------------------------------------")
                print("Estadia/Dias","      ", "Descripción","      ", "Precio Unitario","      ", "Importe","     ")
                print("  ",total,"             ",factura,"          ","$",precio,"        ", "$",precio*total)
            B=1
        i=i+1

    if B==0:
        print (" ¡Dni no encontrado! ")


def informemapahotel(hab):
    print(" ")
    print("「🏨」MAPA HOTEL ")
    i = 0
    if D[i]["tipo"] == "D":
        print(" ")
        print("➥ Habitacion Doble")
        for i in range(0,10):
            print(" ")
            print("╭─────────────────────────────────────────────────────────────────────────────────────────────────✧")
            print("│Numero habitacion:",D[i]["nro_h"],"[",D[i]["est_d"],"]","Estado:",D[i]["est_h"])
            print("╰─────────────────────────────────────────────────────────────────────────────────────────────────✧")
    i = 0
    if T[i]["tipo"] == "T":
        print(" ")
        print("➥ Habitacion Triple")
        for i in range(0,8):
            print(" ")
            print("╭─────────────────────────────────────────────────────────────────────────────────────────────────✧")
            print("│Numero habitacion:",T[i]["nro_h"],"[",T[i]["est_d"],"]","Estado:",T[i]["est_h"])
            print("╰─────────────────────────────────────────────────────────────────────────────────────────────────✧")
    i = 0
    if C[i]["tipo"] == "C":
        print(" ")
        print("➥ Habitacion Cuadruple")
        for i in range(0,7):
            print(" ")
            print("╭─────────────────────────────────────────────────────────────────────────────────────────────────✧")
            print("│Numero habitacion:",C[i]["nro_h"],"[",C[i]["est_d"],"]","Estado:",C[i]["est_h"])
            print("╰─────────────────────────────────────────────────────────────────────────────────────────────────✧")
    


def habilitar_deshabilitar(hab):
    print(" ")
    print("Habilitar【1】","|","Deshabilitar【2】")
    ophab = int(input(" > "))
    print(" ")
    print("Ingrese el numero de habitacion que desea habilitar")
    habitacion = int(input(" > "))
    if ophab == 1:
        i = 0
        b = 0
        while i < 10 and b == 0:
            if D[i]["nro_h"] == habitacion:
                pos = i
                if D[pos]["est_h"] == "Deshabilitada":
                    D[pos]["est_h"] = "Habilitada"
                    clear()
                    print(" ")
                    print("La habitacion",habitacion,"fue habilitada correctamente")
                    b = 1
                else:
                    clear()
                    print("¡La habitacion ya esta habilitada!")
            i = i + 1
        i = 0
        b = 0
        while i < 7 and b == 0:
            if T[i]["nro_h"] == habitacion:
                pos = i
                if T[pos]["est_h"] == "Deshabilitada":
                    T[pos]["est_h"] = "Habilitada"
                    clear()
                    print(" ")
                    print("La habitacion",habitacion,"fue habilitada correctamente")
                    b = 1
                else:
                    clear()
                    print("¡La habitacion ya esta habilitada!")
            i = i + 1
        i = 0
        b = 0
        while i < 8 and b == 0:
            if C[i]["nro_h"] == habitacion:
                pos = i
                if C[pos]["est_h"] == "Deshabilitada":
                    C[pos]["est_h"] = "Habilitada"
                    clear()
                    print(" ")
                    print("La habitacion",habitacion,"fue habilitada correctamente")
                    b = 1
                else:
                    clear()
                    print("¡La habitacion ya esta habilitada!")
            i = i + 1
    if ophab == 2:
        i = 0
        b = 0
        while i < 10 and b == 0:
            if D[i]["nro_h"] == habitacion:
                pos = i
                if D[pos]["est_h"] == "Habilitada":
                    D[pos]["est_h"] = "Deshabilitada"
                    clear()
                    print(" ")
                    print("La habitacion",habitacion,"fue Deshabilitada correctamente")
                    b = 1
                else:
                    clear()
                    print("¡La habitacion ya esta Deshabilitada!")
            i = i + 1
        i = 0
        b = 0
        while i < 8 and b == 0:
            if T[i]["nro_h"] == habitacion:
                pos = i
                if T[pos]["est_h"] == "Habilitada":
                    T[pos]["est_h"] = "Deshabilitada"
                    clear()
                    print(" ")
                    print("La habitacion",habitacion,"fue Deshabilitada correctamente")
                    b = 1
                else:
                    clear()
                    print("¡La habitacion ya esta Deshabilitada!")
            i = i + 1
        i = 0
        b = 0
        while i < 7 and b == 0:
            if C[i]["nro_h"] == habitacion:
                pos = i
                if C[pos]["est_h"] == "Habilitada":
                    C[pos]["est_h"] = "Deshabilitada"
                    clear()
                    print(" ")
                    print("La habitacion",habitacion,"fue Deshabilitada correctamente")
                    b = 1
                else:
                    clear()
                    print("¡La habitacion ya esta Deshabilitada!")
            i = i + 1
        
def informes(h,nh, check_in,day, ac):
    print(" ")
    print("Informes de reservas【1】 ","|","Informes menores de edad【2】","|","Mapa habitaciones【3】","|","Habilitar/Deshabilitar Habitaciones【4】")
    op = int(input(" > "))
    if op == 1:
        i = 0
        while i < nh:
            if day == check_in:
                if check_in == h[i]["checkin"]["dia"]:
                    print(" ")
                    print(h[i]["nombre"],h[i]["apellido"],h[i]["dni"],h[i]["nro_habitacion"],"📅",dia.day,"/",dia.month)
                    print("-------------------------------------------------------")
            i = i + 1
    if op == 2:
        i = 0
        while i < nh:
                if day == check_in:
                    if check_in == h[i]["checkin"]["dia"]:
                        ordenarnombres(h, ac, nh)
                        print(" ")
                        print("INFORME DE MENORES DE EDAD DEL DIA","📅",dia.day,"/",dia.month)
                        print("-------------------------------------------------------")
                        print("Habitacion:", h[i]["nro_habitacion"],"     ", "Huesped a cargo: ",  h[i]["nombre"],  h[i]["apellido"])
                        print("DNI:",  h[i]["dni"])
                        print("-------------------------------------------------------")
                        print("Documento", o)
                i = i + 1
    if op == 3:
        informemapahotel(hab)
    if op == 4:
        habilitar_deshabilitar(hab)



def huespedes_aus(o,nh,contdim): #! este
    print(" ")
    print(" 【HUESPEDES ASUSENTES】")
    print(" ")
    for i in range(0,2):
        if o[i]["checkin"]["dia"] < dia.day:
            print(o[i]["dni"],"Nroh:",o[i]["nroh"],"Check In:",o[i]["checkin"]["dia"],"/",o[i]["checkin"]["mes"],"Check Out:",o[i]["checkout"]["dia"],"/",o[i]["checkout"]["mes"])
            mh[i]["dni"] = o[i]["dni"]
            mh[i]["fecha"]["dia"] = dia.day
            mh[i]["fecha"]["mes"] = dia.month
            mh[i]["monto"] = mh[i]["monto"] + 2000
            print("¡Fue multado exitosamente!")
            print("----------------------------------------------------------")

def tareas_diarias(h,nh, check_out,contdim,tipo): 
    print("")
    print("Extension de estadia【1】 ","|","Huespedes ausentes【2】")
    op = int(input(" > "))
    if op == 1:
        print(" ")
        dni = int(input("Dni > "))
        i = 0
        while i < nh:
            if dni == h[i]["dni"]:
                # for j in range(0,):
                #     print(o[i]["nroh"])
                if check_out == h[i]["checkout"]["dia"]:
                    #ciclo infinito
                    print(" ")
                    print("Seleccione la habitacion que desea actualizar")
                    x = int(input((" > ")))
                    print(" ")
                    diashasta = int(input("Ingrese hasta que dia desea extender > "))
                    busquedahabs (hab, nh, x, diashasta, check_out, tipo)
            i = i + 1
    if op == 2:
        acces = loginadmin()
        if acces == "valido":
            print(" ")
            print(" ✅【Logueado exitosamente】 ")
            huespedes_aus(o,nh,contdim)
        else:
            print(" ")
            print(" ⛔【Acceso invalido】")

                    
def busquedahabs (hab, nh, x, diashasta, check_out,tipo): 
    i = 0
    B = 0
    B2 = 1
    p = check_out
    k = diashasta
    if tipo == "T":
        while i < 8 and B == 0:
            if T[i]["nro_h"] == x:
                B = 1
                posi = i
            i = i + 1
        while check_out <= diashasta:
            if T[posi]["est_d"][check_out] == "D":
                B2 = 0
            check_out = check_out + 1
        if B2 == 1:
            print("")
        else:
            clear()
            print(" ")
            print(" ✅【Estadia extendida con exito】 ")
        while p <= k:
            if T[posi]["est_d"][p] == "D":
                T[posi]["est_d"][p] = "O"
            p = p + 1

    if tipo == "C":
        while i < 8 and B == 0:
            if C[i]["nro_h"] == x:
                B = 1
                posi = i
            i = i + 1
        while check_out <= diashasta:
            if C[posi]["est_d"][check_out] == "D":
                B2 = 0
            check_out = check_out + 1
        if B2 == 1:
            print("")
        else:
            clear()
            print(" ")
            print(" ✅【Estadia extendida con exito】 ")
        while p <= k:
            if C[posi]["est_d"][p] == "D":
                C[posi]["est_d"][p] = "O"
            p = p + 1

    if tipo == "D":
        while i < 8 and B == 0:
            if D[i]["nro_h"] == x:
                B = 1
                posi = i
            i = i + 1
        while check_out <= diashasta:
            if D[posi]["est_d"][check_out] == "D":
                B2 = 0
            check_out = check_out + 1
        if B2 == 1:
            print("")
        else:
            clear()
            print(" ")
            print(" ✅【Estadia extendida con exito】 ")
        while p <= k:
            if D[posi]["est_d"][p] == "D":
                D[posi]["est_d"][p] = "O"
            p = p + 1

def mostrar_menuppal(): #! este
    print(" ")
    print("- Bienvenido al sistema automatico de menu para usuarios - ")
    print(" ")
    print("📅",format(dia.day),"/",format(dia.month),"/",format(dia.year))
    print(" ")
    print("✦                      MENU HUESPEDES                       ✦")
    print("✧═══════════════════════════✧════════════════════════════✧")
    print("➀ ➤ Registro al sistema: ")
    print("➁ ➤ Reserva: ") 
    print("➂ ➤ Cancelar reserva: ")
    print("➃ ➤ Check In: ") 
    print("➄ ➤ Servicios: ") #! No completado
    print("➅ ➤ Check Out: ")
    print("➆ ➤ Informes: ") 
    print("➇ ➤ Tareas diarias: ") #! No completado
    print("➈ ➤ Limpiar ")
    print("➉ ➤ Salir ")

def login(h,nh,acces): #! este
    print(" ")
    print(" 🔒【LOG IN】")
    print(" ")
    dni = int(input(" Dni > "))
    clave = input(" Clave > ")
    print(" ")
    for i in range (0,nh):
        if h[i]["dni"] == dni:
            if h[i]["clave"] == clave:
                acces = "valido"
            else: 
                acces = "invalido"
    return acces,dni

def menu_servicios(): #! este
    print("Ingrese el servicio que desee > ")
    print("➀ ➤ Gimnasio")
    print("➁ ➤ Spa")
    print("➂ ➤ Room-Service")
    print("➃ ➤ Bar")
    print("➄ ➤ Frigobar")
    print("➅ ➤ Lavandería")
    print("➆ ➤ Mostrar Pila")
    print("➇ ➤ Salir")

#programa principal
pos_check= 0
salir = False
paso = False

def impr(h):
    for i in range(0,2):
        print(h[i]["dni"])
        print(h[i]["clave"])
        print(h[i]["nombre"])
        print(h[i]["apellido"])

p = 0
while not salir:
    mostrar_menuppal()
    print(" ")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        B = 0
        dni_valido = validacion(h,nh,B)
        registro_sistema(h, hab, nh, dni_valido,p)
        p = p + 1
        paso = True
    elif op == 2:
        acces = "invalido"
        a,dni = login(h,nh,acces)
        if a == "valido":
            print(" ")
            print(" ✅【Logueado exitosamente】 ")
            check_in,canta,p,k,x,pcancel, total, factura, precio,contdim,tipo = reserva(h, hab,dni)
        else:
            print(" ")
            print(" ⛔【Acceso invalido】")
    elif op == 3:
        acces = "invalido"
        a,dni = login(h,nh,acces)
        if a == "valido":
            print(" ")
            print(" ✅【Logueado exitosamente】 ")
            cancelar_reserva(h,hab,nh,p,k,mh,day,pcancel,dni)
        else:
            print(" ")
            print(" ⛔【Acceso invalido】")
    elif op == 4:
        acces = "invalido"
        a,dni = login(h,nh,acces)
        if a == "valido":
            print(" ")
            print(" ✅【Logueado exitosamente】 ")
            checkin(h,hab,nh,check_in,canta,x,dni,k)
        else:
            print(" ")
            print(" ⛔【Acceso invalido】")
    elif op == 5:
        ej = True
        while ej:
            menu_servicios()
            op = int(input(">"))
            ej = carga_pila(ej, op, s, pila, pilaux)
    elif op == 6:
        acces = "invalido"
        a,dni = login(h,nh,acces)
        if a == "valido":
            print(" ")
            print(" ✅【Logueado exitosamente】 ")
            check_out(h, nh,dni, total, factura, precio)
    elif op == 7:
        acces = loginadmin()
        if acces == "valido":
            print(" ")
            print(" ✅【Logueado exitosamente】 ")
            informes(h, nh, checkin,day, ac)
        else:
            print(" ")
            print(" ⛔【Acceso invalido】")
            
    elif op == 8:
        tareas_diarias(o,nh, k,contdim,tipo)
    elif op == 9:
        impr(h)
        #clear()
    elif op== 10:
        salir = True
    else:
        print("⛔【Opción inválida】")




