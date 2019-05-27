import os
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    pygame.init()
    pygame.mixer.init()

def main():
    '''Funcion principal del buscador de archivos mp3. Esta aplicación funciona vía PyGame.
       Es necesario insertar en el terminal las 2 lineas de abajo '''
    #source dataenv/bin/activate
    #pip3 install pygame
    interactuar(buscar())


class Mp3:
    '''Representación de un archivo.mp3'''

    def __init__(self, nombre, ruta):
        '''Constructor de la  clase mp3 '''
        self.nombre = nombre
        self.ruta = ruta

    def __str__(self):
        '''Nos brinda la representacion del mp3 como cadena de texto (para imprimir)'''
        return "{}".format(self.nombre)

    def ver_tamaño(self, ruta_y_mp3):
        '''Nos da el tamaño del mp3'''
        tamaño = str(os.path.getsize(ruta_y_mp3))
        if len(tamaño) >= 7:
            tamaño = "4389435"
            tamaño=[tamaño[:-6],str(int(tamaño[-6:-5]) + 1)]
            tamaño=".".join(tamaño)    
            return tamaño + " MB"
        return tamaño + " Bytes"

    def ver_nombre(self):
        '''Nos da el nombre del mp3'''
        return self.nombre    

    def ver_ruta(self):
        '''Nos da la ruta del mp3'''
        return self.ruta

    def __lt__(self, otro):
        '''Permite comparar objetos mediante < y >.'''
        return self.nombre < otro.nombre

def buscar():
    '''Busca todos los archivos .mp3 de la PC, por cada uno devuelve su nombre y un numero asociado'''
    import os
    import bisect
    initial_dir = '/Users'
    mp3_totales = []
    cantidad_de_mp3 = 0
    ruta = ''
    for origen, _, archivos in os.walk(initial_dir):
        for archivo in archivos:
            if '.mp3' not in archivo or '.asd' in archivo or '.pek' in archivo or '.cfa' in archivo:
                continue
            ruta = os.path.join(origen)
            archivo = Mp3(archivo, ruta)
            bisect.insort(mp3_totales, archivo)
            cantidad_de_mp3 += 1   
    nro_del_mp3 = 1
    for mp3 in mp3_totales:
        print (nro_del_mp3, mp3)
        nro_del_mp3 += 1
    print ("La cantidad de archivos .mp3 en el ordenador es de ", cantidad_de_mp3)
    return mp3_totales

def reproducir(ruta_y_mp3):
    '''Reproduce via PyGame el mp3 elegido''' 
    import time
    import contextlib
    with contextlib.redirect_stdout(None):
        pygame.mixer.music.load(ruta_y_mp3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
   
def interactuar(mp3_totales):
    '''Si el usuario selecciona uno devuelve su ubicacion, duracion y pregunta si quiere que lo reproduzca'''
    continuar = "s"
    while continuar == "s":
        mp3_elegido=int(input("Ingrese el nro del mp3 para obtener sus datos: "))
        if len(mp3_totales) > (mp3_elegido-1):
            mp3 = mp3_totales[mp3_elegido-1]
            ruta_y_mp3 = [mp3.ver_ruta(), mp3.ver_nombre()]
            ruta_y_mp3 = "/".join(ruta_y_mp3)      
            print ("Nombre: ", mp3," - Tamaño: ", mp3.ver_tamaño(ruta_y_mp3), "- Ubicación: ", mp3.ver_ruta())
        sonar=input("¿Querés reproducirlo? (s/n)")
        if sonar == "s":
            reproducir(ruta_y_mp3)    
        print (ruta_y_mp3)
        continuar=input("¿Querés continuar?(s/n)") 

main()