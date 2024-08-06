# ANAGRAMA

# Escribe una funcion que reciba dos pálabras y retorne verdadero o falso segun sea o n o anagrama, 
# Un anagrama consiste en formar una palabra reordenando todas las letras de otra palabra inicial,
# No hace falta comprobar que ambas palabras existen, 
# Dos palabras exactamentes iguales no son anagramas. 


def sonAnagramas(palabra1, palabra2):
    # Verificar si las álabras son exactamentes iguales 
    if palabra1 == palabra2:
        return False
    # Verificar si al ordenar las letras de ambas palabras obtenemos el mismo resultado
    return sorted(palabra1) == sorted(palabra2)

# Solicitar las palabras al usuario 
palabra1 = input("ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

# Verificar si son anagramasd y mostrar el resultado
if sonAnagramas(palabra1, palabra2):
    print(f"las palabras '{palabra1}' y '{palabra2}' son anagramas")

else:
    print("Las palabras no son anagramas")
