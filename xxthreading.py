#!/usr/bin/env python3
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

"""
To start a thread
x = threading.Thread(target=thread_function, args=(1,))
x.start()

Single Thread Format

$ ./single_thread.py
Main    : before creating thread
Main    : before running thread
Thread 1: starting
Main    : wait for the thread to finish
Main    : all done
Thread 1: finishing

Example of single thread

import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
"""

def threading_ex():
    import logging
    import threading
    import time

    def thread_function(name):
        logging.info("Thread %s: starting", name)
        time.sleep(2)
        logging.info("Thread %s: finishing", name)

     if __name__ == "__main__":
            format = "%(asctime)s: %(message)s"
            logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

         logging.info("Main    : before creating thread")
         x = threading.Thread(target=thread_function, args=(1,))
        logging.info("Main    : before running thread")
        x.start()
        logging.info("Main    : wait for the thread to finish")
        # x.join()
        logging.info("Main    : all done")