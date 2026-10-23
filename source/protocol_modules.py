from source.tools import *
import keyboard


def enter_ready():
    keyboard.press_and_release('alt+escape')
    for i in range(1, 8): #enter Enu
        rand_wait(0.08, 0.120)
        rand_wait(0.01, 0.120)
        #rand_wait(0.08, 0.120)
        mouse_move(803, 126)
        sleep(0.02)
        left_click()
        sleep(0.02)
        mouse_move(777, 395)#épée
        righ_click()
        print(f"Enu {i} in fight")
        rand_wait(0.08, 0.120)
        keyboard.press_and_release('alt+escape')

    #rand_wait(0.08, 0.120)
    #rand_mouse_move(1045, 533, 1116, 543)# pos prêt

    for i in range (1, 9):
        #rand_wait(0.1, 0.120)
        rand_wait(0.08, 0.120)
        rand_wait(0.08, 0.120)
        #left_click()
        keyboard.press_and_release('=') #press button for ready
        print(f"Pj {i} is ready to fight")
        rand_wait(0.1, 0.120)
        keyboard.press_and_release('alt+escape')
