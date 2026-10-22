from tkinter import *
import time
class Ball:

    def __init__(self,canvas,x,y,diameter,xvelocity,yvelocity,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity

    def bouncing(self):
        coordinates = self.canvas.coords(self.image)
        if (coordinates[2]>= (self.canvas.winfo_width()) or coordinates[0]<0):
            self.xvelocity = -self.xvelocity
        if (coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yvelocity = -self.yvelocity

        self.canvas.move(self.image,self.xvelocity,self.yvelocity)



window = Tk()
window.title("kevin's funny balls")
WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
ball1 = Ball(canvas,0,0,100,4,2,"blue")
ball2 = Ball(canvas,0,0,50,3,4,"red")
ball3 = Ball(canvas,0,0,125,8,7,"orange")
ball4 = Ball(canvas,0,0,75,10,15,"green")
ball5 = Ball(canvas,2,2,150,5,6,"yellow")
ball6 = Ball(canvas,250,250,170,9,5,"white")
ball7 = Ball(canvas,3,3,100,10,7,"black")
canvas.pack()

while True:
    ball1.bouncing()
    ball2.bouncing()
    ball3.bouncing()
    ball4.bouncing()
    ball5.bouncing()
    ball6.bouncing()
    ball7.bouncing()
    window.update()
    time.sleep(0.01)


window.mainloop()