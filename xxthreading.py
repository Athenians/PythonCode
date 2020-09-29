#from time import sleep
#from threading import Thread
#bt = Button()

#def play_sound():
#    for j in range(0,10):             # Does 10 times
#        Sound.tone(1000, 2000).wait()  #1000Hz for 2s
#        sleep(0.5)

#t = Thread(target=play_sound)
#t.start()
#for i in range(0,5):       # Do five times.
#    while bt.value() ==0:  # while button is not pressed
#        sleep(0.01)        # do nothing other than wait
#    while bt.value() ==1:  # while button is pressed
#        sleep(0.01)        # do nothing other than wait
#Sound.beep()