#Problema 091 - Triangulos Rectangulos con Coordenadas enteras
#Enunciado: https://projecteuler.net/problem=91
#Nivel de Dificultad: d = 4
#Puntos: p(d,n) = 11
#Tiempo observado en Colab (CPU): 0.000000 s
#Estrategia: Usando la forma vectorial de ellos y defineindo el producto punto

n = int(input("Escriba el tamaño de la cuadrícula: "))

#Si los vectores ya fueran ortogonales serian de la forma (a,0) y (0,b) con a y b 
#variando entre 1 y n los cuales nos dejan n*n vectores
conteo_total = n * n

# Definimos el producto punto como función
def productopunto(u, v):
    return (u[0] * v[0]) + (u[1] * v[1])

# Probano todos los puntos posibles de la cuadricula salvo el (0,0)
puntos = []
for x in range(n + 1):
    for y in range(n + 1):
        if not (x == 0 and y == 0):
            puntos.append((x, y))

total_puntos = len(puntos)

#eliminamos parejas duplicadas
for i in range(total_puntos):
    u = puntos[i]
    x1, y1 = u
    
    for j in range(i + 1, total_puntos):
        v = puntos[j]
        x2, y2 = v
        
#Descartamos las que esten alineadas entre si, usando la definicion de producto cruz y obviando la tercer componente 
        pcruz = (x1 * y2) - (x2 * y1)
        if pcruz != 0:
            
            # Calculamos los vectores diferencia para probar los otros dos vértices y ver si son ortogonales
            v_menos_u = (x2 - x1, y2 - y1)
            u_menos_v = (x1 - x2, y1 - y2)
            
            # Verificamos si hay un ángulo de 90° en el vértice u o en el vértice v
            if productopunto(u, v_menos_u) == 0:
                conteo_total += 1
            elif productopunto(v, u_menos_v) == 0:
                conteo_total += 1

print(f"Total de triángulos rectángulos con un vértice en el origen: {conteo_total}")
