import os
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    pygame.init()
    pygame.mixer.init()

def main():
    '''Main function of the mp3 player'''
    interact(find())


class Mp3:
    '''Representation of one mp3 file'''

    def __init__(self, name, path):
        '''Constructor of the mp3 class '''
        self.name = name
        self.path = path

    def __str__(self):
        '''Readable string representation of the mp3 object'''
        return "{}".format(self.name)

    def see_size(self, path_and_mp3):
        '''Size of the mp3'''
        size = str(os.path.getsize(path_and_mp3))
        if len(size) >= 7:
            size = "4389435"
            size=[size[:-6],str(int(size[-6:-5]) + 1)]
            size=".".join(size)    
            return size + " MB"
        return tamaño + " Bytes"

    def see_name(self):
        '''Shows the name of the mp3'''
        return self.name    

    def see_path(self):
        '''Shows the path of the mp3'''
        return self.path

    def __lt__(self, other):
        '''Allows to compare objects throught < and >.'''
        return self.name < other.name

def find():
    '''Finds all the mp3 files on the computer. For each returns the name and one number'''
    import os
    import bisect
    initial_dir = '/Users'
    total_mp3s = []
    mp3s_amount = 0
    path = ''
    for origin, _, files in os.walk(initial_dir):
        for files in files:
            if '.mp3' not in files or '.asd' in files or '.pek' in files or '.cfa' in files:
                continue
            path = os.path.join(origin)
            files = Mp3(files, path)
            bisect.insort(total_mp3s, files)
            mp3s_amount += 1   
    mp3_number = 1
    for mp3 in total_mp3s:
        print (mp3_number, mp3)
        mp3_number += 1
    print ("The amount of mp3 files in the computer is ", mp3s_amount)
    return total_mp3s

def play(path_and_mp3):
    '''Plays via PyGame the chosen mp3''' 
    import time
    import contextlib
    with contextlib.redirect_stdout(None):
        pygame.mixer.music.load(path_and_mp3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
   
def interact(total_mp3s):
    '''If the user choose one it return his path, duration and ask if he want to hear it'''
    continue_ = "s"
    while continue_ == "s":
        chosen_mp3=int(input("Enter the mp3's number to obtain his data: "))
        if len(total_mp3s) > (chosen_mp3-1):
            mp3 = total_mp3s[chosen_mp3-1]
            path_and_mp3 = [mp3.see_path(), mp3.see_name()]
            path_and_mp3 = "/".join(path_and_mp3)      
            print ("Name: ", mp3," - Size: ", mp3.see_size(path_and_mp3), "- Path: ", mp3.see_path())
        sound=input("¿Do you want to play it? (s/n)")
        if sound == "s":
            play(path_and_mp3)    
        print (path_and_mp3)
        continue_=input("¿Do you want to continue?(s/n)") 

main()
