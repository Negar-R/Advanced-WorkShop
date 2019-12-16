from tkinter import *
import time


root = Tk()

timer = Label(root , font = ('Tahoma' , 80) , width = 6 , heigh = 2)
timer.pack()

counter = 0
todo = True

def Ttime():
    global counter

    if not todo:
        return 
 
    if counter < 100:
        counter += 1
        name = str(counter)
        time.sleep(1) #bade 1S counter ro ++ mikone
        timer.config(text = name) #text ro mazare tu window
    timer.after(50 , start) #bad az 50 ms dobare function start ro ejra mikone

def stop():
    # global todo 
    todo = False 
    Ttime() 

def start():
    global todo
    todo = True
    Ttime()    

def restart():
    global counter
    counter = 0
    name = str(counter)
    # timer.config(text = name) #text ro mIzare tu window
    timer.config(text = name)

# start()
btn1 = Button(root , text = "Start Timer"  , command = start)  
btn1.place(x = 0 , y = 0) 

btn2 = Button(root , text = "Reset" , command = restart)
btn2.place(x = 300 , y = 0)

btn3 = Button(root , text = "Stop" , command = stop)
btn3.place(x = 600 , y = 0)

root.mainloop()