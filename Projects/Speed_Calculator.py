from time import *
import random as r


def mistake(partest,usertest):
    error = 0
    correct = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
            else:
                correct = correct + 1
                print(correct)
        except:
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(userinput) / time_r
    return round(speed)

if __name__ == '__main__':
    while True:
        ck = input("ready to test : yes / no :")
        if ck == 'yes':
            test =["Length and appearance do not","determine whether a section in","a paper is a paragraph.","welcome to speed calculator app"]
            test1 = r.choice(test)
            print("***** Typing speed *****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input("Enter:  ")
            time_2 = time()

            print('Speed : ', speed_time(time_1, time_2, testinput), "W/sec")
            print("Error : ", mistake(test1, testinput))
            print("Correct : ", mistake(test1, testinput))

        elif ck == 'no':
            print("Thank you ")
            break
        else:
            print("Wrong input")



