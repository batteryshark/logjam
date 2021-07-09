# Implements a AF_UNIX Socket-Based Logger - Sort of a cross-platform replacement for DBGView without a debugger.
from threading import Thread
from queue import Queue

import sys
# For testing in staging environment.
#sys.path.append('../afunix')
from pyafunix import AFUnixServer

PACKET_LEN = 0x1000
LOGGER_PATH = "/tmp/LOGGER"

def display_worker(display_queue):
    while True:
        line = display_queue.get()
        if line is None:  # simple termination logic, other sentinels can be used
            break
        print(line, flush=True)  # remove flush if slow or using Python2

def display_adder(args):
    display_queue = args[1]
    display_queue.put(args[0])


if __name__ == "__main__":
    display_queue = Queue()
    display_queue_thread = Thread(target=display_worker,args=(display_queue,),)
    display_queue_thread.setDaemon(True)
    display_queue_thread.start()

    afserver = AFUnixServer(LOGGER_PATH,"recv",display_adder,[display_queue],PACKET_LEN)
    afserver.startup()
    wat = input("Logger Started - Press Any Key to Quit\n")
    afserver.shutdown()