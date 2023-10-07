""" Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
Imprime el contenido completo de "registro.txt" al finalizar.
Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido. """

# Lista de valores a escribir en el archivo
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
registro_ultima_sesion2 = ["Jimy", "06/|0/2023","16:30:50 hs", "Datos entregados"]

# Abre el archivo en modo escritura ('a' para agregar al final)
with open("registro.txt", "a") as archivo:
    # Escribe los elementos de la lista separados por tabuladores y agrega una nueva línea
    linea = "\t".join(registro_ultima_sesion) + "\n"
    linea = "\t".join(registro_ultima_sesion2) + "\n"
    archivo.writelines(linea)

# Cierra el archivo de escritura

# Abre el archivo en modo lectura ('r') y muestra su contenido
with open("registro.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
