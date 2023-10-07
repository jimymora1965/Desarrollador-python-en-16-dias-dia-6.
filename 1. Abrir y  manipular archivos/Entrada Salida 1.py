
# lee todo lo que esta en el archivo prueba.txt, creando una variable(en  este caso mi_archivo)
""" mi_archivo = open('Prueba.txt')
#leo todas las lineas del archivo:
print(mi_archivo.read())    
mi_archivo.close()  """

print("===============================")

""" #para leer solo una linea:
mi_archivo = open('Prueba.txt')
linea = mi_archivo.readline()
print(linea) """

print("===============================")

#para leer todas las lineas una a una del texto prueba
""" mi_archivo = open('Prueba.txt')
linea = mi_archivo.readline()
print(linea)

linea = mi_archivo.readline()
print(linea)

linea = mi_archivo.readline()
print(linea)
 """
 
""" #para quitar el salto de linea del codigo anterior cuando se imnprima, uso el metodo rstrip()
mi_archivo = open('Prueba.txt')
linea = mi_archivo.readline()
print(linea.rstrip())

linea = mi_archivo.readline()
print(linea.rstrip())

linea = mi_archivo.readline()
print(linea) """

mi_archivo = open('Prueba.txt')

lineas = mi_archivo.readlines()
if len(lineas)>= 2:
    print(lineas[1])

