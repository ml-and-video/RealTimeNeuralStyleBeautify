from tkinter import *
from tkinter import messagebox
import init as initial
import subprocess
from PIL import Image, ImageTk

mainDir = ''
def click():
	Label(window, text = 'You pressed button!', bg = 'black', fg = 'white', font = 'arial 18 bold').grid(row = 2, column = 1, sticky = E)

def image1():
	subprocess.call(["python", "init.py", "-i", str(mainDir)])
def image2():
	subprocess.call(["python", "init.py", "-i", str(mainDir), "-md","/home/shubham/Desktop/NeuralStyle/Neural-Style-Transfer-with-OpenCV-master/models/instance_norm/feathers.t7"] )
def image3():
	subprocess.call(["python", "init.py", "-i", str(mainDir), "-md","/home/shubham/Desktop/NeuralStyle/Neural-Style-Transfer-with-OpenCV-master/models/instance_norm/la_muse.t7"] )
def image4():
	subprocess.call(["python", "init.py", "-i", str(mainDir), "-md","/home/shubham/Desktop/NeuralStyle/Neural-Style-Transfer-with-OpenCV-master/models/instance_norm/mosaic.t7"] )
def image5():
	subprocess.call(["python", "init.py", "-i", str(mainDir), "-md","/home/shubham/Desktop/NeuralStyle/Neural-Style-Transfer-with-OpenCV-master/models/instance_norm/the_scream.t7"] )
def image6():
	subprocess.call(["python", "init.py", "-i", str(mainDir), "-md","/home/shubham/Desktop/NeuralStyle/Neural-Style-Transfer-with-OpenCV-master/models/instance_norm/udnie.t7"] )
def video1():
	subprocess.call(["python", "init.py", "-md","/home/shubham/Desktop/NeuralStyle/Neural-Style-Transfer-with-OpenCV-master/models/instance_norm/feathers.t7"])
def video2():
	subprocess.call(["python", "init.py", "-md","/home/shubham/Desktop/NeuralStyle/Neural-Style-Transfer-with-OpenCV-master/models/instance_norm/la_muse.t7"])
def video3():
	subprocess.call(["python", "init.py", "-md","/home/shubham/Desktop/NeuralStyle/Neural-Style-Transfer-with-OpenCV-master/models/instance_norm/mosaic.t7"])
def video4():
	subprocess.call(["python", "init.py", "-md","/home/shubham/Desktop/NeuralStyle/Neural-Style-Transfer-with-OpenCV-master/models/instance_norm/the_scream.t7"])
def video5():
	subprocess.call(["python", "init.py", "-md","/home/shubham/Desktop/NeuralStyle/Neural-Style-Transfer-with-OpenCV-master/models/instance_norm/udnie.t7"])
def video6():
	subprocess.call(["python", "init.py"])
def submitDir():
	global mainDir
	directory = v.get()
	mainDir  = str(directory)


initial.printTest()

window = Tk()
window.title('Beautify!')
window.geometry("1192x600")
window.resizable(0,0)

photo1 = PhotoImage(file = '/home/shubham/Downloads/cool-background1.png')

C = Canvas(window, bg="blue", height=250, width=300)
filename = PhotoImage(file = "/home/shubham/Downloads/cool-background1.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#Label(window, image = photo1, bg = 'blue').grid(row = 0, column = 0, sticky = E)
window.configure(background = 'black')
Label(window, text = 'CarpeDiem', bg = 'black', fg = 'white', font = 'arial 12 bold').place(relx = 0.5, rely = 0.1, anchor = CENTER)
#Button(window, text = 'Test!', height = 10, width = 10, command = click).grid(row = 2, column = 0, sticky = E)
a = Label(window, text = 'Beautify Image', bg = 'black', fg = 'white', font = 'arial 12 bold').place(relx = 0.1, rely = 0.1, anchor = CENTER)
Label(window, text = '(select a particular style)', bg = 'black', fg = 'white', font = 'arial 10').place(relx = 0.15, rely = 0.15, anchor = CENTER)
Button(a, text = 'Candy', width = 9, command = image1).place(relx = 0.1, rely = 0.20, anchor = CENTER)
Button(a, text = 'Feathers', width = 9, command = image2).place(relx = 0.1, rely = 0.25, anchor = CENTER)
Button(a, text = 'LaMuse', width = 9, command = image3).place(relx = 0.1, rely = 0.30, anchor = CENTER)
Button(a, text = 'Mosaic', width = 9, command = image4).place(relx = 0.1, rely = 0.35, anchor = CENTER)
Button(a, text = 'TheScream', width = 9, command = image5).place(relx = 0.1, rely = 0.40, anchor = CENTER)
Button(a, text = 'Udnie', width = 9, command = image6).place(relx = 0.1, rely = 0.45, anchor = CENTER)
a = Label(window, text = 'Beautify Video', bg = 'black', fg = 'white', font = 'arial 12 bold').place(relx = 0.85, rely = 0.1, anchor = CENTER)
Label(window, text = '(select a particular style)', bg = 'black', fg = 'white', font = 'arial 10').place(relx = 0.90, rely = 0.15, anchor = CENTER)
#Button(window, text = 'Video', width = 9, command = video).place(relx = 0.5, rely = 0.9, anchor = CENTER)


Button(a, text = 'Candy', width = 9, command = video1).place(relx = 0.85, rely = 0.20, anchor = CENTER)
Button(a, text = 'Feathers', width = 9, command = video2).place(relx = 0.85, rely = 0.25, anchor = CENTER)
Button(a, text = 'LaMuse', width = 9, command = video3).place(relx = 0.85, rely = 0.30, anchor = CENTER)
Button(a, text = 'Mosaic', width = 9, command = video4).place(relx = 0.85, rely = 0.35, anchor = CENTER)
Button(a, text = 'TheScream', width = 9, command = video5).place(relx = 0.85, rely = 0.40, anchor = CENTER)
Button(a, text = 'Udnie', width = 9, command = video6).place(relx = 0.85, rely = 0.45, anchor = CENTER)
v = StringVar()
textentry = Entry(window, textvariable = v, width = 20, bg = 'white').place(relx = 0.5, rely = 0.5, anchor = CENTER)

Button(window, text = 'Submit', font = 'arial 10', width = 6, command = submitDir).place(relx = 0.6, rely = 0.5, anchor = CENTER)
Label(window, text = 'enter the directory of image:', bg = 'black', fg = 'white', font = 'arial 10').place(relx = 0.33, rely = 0.5, anchor = CENTER)





window.mainloop()
