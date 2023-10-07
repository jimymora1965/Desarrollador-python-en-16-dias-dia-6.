"""with open("mi_archivo.txt", "w") as archivo:
    archivo.write("Nuevo texto")

# Vuelve a abrir el archivo en modo lectura para imprimir su contenido
with open("mi_archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)"""
    
""" mi_archivo = open('mi_archivo.txt',"w")
mi_archivo.write("Nuevo texto para practicar lectura archivos")

mi_archivo = open('mi_archivo.txt',"r")
contenido= mi_archivo.read()
print(contenido) """

# Abre el archivo en modo escritura para añadir una línea al final
with open("mi_archivo.txt", "a") as archivo:
    archivo.write("Nuevo inicio de sesión\n")

# Vuelve a abrir el archivo en modo lectura para imprimir su contenido
with open("mi_archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)