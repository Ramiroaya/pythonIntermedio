 # Escribe un programa que intente dividir dos números. Si el segundo número es cero,captura la excepción ZeroDivisionError
 #  y muestra un mensaje de error al usuario.

def dividir(dividendo, divisor):
    try:
        dividendo = int(dividendo)
        divisor = int(divisor)
        resultado = dividendo / divisor
    except ValueError:
        print("Error: Ingrese valores numericos para el dividendo y/o divisor.")
    except ZeroDivisionError:
        print("Error: El divisor no puede ser 0.")
    else:
        print(f"El resultado de la division es:  {resultado}")   


dividendo = input('Ingrese el dividendo: ')
divisor = input('Ingrese el divisor: ')
dividir(dividendo,divisor)


 # Escribe un programa que intente sumar un número y una cadena. Si se produce un errorde tipo, captura la excepción TypeError 
 # y muestra un mensaje de error al usuario.


def sumar(numero, cadena):
    try:
        resultado = numero + cadena
    except TypeError:
        print("Error: Ingrese un tipo de dato numerico para numero y cadena.")
    else:
        print(f"La suma es:  {resultado}")

numero = 120
cadena = "abc"
sumar(numero,cadena)

 # Escribe un programa que intente acceder a una clave que no existe en undiccionario. Si se produce una excepción KeyError, 
 # captura la excepción y muestraun mensaje de error al usuario.



def acceder(diccionario, indice):
    try:
        indice = int(indice)
        resultado = diccionario[indice]
    except ValueError:
        print("Error: Ingrese un valor numerico para el indice.")
    except KeyError:
        print("Error: El indice ingresado no existe en el diccionario.")
    else:
        print(f"la clave en ese indice es:   {resultado}")

diccionario = {0:'azul', 1:'rojo', 2:'verde', 3:'amarillo'}
indice = input("Ingrese el indice a buscar:  ")
acceder(diccionario,indice)


 # Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepciónFileNotFoundError,
 # captura la excepción y muestra un mensaje de error al usuario. Sinembargo, también intenta crear el archivo si no existe.
 





 # Escribe un programa que intente dividir dos números. Si el segundo número es cero,captura la excepción ZeroDivisionError. 
 # Si el primer número es un número no válido,captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

def dividir(dividendo, divisor):
    try:
        dividendo = int(dividendo)
        divisor = int(divisor)
        if divisor == 0:
            
