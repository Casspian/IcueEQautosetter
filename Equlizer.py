try:
    import pickle
except :
    print('ERROR: Module "pickle" not found.')
    exit()

#Colors


#checks range
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
        #No settings found
        print( "No equlizer settings found, please add a Equlizer" )
        exit()
    print( "equlizer settings found.")
    #counts how many EQ are there
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
        print( Equlizers[count]  +" "+ Equlizers[count + 1] +", "+ Equlizers[count + 2] +", "+ Equlizers[count + 3] +", "+ Equlizers[count + 4] +", "+ Equlizers[count + 5] +", "+ Equlizers[count + 6] +", "+ Equlizers[count + 7] +", "+ Equlizers[count + 8] +", "+ Equlizers[count + 9] +", "+ Equlizers[count + 10])
        count = count + 11
    count = 0


    #ask if exit or delete
    while "answer invalid":
        reply = str(input("Do you want to (d)elete a Equlizer or (E)xit this programm ? \n" + ' (d/e): ')).lower().strip()
        if reply[:1] == 'd':
            # sacadaka
            while " ":
                bra = False
                count = 0
                eqname = input("Enter name of Equlizer: ")
                for i in range(listc):
                    if eqname == Equlizers[count]:
                        print( "Name found" )
                        bra = True
                        break
                    else:
                        count = count + 11
                if bra == True:
                    break
                else:
                    print( "Name not found" )




        if reply[:1] == 'e':
            exit()
        for i in range(11):
            print(count)
            del Equlizers[count]
        print( "Equlizer deleted." )
        pickle.dump(Equlizers, open("Equliz.dat", "wb"))
        exit()










#add new eq
def Addeq():
    eqsettings = False
    #looks if there are information
    try:
        Equlizers = pickle.load(open("Equliz.dat", "rb"))
        eqsettings = True
    except:
        eqsettings = False

    if eqsettings == False:
        #asks for information
        #32
        while "32":
            settings32 = input("input your Settings for 32: ")
            if rangetest(settings32) == True:
                break
            else:
                print( + "invalid input retry." )
        #64
        while "64":
            settings64 = input("input your Settings for 64: ")
            if rangetest(settings64) == True:
                break
            else:
                print( "invalid input retry." )
        #125
        while "125":
            settings125 = input("input your Settings for 125: ")
            if rangetest(settings125) == True:
                break
            else:
                print("invalid input retry.")
        #250
        while "250":
            settings250 = input("input your Settings for 250: ")
            if rangetest(settings250) == True:
                break
            else:
                print("invalid input retry.")
        #500
        while "500":
            settings500 = input("input your Settings for 500: ")
            if rangetest(settings500) == True:
                break
            else:
                print("invalid input retry.")
        #1k
        while "1k":
            settings1k = input("input your Settings for 1k: ")
            if rangetest(settings1k) == True:
                break
            else:
                print("invalid input retry.")
        #2k
        while "2k":
            settings2k = input("input your Settings for 2k: ")
            if rangetest(settings2k) == True:
                break
            else:
                print("invalid input retry.")
        #4k
        while "4k":
            settings4k = input("input your Settings for 4k: ")
            if rangetest(settings4k) == True:
                break
            else:
                print("invalid input retry.")
        #8k
        while "8k":
            settings8k = input("input your Settings for 8k: ")
            if rangetest(settings8k) == True:
                break
            else:
                print("invalid input retry.")
        #16k
        while "16k":
            settings16k = input("input your Settings for 16k: ")
            if rangetest(settings16k) == True:
                break
            else:
                print("invalid input retry.")

        Nameofeq = input("Name: ").replace(" ", "")
        list = [str(Nameofeq), settings32, settings64, settings125, settings250, settings500, settings1k, settings2k, settings4k, settings8k, settings16k]
        print(list)

        pickle.dump(list, open("Equliz.dat", "wb"))
        print("invalid input retry.")
        exit()


# asks for information
    if eqsettings == True:

        #32
        while True:
            settings32 = input("input your Settings for 32: ")
            if rangetest(settings32) == True:
                break
            else:
                print("invalid input retry.")
        #64
        while True:
            settings64 = input("input your Settings for 64: ")
            if rangetest(settings64) == True:
                break
            else:
                print("invalid input retry.")
        #125
        while True:
            settings125 = input("input your Settings for 125: ")
            if rangetest(settings125) == True:
                break
            else:
                print("invalid input retry.")
        #250
        while True:
            settings250 = input("input your Settings for 250: ")
            if rangetest(settings250) == True:
                break
            else:
                print("invalid input retry.")
        #500
        while True:
            settings500 = input("input your Settings for 500: ")
            if rangetest(settings500) == True:
                break
            else:
                print("invalid input retry.")
        #1k
        while True:
            settings1k = input("input your Settings for 1k: ")
            if rangetest(settings1k) == True:
                break
            else:
                print("invalid input retry.")
        #2k
        while True:
            settings2k = input("input your Settings for 2k: ")
            if rangetest(settings2k) == True:
                break
            else:
                print("invalid input retry.")
        #4k
        while True:
            settings4k = input("input your Settings for 4k: ")
            if rangetest(settings4k) == True:
                break
            else:
                print("invalid input retry.")
        #8k
        while True:
            settings8k = input("input your Settings for 8k: ")
            if rangetest(settings8k) == True:
                break
            else:
                print("invalid input retry.")
        #16k
        while True:
            settings16k = input("input your Settings for 16k: ")
            if rangetest(settings16k) == True:
                break
            else:
                print("invalid input retry.")




        Nameofeq = input("Name: ").replace(" ", "")





        list = Equlizers + [str(Nameofeq), settings32, settings64, settings125, settings250, settings500, settings1k, settings2k, settings4k, settings8k, settings16k]
        print(list)
        #
        pickle.dump(list, open("Equliz.dat", "wb"))
        print("invalid input retry.")

        exit()






#ask what to do
while "answer invalid":
    reply = str(input("Do you want to (c)hange equlizer settings or (a)dd equlizer settings ?\n" +' (c/a): ')).lower().strip()
    if reply[:1] == 'a':
        Addeq()



    if reply[:1] == 'c':
        Change()

