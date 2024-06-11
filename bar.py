import tkinter as tk

class bar (tk.Frame):
    step=40
    def __init__(self, root, bg='white', points=0):
        super().__init__(root, bg=bg)
        self.points= points

    def score(self):
        self.points+=1

    def getX(self):
        cord= self.winfo_x()
        return cord
    
    def getY(self):
        cord= self.winfo_y()
        return cord

    def getWidth(self):
        return self.winfo_width
    
    def getHeight(self):
        return self.winfo_height
    
    def moveUp(self):
        coordinate= self.winfo_y()
        self.place(y=coordinate-self.step)

    def moveDown(self):
        coordinate= self.winfo_y()
        self.place(y=coordinate+self.step)