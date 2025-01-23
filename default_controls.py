import keyboard
def arrow(data,x):
    if keyboard.is_pressed('4') and not keyboard.is_pressed('6'):
        return -1
    elif keyboard.is_pressed('6') and not keyboard.is_pressed('4'):
        return 1
    else:
        return 0

def asd(data,x):
    if keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
        return -1
    elif keyboard.is_pressed('d') and not keyboard.is_pressed('a'):
        return 1
    else:
        return 0