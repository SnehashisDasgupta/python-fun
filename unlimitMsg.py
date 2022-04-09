import pyautogui as pt, time

time.sleep(2)
f = open("book.txt",'r')

for word in f:
    pt.typewrite(word)
    pt.press("enter")
    