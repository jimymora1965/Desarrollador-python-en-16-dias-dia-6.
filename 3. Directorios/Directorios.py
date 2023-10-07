import os
#con este codigo ubico la ruta del archivo con que estoy trabajando actualmente en la misma carpeta
""" 
ruta = os.getcwd()
print(ruta) """

#con este codigo ubico un archivo en una ruta diferente

ruta = os.chdir('C:\\Users\\jimym\\Pictures')

archivo = open('archivo.txt')
print(archivo.read())