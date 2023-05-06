import pyautogui
from time import sleep


def spam(msg, maxMsg):
    count = 0
    while count < maxMsg:
        count += 1
        print("Send Message: " + str(count))
        pyautogui.write(msg)
        pyautogui.press("enter")
        print(count)
        print(maxMsg)
        if count % 9 == 0:
            sleep(2)


output_choice = input("What would you like to spam?\n")
number_times_choice = int(input("How many times would you like to spam it?\n"))


time  =0
while time != 10:
    time+= 1
    sleep(1)
    print("Spammer Waiting..." + str(time))



spam(output_choice, number_times_choice)

