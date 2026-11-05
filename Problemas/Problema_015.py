#Problema 015 - Caminos Recticulares
#Enunciado: https://projecteuler.net/problem=15
#Nivel de Dificultad: d = 2
#Puntos: p(d,n) = 6
#Tiempo observado en Colab (CPU): 0.000000 s
#Estrategia: Contar como si las felchas fuesen todas distintas usando factoriales
#Luego eliminar los casos repetidos de cada subgrupo de flechas (derecha,abajo)

n_i = int(input("Número de cuadros por lado: "))

#definiendo el factorial: f(n)
def f(n):
    return 1 if n == 0 else n * f(n - 1)

#si fuesen flechas distintas serian 2n!, y eliminar los dos subgrupos de n 
n_f = int((f(2*n_i))/(f(n_i)**2))

print(n_f)