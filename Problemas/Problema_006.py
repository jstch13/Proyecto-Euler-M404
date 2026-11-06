#Problema 006 - Suma de las diferencias cuadradas
#Enunciado: https://projecteuler.net/problem=6
#Nivel de Dificultad: d = 0
#Puntos: p(d,n) = 1
#Tiempo observado en Colab (CPU): 0.000000 s
#Estrategia: Usando Formulas conocidas para simplificar los calculos 

n_1 = input("El número superior: ")

#lo volvemos entero
n = int(n_1)

#usando formulas conocidas de suma de cuadrados y sumara de enteros 
#n(n+1)/2 y n(n+1)(2n+1)/6
n_f = (n*(n+1)/2)**2 - (n*(n+1)*(2*n+1)/6)

print(n_f)