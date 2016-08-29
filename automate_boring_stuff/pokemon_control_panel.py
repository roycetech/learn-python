import tkinter
import pyautogui

# import throw_pokeball
# import area_sweeper
# import pokemon_marcher


gui = tkinter.Tk()
gui.title("Pokébot - Idle")
gui.geometry("250x260")


# Mouse Position
def savePosition():
    global position
    position = pyautogui.position()

# Mouse Position
def loadPosition():
    pyautogui.moveTo(position[0], position[1])


def feed():
    savePosition()
    loadPosition()


def sweep():
    pass


def throw1():
    _throw(1)

def throw2():
    _throw(2)

def throw3():
    _throw(3)

def _throw(throw_type):
    print("Doing type %d throw!" % throw_type);


def marchNorth():
    _march(0)

def marchEast():
    _march(1)

def marchWest():
    _march(2)

def marchSouth():
    _march(3)

def _march(index):
    btnSweep.config(state='disabled')
    for i in range(len(buttonList)):
        button = buttonList[i]
        if i == index:
            buttonText = button.config('text')[4]
            print(buttonText)
            if 'Stop Marching' == buttonText:
                enableMarchButtons()
                button.config(text='March ' + directionList[index])
                gui.title("Pokébot - Idle")
                break
            else:
                gui.title("Pokébot - Marching " + directionList[index])
                button.config(text='Stop Marching')
        else:
            button.config(state='disabled')


def enableMarchButtons():
    btnSweep.config(state='normal')
    marchEast.config(state=tkinter.NORMAL)
    for i in range(len(buttonList)):
        button = buttonList[i]
        buttonText = button.config('text')[4]
        print('Enable ' + buttonText)
        button.configure(state=tkinter.NORMAL)


btnSweep = tkinter.Button(text='Sweep Area', command=sweep)
btnSweep.pack()


marchNorth = tkinter.Button(text='March North', state='normal', command=marchNorth)
marchNorth.pack()

marchEast = tkinter.Button(text='March East', command=marchEast)
marchEast.pack()

marchWest = tkinter.Button(text='March West', command=marchWest)
marchWest.pack()

marchSouth = tkinter.Button(text='March South', command=marchSouth)
marchSouth.pack()


btnBerry = tkinter.Button(text='Razz Berry ', command=feed)
btnBerry.pack()


btnNear = tkinter.Button(text='Throw Pokéball Near', command=throw1)
btnNear.pack()

tkinter.Button(text='Throw Pokéball Medium', command=throw2).pack()
tkinter.Button(text='Throw Pokéball Far', command=throw3).pack()


directionList = ['North', 'East', 'West', 'South']
buttonList = [marchNorth, marchEast, marchWest, marchSouth]


gui.mainloop()
