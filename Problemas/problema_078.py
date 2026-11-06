#Problema 078 - Particiones de Monedas
#Enunciado: https://projecteuler.net/problem=78
#Nivel de Dificultad: d = 3
#Puntos: p(d,n) = 8
#Tiempo observado en Colab (CPU): 0.000000 s
#Estrategia: 

k = int(input("Escribe el divisor que debe cumplir n: "))

#Usando ideas similares del ejercicio 76
def subgrupos(n):
    sb = [0] * (n + 1)
    sb[0] = 1
    for i in range(1, n + 1):
        j = 1
        signo = 1
        while True:
            pentagonal1 = j * (3 * j - 1) // 2
            pentagonal2 = j * (3 * j + 1) // 2

            if pentagonal1 > i:
                break
            sb[i] += signo * sb[i - pentagonal1]
            if pentagonal2 <= i:
                sb[i] += signo * sb[i - pentagonal2]
            j += 1
            signo = -signo
    return sb[n] 

encontrado = False

#no supe como reducir los limites de busqueda sin que sea haga muy largo la ejecucion del codigo 
#aunque usando algo como k/19 = a y k/18 = b, sirven, solo que no tengo capacidad de computo para hacerlo
a = 55370
b = 55380
for n_i in range(a,b): 
    if subgrupos(n_i) % k == 0:
        print(f"El numero {n_i} es minimo")
        encontrado = True
        break

if not encontrado:
    print("no hay o no existe")
