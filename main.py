try:
    import tkinter as tk
    import os
    from pynput.keyboard import Key, Controller as KeyboardController
    from pynput.mouse import Button, Controller
    import pickle
    import re
    import time

    mouse = Controller()
    keyboard = KeyboardController()
except Exception as e:
    print(e)
    exit()


# Calibration
def Cal():
    # get first pos
    print("Recalibration Started.")
    input("place your mouse on the 32 knob and on 12 db ,then press enter.")
    print("Current position: " + str(mouse.position))
    knop1 = mouse.position

    # get second pos
    input("place mouse on 64 knob on -12 db and then press enter.")
    print("Current position: " + str(mouse.position))
    knop2 = mouse.position

    # get pos of create new eq set
    input("place mouse on create new EQ and then press enter.")
    print("Current position: " + str(mouse.position))
    Neweq = mouse.position

    # saves pos
    knops = [str(knop1), str(knop2), str(Neweq)]
    pickle.dump(knops, open("CInfo.dat", "wb"))
    print("Recalibrated")

    # Name Todo: dump Name to CInfo.dat, not to Optiona.dat
    input("place your mouse on the first EQ Setting.")
    print("Current position: " + str(mouse.position))
    Nameadd = mouse.position
    pickle.dump(Nameadd, open("Optiona.dat", "wb"))

    # Human Test
    strknops = str(knops)
    knopscor = re.findall("(\d+)", strknops)

    # calculations
    x = int(knopscor[0]) - int(knopscor[2])

    y = int(knopscor[1]) - int(knopscor[3])
    y = y / 24
    y0 = int(knopscor[1]) - y * 12

    xN = int(knopscor[0])
    # test
    for i in range(10):
        mouse.position = (xN, y0)

        reply = str(input("Press Enter if your mouse is on the knop if not enter " + ' (n): ')).lower().strip()
        if reply[:1] == 'n':
            # Redose Calibration
            print("Please recalibrate and put your mouse in the middle of the knop.")
            Cal()

        if reply[:1] == '':
            xN = xN - x


# EQ settings

# checks range
def rangetest(Number):
    print(Number)
    try:
        if int(Number) in range(-13, 13):
            return True
        else:
            return False
    except:
        pass


def Change():
    try:
        Equlizers = pickle.load(open("Equliz.dat", "rb"))
        Equlizers[0]
    except:
        # No settings found
        print("No equlizer settings found, please add a Equlizer")
        exit()
    print("equlizer settings found.")
    # counts how many EQ are there
    listc = 0
    listcount = int(len(Equlizers))

    while True:
        if listcount == 0:
            break
        else:
            listcount = listcount - 11
            listc = listc + 1

    # prints all EQs
    count = 0
    for i in range(listc):
        print(Equlizers[count] + " " + Equlizers[count + 1] + ", " + Equlizers[count + 2] + ", " + Equlizers[
            count + 3] + ", " + Equlizers[count + 4] + ", " + Equlizers[count + 5] + ", " + Equlizers[
                  count + 6] + ", " + Equlizers[count + 7] + ", " + Equlizers[count + 8] + ", " + Equlizers[
                  count + 9] + ", " + Equlizers[count + 10])
        count = count + 11
    count = 0

    # ask if exit or delete
    while "answer invalid":
        reply = str(
            input("Do you want to (d)elete a Equlizer or (E)xit this programm ? \n" + ' (d/e): ')).lower().strip()
        if reply[:1] == 'd':
            # sacadaka
            while " ":
                bra = False
                count = 0
                eqname = input("Enter name of Equlizer: ")
                for i in range(listc):
                    if eqname == Equlizers[count]:
                        print("Name found")
                        bra = True
                        break
                    else:
                        count = count + 11
                if bra == True:
                    break
                else:
                    print("Name not found")

        if reply[:1] == 'e':
            exit()
        for i in range(11):
            print(count)
            del Equlizers[count]
        print("Equlizer deleted.")
        pickle.dump(Equlizers, open("Equliz.dat", "wb"))
        exit()


# add new eq
def Addeq():
    eqsettings = False
    # looks if there are information
    try:
        Equlizers = pickle.load(open("Equliz.dat", "rb"))
        eqsettings = True
    except:
        eqsettings = False

    if eqsettings == False:
        # asks for information
        # 32
        while "32":
            settings32 = input("input your Settings for 32: ")
            if rangetest(settings32) == True:
                break
            else:
                print(+ "invalid input retry.")
        # 64
        while "64":
            settings64 = input("input your Settings for 64: ")
            if rangetest(settings64) == True:
                break
            else:
                print("invalid input retry.")
        # 125
        while "125":
            settings125 = input("input your Settings for 125: ")
            if rangetest(settings125) == True:
                break
            else:
                print("invalid input retry.")
        # 250
        while "250":
            settings250 = input("input your Settings for 250: ")
            if rangetest(settings250) == True:
                break
            else:
                print("invalid input retry.")
        # 500
        while "500":
            settings500 = input("input your Settings for 500: ")
            if rangetest(settings500) == True:
                break
            else:
                print("invalid input retry.")
        # 1k
        while "1k":
            settings1k = input("input your Settings for 1k: ")
            if rangetest(settings1k) == True:
                break
            else:
                print("invalid input retry.")
        # 2k
        while "2k":
            settings2k = input("input your Settings for 2k: ")
            if rangetest(settings2k) == True:
                break
            else:
                print("invalid input retry.")
        # 4k
        while "4k":
            settings4k = input("input your Settings for 4k: ")
            if rangetest(settings4k) == True:
                break
            else:
                print("invalid input retry.")
        # 8k
        while "8k":
            settings8k = input("input your Settings for 8k: ")
            if rangetest(settings8k) == True:
                break
            else:
                print("invalid input retry.")
        # 16k
        while "16k":
            settings16k = input("input your Settings for 16k: ")
            if rangetest(settings16k) == True:
                break
            else:
                print("invalid input retry.")

        Nameofeq = input("Name: ").replace(" ", "")
        list = [str(Nameofeq), settings32, settings64, settings125, settings250, settings500, settings1k, settings2k,
                settings4k, settings8k, settings16k]
        print(list)

        pickle.dump(list, open("Equliz.dat", "wb"))
        print("invalid input retry.")
        exit()


# main

def ExportEQ():
    addnametf = False
    try:
        addname = pickle.load(open("Optiona.dat", "rb"))
        addname[0]
        print("Optional Rename Found.")
        addnametf = True
    except:
        pass

    # loads cords
    try:
        knops = pickle.load(open("CInfo.dat", "rb"))
        knops[0]
        print("Calibration Found.")
    except:
        print('ERROR: No calibration found.\n' + ' To calibrate open "calibration.py".')
        exit()
    # loads EQ settings
    try:
        Equlizers = pickle.load(open("Equliz.dat", "rb"))
        Equlizers[0]
        print("EQulizers Found.")
    except:
        print('ERROR: No Equlizers found.\n' + 'To add a EQulizer open "Equlizer.py".')
        exit()

    # calculates distanz
    strknops = str(knops)
    knopscor = re.findall("(\d+)", strknops)

    x = int(knopscor[0]) - int(knopscor[2])
    y = int(knopscor[1]) - int(knopscor[3])

    y = y / 24

    # calculates distanz for x
    x32 = int(knopscor[0])
    x64 = x32 - x
    x125 = x64 - x
    x250 = x125 - x
    x500 = x250 - x
    x1k = x500 - x
    x2k = x1k - x
    x4k = x2k - x
    x8k = x4k - x
    x16k = x8k - x

    # calculation for y

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

    # prints all EQs
    count = 0
    for i in range(listc):
        print(Equlizers[count] + " " + Equlizers[count + 1] + ", " + Equlizers[count + 2] + ", " + Equlizers[
            count + 3] + ", " + Equlizers[count + 4] + ", " + Equlizers[count + 5] + ", " + Equlizers[
                  count + 6] + ", " + Equlizers[count + 7] + ", " + Equlizers[count + 8] + ", " + Equlizers[
                  count + 9] + ", " + Equlizers[count + 10])
        count = count + 11
    count = 0

    input('!!!DONT MOVE YOUR MOUSE!!!\n' + 'Click Enter if ready.')

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
                    keyboard.type(str(Equlizers[count - 11]))

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

            print("Setting " + str(count) + " is Configured")
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
            keyboard.type(str(Equlizers[count - 11]))


# ask what they want to do
if __name__ == "__main__":
    while "answer invalid":
        reply = str(input(
            "What do you want to do ? \n [Recalibrate]      [1] \n [Edit EQ Settings] [2] \n [Start Exporting]  [3] \n [Exit]             [4]")).lower().strip()
        if reply[:1] == '1':
            # test if data is already there
            try:
                # reads if data is there
                testifinformationisthere = pickle.load(open("CInfo.dat", "rb"))
                testifinformationisthere[0]
            except:
                # Calibration not found, makes calibration.
                Cal()

            # if data found ask if recalibrate
            while "answer invalid":
                reply = str(input("Calibration found. Do you want to recalibrate ? \n" + ' (y/n): ')).lower().strip()
                if reply[:1] == 'y':
                    # Redose Calibration
                    Cal()

                if reply[:1] == 'n':
                    print("Recalibration canceled.")
                    exit()

        if reply[:1] == '2':
            # ask what to do
            while "answer invalid":
                reply = str(input(
                    "Do you want to (c)hange equlizer settings or (a)dd equlizer settings ?\n" + ' (c/a): ')).lower().strip()
                if reply[:1] == 'a':
                    Addeq()

                if reply[:1] == 'c':
                    Change()

        if reply[:1] == '3':
            ExportEQ()

        if reply[:1] == '4':
            exit()
