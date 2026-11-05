#Problema 001 - Multiplos de 3 0 5
#Enunciado: https://projecteuler.net/problem=1
#Nivel de Dificultad: d = 0
#Puntos: p(d,n) = 1
#Tiempo observado en Colab (CPU): 0.000000 s
#Estrategia: Usando el prinicipio de inclusion y exclusion contar y eliminar repetidos

n = int(input("escribe la cota superior (N): " ))
a = int(input("escribe el primer criterio de divisibilidad: "))
b = int(input("escribe el segundo criterio de divisibilidad: "))
#aub = a + b - anb por principio de inclusion-exclusion

n_a = (a)*((n-1)//a)*((n-1)//a + 1)*(1/2)
n_b = (b)*((n-1)//b)*((n-1)//b + 1)*(1/2)
n_ab =(a*b)*((n-1)//(a*b))*((n-1)//(a*b) + 1)*(1/2)

#calcula la diferencia de inclusion y exclusion
n_fin = n_a + n_b - n_ab

print(n_fin)