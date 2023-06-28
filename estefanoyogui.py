# -*- coding: utf-8 -*-
"""EstefanoYogui

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rcDUZQXlfMsY4qa3iPP-Z44MVOdOpdQE
"""

personas = []

def verificar_nif(nif):
    letras_validas = 'TRWAGMYFPDXBNJZSQVHLCKE'
    nif = nif.upper().strip()

    if len(nif) != 9 or not nif[:-1].isdigit() or not nif[-1].isalpha():
        return False

    letra = nif[-1]
    numeros = int(nif[:-1])
    indice = numeros % 23

    if letras_validas[indice] == letra:
        return True
    else:
        return False

def grabar_persona():
    nif = input("Ingrese el NIF: ")
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))

    if verificar_nif(nif) and len(nombre) >= 8 and edad >= 0:
        persona =
            "NIF": nif,
            "Nombre": nombre,
            "Edad": edad

        personas.append(persona)
        print("Datos guardados correctamente.")
    else:
        print("Error: Los datos no cumplen los requisitos.")

def buscar_persona():
    nif_buscar = input("Ingrese el NIF de la persona a buscar: ")

    for persona in personas:
        if persona["NIF"] == nif_buscar:
            print("Información de la persona:")
            print("NIF:", persona["NIF"])
            print("Nombre:", persona["Nombre"])
            print("Edad:", persona["Edad"])

            if persona["NIF"][:2] == "ES":
                print("La persona pertenece a la Unión Europea.")
            else:
                print("La persona no pertenece a la Unión Europea.")
            return

    print("No se encontró ninguna persona con el NIF proporcionado.")

def imprimir_certificados():
    certificados = {
        "Certificado de Nacimiento": ["Fecha de Nacimiento", "Lugar de Nacimiento"],
        "Certificado de Estado Conyugal": ["Estado Conyugal"],
        "Certificado de Pertenencia a la Unión Europea": []
    }

    for persona in personas:
        print("Nombre:", persona["Nombre"])
        print("NIF:", persona["NIF"])

        for certificado, datos in certificados.items():
            print("---", certificado, "---")
            if certificado == "Certificado de Nacimiento":
                print("Fecha de Nacimiento:", random.randint(1, 31), "/", random.randint(1, 12), "/", random.randint(1950, 2005))
                print("Lugar de Nacimiento: Ciudad Ejemplo")
            elif certificado == "Certificado de Estado Conyugal":
                print("Estado Conyugal: Soltero(a)")
            elif certificado == "Certificado de Pertenencia a la Unión Europea":
                if persona["NIF"][:2] == "ES":
                    print("La persona pertenece a la Unión Europea.")
                else:
                    print("La persona no pertenece a la Unión Europea.")

            print("--------------------")

    print("Certificados impresos correctamente.")


def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Grabar")
        print("2. Buscar")
        print("3. Imprimir certificados")
        print