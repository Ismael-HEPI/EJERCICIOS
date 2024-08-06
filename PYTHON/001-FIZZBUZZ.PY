# FIZZ BUZZ 

# Escribe un programa que muestre por consola los numeros de 1 a 100 sustituyendo los siguiente:
# multiplos de 3 por la palabra "fizz",
# multiplos de 5 por la palabra "buzz", 
# multiplos de 3 y 5 a la vez por la palabra "fizzbuzz",


for i in range(1, 100+1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)