import keyboard
def control(data,x):
    if keyboard.is_pressed('4') and not keyboard.is_pressed('6'):
        return 1
    elif keyboard.is_pressed('6') and not keyboard.is_pressed('4'):
        return -1
    else:
        return 0