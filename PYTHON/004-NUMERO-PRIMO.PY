# NUMEROS PRIMOS 

# ESCRIBE UN PROGRAMA QUE SE ENCARGUE DE COMPROBAR SI UN NUMERO ES O NO PRIMO.
# ECHO ESTO, IMPRIME LOS NUMEROS PRIMOS ENTRE 1 Y 100.


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for j in range(1, 101):
    if es_primo(j):
        print(j)
