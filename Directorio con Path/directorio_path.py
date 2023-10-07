from pathlib import Path #Path en mayuscular porque es un objeto

""" carpeta = Path('C:/Users/jimym/Pictures/carpeta_path') 
archivo = carpeta / 'archivo_path.txt'
mi_archivo = open(archivo)
print(mi_archivo.read()) """

#otra forma mas acortada es: 

carpeta = Path('C:/Users/jimym/Pictures/carpeta_path') / 'archivo_path.txt'
mi_archivo = open(carpeta)
print(mi_archivo.read())

#para mac la direccion se usa:  Path('Users/jimym/Pictures/carpeta_path') 