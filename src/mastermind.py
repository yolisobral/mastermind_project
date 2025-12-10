import random 
tamaño_genes = 4
valores_posibles = ['AMARILLO', 'AZUL', 'ROJO', 'VERDE', 'NARANJA', 'MORADO']
tamaño_populacion = 100
tasa_mutacion = 0.1

def crear_codigo_secreto ():
    codigo = []
    for posicion in range (tamaño_genes):
        valores_posibles = ['AMARILLO', 'AZUL', 'ROJO', 'VERDE', 'NARANJA', 'MORADO']
        valor = random.choice (valores_posibles)
        codigo.append (valor)
    return codigo
# random.choice() permite obtener un número entero aleatorio de esa secuencia especificada (inicio, fin, paso), en lugar de iterar sobre todos los números, generando así   valores enteros que caen dentro de un rango definido por el usuario. 

def crear_individuo ():
    individuo = []
    for posicion in range (tamaño_genes):
        valor = random.choice (valores_posibles)
        individuo.append (valor)
    return individuo

def crear_poblacion ():
    poblacion = []
    for individuo in range (tamaño_populacion):
        individuo = crear_individuo ()
        poblacion.append (individuo)
    return poblacion






if __name__ == "__main__":
    codigo_secreto = crear_codigo_secreto ()
    print ("Código secreto:", codigo_secreto)

    poblacion_inicial = crear_poblacion ()
    print ("Población inicial:")
    for individuo in poblacion_inicial:
        print (individuo)