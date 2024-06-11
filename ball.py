import tkinter as tk
from math import pi, sin
from random import randint, random

class ball (tk.Frame):
    def __init__(self, parent, speed=2, angle=pi/5, random= False, color="black"):
        self.posX=350
        self.posY=200
        self.speed=speed
        self.angle= angle
        self.random= random
        super().__init__(parent,bg= color)
        self.place(x=self.posX, y=self.posY, height=10, width=10)

    def setAngle(self, angle):
        self.angle= angle
        
    def setSpeed(self, speed):
        #print(speed)
        self.speed= speed

    def setBounce(self, bounce):
        self.random=bounce

    def bounceX(self):

        if self.random:
            incident= self.angle+(randint(-3,3)*0.2)
 
        else:
            incident= self.angle

        incident= (pi)-incident
        self.setAngle(incident)

    def bounceY(self):
        incident= 2*pi-self.angle
        self.setAngle(incident)