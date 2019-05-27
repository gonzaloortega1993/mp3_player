import os
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    pygame.init()
    pygame.mixer.init()

def main():
    '''Main function of the mp3 player'''
    interactuar(buscar())


class Mp3:
    '''Representation of one mp3 file'''

    def __init__(self, nombre, ruta):
        '''Constructor of the mp3 class '''
        self.nombre = nombre
        self.ruta = ruta

    def __str__(self):
        '''Readable string representation of the mp3 object'''
        return "{}".format(self.nombre)

    def ver_tamaño(self, ruta_y_mp3):
        '''Size of the mp3'''
        tamaño = str(os.path.getsize(ruta_y_mp3))
        if len(tamaño) >= 7:
            tamaño = "4389435"
            tamaño=[tamaño[:-6],str(int(tamaño[-6:-5]) + 1)]
            tamaño=".".join(tamaño)    
            return tamaño + " MB"
        return tamaño + " Bytes"

    def ver_nombre(self):
        '''Shows the name of the mp3'''
        return self.nombre    

    def ver_ruta(self):
        '''Shows the path of the mp3'''
        return self.ruta

    def __lt__(self, otro):
        '''Allows to compare objects throught < and >.'''
        return self.nombre < otro.nombre

def buscar():
    '''Finds all the mp3 files on the computer. For each returns the name and one number'''
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
    print ("The amount of mp3 files in the computer is ", cantidad_de_mp3)
    return mp3_totales

def reproducir(ruta_y_mp3):
    '''Plays via PyGame the chosen mp3''' 
    import time
    import contextlib
    with contextlib.redirect_stdout(None):
        pygame.mixer.music.load(ruta_y_mp3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
   
def interactuar(mp3_totales):
    '''If the user choose one it return his path, duration and ask if he want to hear it'''
    continuar = "s"
    while continuar == "s":
        mp3_elegido=int(input("Enter the mp3's number to obtain his data: "))
        if len(mp3_totales) > (mp3_elegido-1):
            mp3 = mp3_totales[mp3_elegido-1]
            ruta_y_mp3 = [mp3.ver_ruta(), mp3.ver_nombre()]
            ruta_y_mp3 = "/".join(ruta_y_mp3)      
            print ("Nombre: ", mp3," - Tamaño: ", mp3.ver_tamaño(ruta_y_mp3), "- Ubicación: ", mp3.ver_ruta())
        sonar=input("¿Do you want to play it? (s/n)")
        if sonar == "s":
            reproducir(ruta_y_mp3)    
        print (ruta_y_mp3)
        continuar=input("¿Do you want to continue?(s/n)") 

main()
