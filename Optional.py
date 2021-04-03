try:
    import pickle
except:
    print('ERROR: Module "pickle" not found.')
    exit()

try:
    from pynput.mouse import Button, Controller
except:
    print('ERROR: Module "pynput" not found.')
    exit()

mouse = Controller()

def Namepoint():
    input("place your mouse on the first EQ.")
    print ("Current position: " + str(mouse.position))
    Nameadd = mouse.position
    pickle.dump(Nameadd, open("Optiona.dat", "wb"))
Namepoint()