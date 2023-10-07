import csv

# Supongamos que tienes una lista de datos
lista_de_datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Juan", 25, "Madrid"],
    ["María", 30, "Barcelona"],
    ["Pedro", 28, "Valencia"],
]

# Nombre del archivo en el que deseas guardar los datos
nombre_archivo = "datos.csv"

# Abre el archivo en modo escritura
with open(nombre_archivo, mode='w', newline='',  encoding='utf-8') as archivo_csv:
    # Crea un objeto escritor CSV
    escritor_csv = csv.writer(archivo_csv, delimiter='\t')

    # Escribe los datos en el archivo
    for fila in lista_de_datos:
        escritor_csv.writerow(fila)

print(f"Se ha creado el archivo {nombre_archivo} con los datos tabulados.")
