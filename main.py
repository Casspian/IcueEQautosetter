try:
    from pynput.keyboard import Key, Controller as KeyboardController
    from pynput.mouse import Button, Controller
except:
    print('ERROR: Module "pynput" not found.')
    exit()
try:
    import pickle
except:
    print('ERROR: Module "pickle" not found.')
    exit()
try:
    import re
except:
    print('ERROR: Module "re" not found.')
    exit()
try:
    import time
except:
    print('ERROR: Module "time" not found.')
    exit()






keyboard = KeyboardController()

mouse = Controller()


#optinal
addnametf = False
try:
    addname = pickle.load(open("Optiona.dat", "rb"))
    addname[0]
    print("Optional Rename Found.")
    addnametf = True
except:
    pass




#loads cords
try:
    knops = pickle.load(open("CInfo.dat", "rb"))
    knops[0]
    print("Calibration Found." )
except :
    print('ERROR: No calibration found.\n' + ' To calibrate open "calibration.py".')
    exit()
#loads EQ settings
try:
    Equlizers = pickle.load(open("Equliz.dat", "rb"))
    Equlizers[0]
    print("EQulizers Found.")
except :
    print('ERROR: No Equlizers found.\n'+ 'To add a EQulizer open "Equlizer.py".' )
    exit()


#calculates distanz
strknops = str(knops)
knopscor = re.findall("(\d+)", strknops)

x = int(knopscor[0]) - int(knopscor[2])
y = int(knopscor[1]) - int(knopscor[3])

y = y / 24

#calculates distanz for x
x32 = int(knopscor[0])
x64 = x32 -x
x125 = x64 -x
x250 = x125 -x
x500 = x250 -x
x1k = x500 -x
x2k = x1k -x
x4k = x2k -x
x8k = x4k -x
x16k = x8k -x

#calculation for y

y12 = int(knopscor[1])
y11 = int(knopscor[1]) - y
y10 = int(knopscor[1]) - y * 2
y9 = int(knopscor[1]) - y * 3
y8 = int(knopscor[1]) - y * 4
y7 = int(knopscor[1]) - y * 5
y6 = int(knopscor[1]) - y * 6
y5 = int(knopscor[1]) - y * 7
y4 = int(knopscor[1]) - y * 8
y3 = int(knopscor[1]) - y * 9
y2 = int(knopscor[1]) - y * 10
y1 = int(knopscor[1]) - y * 11
y0 = int(knopscor[1]) - y * 12
ym1 = int(knopscor[1]) - y * 13
ym2 = int(knopscor[1]) - y * 14
ym3 = int(knopscor[1]) - y * 15
ym4 = int(knopscor[1]) - y * 16
ym5 = int(knopscor[1]) - y * 17
ym6 = int(knopscor[1]) - y * 18
ym7 = int(knopscor[1]) - y * 19
ym8 = int(knopscor[1]) - y * 20
ym9 = int(knopscor[1]) - y * 21
ym10 = int(knopscor[1]) - y * 22
ym11 = int(knopscor[1]) - y * 23
ym12 = int(knopscor[1]) - y * 24


# counts how many EQ are there
listc = 0
listcount = int(len(Equlizers))

while True:
    if listcount == 0:
        break
    else:
        listcount = listcount - 11
        listc = listc + 1

#prints all EQs
count = 0
for i in range(listc):
    print( Equlizers[count] + " "+ Equlizers[count + 1] +", "+ Equlizers[count + 2] +", "+ Equlizers[count + 3] +", "+ Equlizers[count + 4] +", "+ Equlizers[count + 5] +", "+ Equlizers[count + 6] +", "+ Equlizers[count + 7] +", "+ Equlizers[count + 8] +", "+ Equlizers[count + 9] +", "+ Equlizers[count + 10])
    count = count + 11
count = 0

input(  '!!!DONT MOVE YOUR MOUSE!!!\n'  + 'Click Enter if ready.' )


Equlizers = pickle.load(open("Equliz.dat", "rb"))
firstrun = True

for i in range(listc):


    if firstrun == False:
        if addnametf == True:
            mouse.position = addname
            for i in range(5):
                mouse.press(Button.left)
                mouse.release(Button.left)
                keyboard.press(Key.delete)
                keyboard.release(Key.delete)
                keyboard.type(str(Equlizers[count-11]))

    firstrun = False

    mouse.position = (knopscor[4], knopscor[5])
    mouse.click(Button.left, 1)
    count = count + 1
    countxn = 0



    mouse.position = (x32, y0)

    xn = x32


    for i in range(10):
        countxn = countxn + 1
        if countxn == 1:
            xn = x32
        if countxn == 2:
            xn = x64
        if countxn == 3:
            xn = x125
        if countxn == 4:
            xn = x250
        if countxn == 5:
            xn = x500
        if countxn == 6:
            xn = x1k
        if countxn == 7:
            xn = x2k
        if countxn == 8:
            xn = x4k
        if countxn == 9:
            xn = x8k
        if countxn == 10:
            xn = x16k



        mouse.position = (xn, y0)
        time.sleep(0.1)
        mouse.press(Button.left)
        time.sleep(0.001)
        print(Equlizers[count])






        if int(Equlizers[count]) == -1:
            mouse.position = (xn, ym1)
        if int(Equlizers[count]) == -2:
            mouse.position = (xn, ym2)
        if int(Equlizers[count]) == -3:
            mouse.position = (xn, ym3)
        if int(Equlizers[count]) == -4:
            mouse.position = (xn, ym4)
        if int(Equlizers[count]) == -5:
            mouse.position = (xn, ym5)
        if int(Equlizers[count]) == -6:
            mouse.position = (xn, ym6)
        if int(Equlizers[count]) == -7:
            mouse.position = (xn, ym7)
        if int(Equlizers[count]) == -8:
            mouse.position = (xn, ym8)
        if int(Equlizers[count]) == -9:
            mouse.position = (xn, ym9)
        if int(Equlizers[count]) == -10:
            mouse.position = (xn, ym10)
        if int(Equlizers[count]) == -11:
            mouse.position = (xn, ym11)
        if int(Equlizers[count]) == -12:
            mouse.position = (xn, ym12)
        if int(Equlizers[count]) == 0:
            mouse.position = (xn, y0)
        if int(Equlizers[count]) == 1:
            mouse.position = (xn, y1)
        if int(Equlizers[count]) == 2:
            mouse.position = (xn, y2)
        if int(Equlizers[count]) == 3:
            mouse.position = (xn, y3)
        if int(Equlizers[count]) == 4:
            mouse.position = (xn, y4)
        if int(Equlizers[count]) == 5:
            mouse.position = (xn, y5)
        if int(Equlizers[count]) == 6:
            mouse.position = (xn, y6)
        if int(Equlizers[count]) == 7:
            mouse.position = (xn, y7)
        if int(Equlizers[count]) == 8:
            mouse.position = (xn, y8)
        if int(Equlizers[count]) == 9:
            mouse.position = (xn, y9)
        if int(Equlizers[count]) == 10:
            mouse.position = (xn, y10)
        if int(Equlizers[count]) == 11:
            mouse.position = (xn, y11)
        if int(Equlizers[count]) == 12:
            mouse.position = (xn, y12)


        print( "Setting " + str(count) + " is Configured" )
        count = count + 1


        mouse.release(Button.left)
        time.sleep(0.001)

if addnametf == True:
        mouse.position = addname
        for i in range(5):
            mouse.press(Button.left)
            mouse.release(Button.left)
            keyboard.press(Key.delete)
            keyboard.release(Key.delete)
            keyboard.type(str(Equlizers[count-11]))









#TEST








print(x, y)



