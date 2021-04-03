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
try:
    import re
except:
    print('ERROR: Module "re" not found.')
    exit()


#Colors



mouse = Controller()


#Calibration
def Cal():
    #get first pos
    print( "Recalibration Started.")
    input("place your mouse on the 32 knob and on 12 db ,then press enter.")
    print ("Current position: " + str(mouse.position))
    knop1 = mouse.position

    #get second pos
    input("place mouse on 64 knob on -12 db and then press enter.")
    print("Current position: " + str(mouse.position))
    knop2 = mouse.position

    # get pos of create new eq set
    input("place mouse on create new EQ and then press enter.")
    print("Current position: " + str(mouse.position))
    Neweq = mouse.position

    #saves pos
    knops = [str(knop1), str(knop2), str(Neweq)]
    pickle.dump(knops, open("CInfo.dat", "wb"))
    print( "Recalibrated" )

    #Human Test
    strknops = str(knops)
    knopscor = re.findall("(\d+)", strknops)

    #calculations
    x = int(knopscor[0]) - int(knopscor[2])



    y = int(knopscor[1]) - int(knopscor[3])
    y = y / 24
    y0 = int(knopscor[1]) - y * 12

    xN = int(knopscor[0])
    #test
    for i in range(10):
        mouse.position = (xN, y0)

        reply = str(input("Press Enter if your mouse is on the knop if not enter "  + ' (n): ')).lower().strip()
        if reply[:1] == 'n':
            # Redose Calibration
            print("Please recalibrate and put your mouse in the middle of the knop.")
            Cal()

        if reply[:1] == '':
            xN = xN - x













    #exits
    exit()



#test if data is already there
try:
     #reads if data is there
     testifinformationisthere = pickle.load(open("CInfo.dat", "rb"))
     testifinformationisthere[0]
except:
    #Calibration not found, makes calibration.
    Cal()



#if data found ask if recalibrate
while "answer invalid":
    reply = str(input( "Calibration found. Do you want to recalibrate ? \n"  +' (y/n): ')).lower().strip()
    if reply[:1] == 'y':
        # Redose Calibration
        Cal()

    if reply[:1] == 'n':
        print("Recalibration canceled.")
        exit()


