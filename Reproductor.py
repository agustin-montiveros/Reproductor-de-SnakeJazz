from pygame import mixer


print("Hora de python")
mixer.init()
mixer.music.load("SnakeJazz.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print("Pulsa P para deneter la cancion")
    print("Pulsa R para reanudar la cancion")
    print("Pulsa S para salir")
    
    opcion = input(">>> ")
    
    if opcion =="p":
        mixer.music.pause()
    elif opcion =="r":
        mixer.music.unpause()
    elif opcion == "s":
        mixer.music.stop()
        break
    
   