from pynput import keyboard
from pynput import mouse
from time import sleep
from _thread import start_new_thread
from pickle import dump as __save_actionList
from pickle import load as __load_actionList
from datetime import datetime
        
class __Core:
    """
        docstring
        """

    def __init__(self):
        
        self.__mouse_controller = mouse.Controller
        self.__keyboard_controller = keyboard.Controller
        
    def _mouse_move(self, position: tuple):
        
        self.__mouse_controller().position = position
    
    def _mouse_click_press(self, mouseButton):
        
        self.__mouse_controller().press(mouseButton)
        
    def _mouse_click_release(self, mouseButton):
        
        self.__mouse_controller().release(mouseButton)

    def _mouse_scroll(self, scroll: tuple):
        
        self.__mouse_controller().scroll(scroll[0], scroll[1])

    def _keyboard_press(self, key):
        
        self.__keyboard_controller().press(key)

    def _keyboard_release(self, key):
        
        self.__keyboard_controller().release(key)

class __SaveClass(__Core):
    
    def __init__(self, actionList=[]):
        
        self.__actionList = actionList
  
    @property
    def actionList(self):
        
        return self.__actionList



def record(actionList: list = [], inicialTimer = 0.0, stopCommand: keyboard.Key = keyboard.Key.esc):

    def __on_move(x, y):
        
        actionList.append({'name': 'on_move',
                           'action':action._mouse_move,
                           'parameters': (x, y),
                           'time': datetime.now() - inicialTimer})

    def __on_click(x, y, button, pressed):
        
        if pressed:
                actionList.append({'name':'on_click_pressed',
                                   'action': action._mouse_click_press,
                                   'parameters': button,
                                   'time': datetime.now() - inicialTimer})
        else:
            actionList.append({'name':'on_click_release',
                               'action': action._mouse_click_release,
                               'parameters': button,
                               'time': datetime.now() - inicialTimer})
    
    def __on_scroll(x, y, dx, dy):
        
        actionList.append({'name':'on_scroll',
                           'action': action._mouse_scroll,
                           'parameters': (dx, dy),
                           'time': datetime.now() - inicialTimer})

    def __on_press(key):

        if key == stopCommand:
                __listener.stop()
        else:
            actionList.append({'name':'on_press',
                               'action': action._keyboard_press, 
                               'parameters': key,
                               'time': datetime.now() - inicialTimer})

    def __on_release(key):
        
        actionList.append({'name':'on_press',
                           'action': action._keyboard_release, 
                           'parameters': key,
                           'time': datetime.now() - inicialTimer})

    action = __Core()
    inicialTimer = datetime.now()
    with mouse.Listener(on_move=__on_move, on_click=__on_click, on_scroll=__on_scroll) as __listener:
            with keyboard.Listener(on_press=__on_press, on_release=__on_release) as __listener:
                try:
                    __listener.join()
                except KeyboardInterrupt:
                    pass # ctrl + c pass error

    return actionList



def play(actionList = [], loop: bool = False, stopCommand: keyboard.Key = keyboard.Key.esc, velocity = 1):


    interrupt = False
    _loop = loop

    def thread_stop_listem(*args):

        def on_press(key):
            if key == stopCommand:
                global _loop
                global interrupt
                listener.stop()
                _loop = False
                interrupt = True
        with keyboard.Listener(on_press=on_press, on_release=None) as listener:
                try:
                    listener.join()
                except KeyboardInterrupt:
                    pass # ctrl + c error pass

    start_new_thread(thread_stop_listem, (0,))
    
    while True:
        inicialTimer = datetime.now()
        for action in actionList:
            while True:
                if datetime.now() - inicialTimer < action['time']:
                    continue
                break
            action['action'](action['parameters'])

            if interrupt:
                break

        if not _loop:
            break
        break



def save_file(actionList, diretory):
    
    with open(diretory + ".pkl", 'wb') as _file:
        fileClass = __SaveClass(actionList)
        __save_actionList(fileClass, _file)

def load_file(fileName):
    
    with open(fileName + ".pkl", 'rb') as _file:
        return __load_actionList(_file).actionList


