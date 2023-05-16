"""
    Ethan Grané Garcia
    Criptografia classica
        Metodo Cesar
        
    El metodo cesar consiste en cojer una palabra (HOLA)
    y saltar x letras en el alfabeto (x = 1, HOLA = IPMB) 
"""
#********** FUNCIONES **********#
#Traduce la letra a su posicion en el alfabeto (A = 1, B = 2, C = 3)
def letras_a_numeros(letra):
    if not isinstance(letra, str) or len(letra) != 1:
        raise ValueError("La entrada debe ser una letra mayúscula del alfabeto latino.")
    
    return ord(letra) - 64  # La función ord() devuelve el valor numérico del código ASCII de la letra.

#traduce el numero a la letra correspondiente en el abecedario
def numeros_a_letras(numero):
    while(numero < 0):
        numero += 26
    while(numero > 26):
        numero -= 26
    
    if not isinstance(numero, int) or numero < 1 or numero > 26:
        raise ValueError("La entrada debe ser un número entero entre 1 y 26.")
    
    return chr(numero + 64)  # La función chr() devuelve la letra correspondiente al valor numérico del código ASCII.

#Separa un string letra por letra en una lista
def separar_por_letras(cadena):
    if not isinstance(cadena, str):
        raise ValueError("La entrada debe ser una cadena de caracteres.")
    
    return list(cadena)

#********** PROGRAMA **********#
a = input("Mensaje: ")
c = int(input("Jumps: "))

list_a = separar_por_letras(a)

list_num_a = []
list_msg = []

"""
    Convierte letras a numeros
"""
for ia in list_a:
    list_num_a.append(letras_a_numeros(ia))

"""
    Convierte de numero a letras
"""
for ib in list_num_a:
    list_msg.append(numeros_a_letras(ib + c))

print("".join(list_msg))
input()
