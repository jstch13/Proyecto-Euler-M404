#Problema 071 - Fracciones Ordenadas
#Enunciado: https://projecteuler.net/problem=71
#Nivel de Dificultad: d = 2
#Puntos: p(d,n) = 6
#Tiempo observado en Colab (CPU): 0.000000 s
#Estrategia: La mejor aproximacion usando el multiplicador mayor que se usar

n_i = input("escriba el número del cual se desea hallar la fraccion mas cercana por la izquierda" \
"primero numerador y luego denominador ")
numerador, denominador = n_i.split()

ad = float(numerador)/float(denominador)
#como el denominador mayor es d menor a 1000000, entonces tendra que usarse d = 999999
n_m = int((ad)*1000000)
#como 1 millon no esta permitido, la relacion entre el valor n_f con un millon 
#es practicamente la misma entre n_f-1 y 999999, pues son numeros bastante grandes

n_f = n_m - 1
print(n_f)