import tkinter as tk
import pickle as pkl
from math import sin, cos, pi
from time import sleep
from random import randint
from ball import ball
from bar import bar
from LangCfg import LangCfg

def isColliding(ball, bar):
    if(ball.posX >= bar.getX() and ball.posX <= (bar.getX() + 10) and ball.posY >= bar.getY() and ball.posY <= (bar.getY() + 100)):
        return True
    else:
        return False
    
def move(ball, elements):
    label.grid_remove()
    isPause=False
    while not isPause:
        ball.posX+= int(2*cos(ball.angle))
        ball.posY+= int(2*sin(ball.angle))

        if ball.posX>700:
            ball.bounceX()
            elements[1].score()
            bluescore.configure(text= elements[1].points)
            ball.posX=350
            ball.posY=200
            break

        if ball.posX<=0:
            ball.bounceX()
            elements[0].score()
            redscore.configure(text= elements[0].points) 
            ball.posX=350
            ball.posY=200
            break

        if (ball.posY>400 or ball.posY<0):
            ball.bounceY()
            continue

        for bar in elements:   
            if isColliding(ball, bar):
                ball.bounceX()
            
        ball.place(x=ball.posX, y=ball.posY)
        sleep(0.0005*ball.speed)   
        root.update()

    ball.place(x=ball.posX, y=ball.posY)
    sleep(0.0005*ball.speed)   
    root.update()   

def submitLang(lang, comp):
    configFile= open(".conf.txt", "w")
    #print(lang, comp)
    if lang==comp[0]:
        configFile.write("SPANISH")
    elif lang == comp[1]:
        configFile.write("ENGLISH")
    else:
        configFile.write("FRENCH")

    configFile.close()

def readlang():
    configfile= open(".conf.txt", "r")
    s= configfile.read()
    if s=="SPANISH":
        return LangCfg.SPANISH, LangCfg.español
    if s=="ENGLISH":
        return LangCfg.ENGLISH, LangCfg.english
    else:
        return LangCfg.FRENCH, LangCfg.français

def serialize(obj):
    pass

def deserialize(obj):
    pass

def cfgmenu(ball):
    menu= tk.Toplevel()
    menu.title("config menu")
    menu.geometry("300x200")
    menu.configure(background="black")

    lang=tk.StringVar(menu)
    lang.set(cfg_lang.name)
    spd=tk.StringVar(menu)
    spd.set(ball.speed)
    bounce=tk.StringVar(menu)
    bounce.set(randBounce)
    
    welcome= tk.Label(menu,bg='black', fg='white', font=('Times New Roman',10), text=cfg_lang.value[0])
    welcome.pack(padx=50, pady=10,)
    field1= tk.OptionMenu(menu, lang, *cfg_lang.value[2], command= lambda x: submitLang(lang.get(), cfg_lang.value[2]))
    field1.pack(padx=10, pady=5)
    field2= tk.OptionMenu(menu, spd, 1,2,3,4,5,6,7,8,9,10, command= lambda x: ball.setSpeed(float(spd.get())))
    field2.pack(padx=10, pady=5)
    field3= tk.OptionMenu(menu, bounce, "True", "False", command= lambda x: ball.setBounce(bool(bounce.get())))
    field3.pack(padx=10, pady=5)
    btn= tk.Button(menu, text= cfg_lang.value[5], command= lambda: [serialize(ball), menu.destroy()])
    btn.pack(padx=10,pady=5)
    
root = tk.Tk()
root.title("Ping Pong")
root.geometry("700x400")
root.configure(background="black")

l= readlang()
cfg_lang= l[1]
language= l[0]
ballSpeed= 4
randBounce= False
initAngle= pi/randint(3,6)
isPause=True

label= tk.Label(root, bg= 'black', fg= 'white', font= ('Times New Roman',12, 'bold'), text= language.value, justify= 'center')
label.grid(row=0, column=1, padx=190, pady=5)

bluebar = bar(root, bg="#15ADD6")
bluebar.place(x=50,y=50, height=100, width=10)

redbar= bar(root, bg="red")
redbar.place(x=650, y= 50, height=100, width=10)

bluescore= tk.Label(root, bg='black', fg='white', font=('Times New Roman',15), text= bluebar.points)
bluescore.place(x=25, y=10)

redscore= tk.Label(root, bg='black', fg='white', font=('Times New Roman',15), text= redbar.points)
redscore.place(x=675, y=10)

elements= [redbar, bluebar]

bola= ball(parent= root, speed=ballSpeed, angle=initAngle, random=randBounce, color= "white")

root.bind("<t>", lambda evt: move(bola, elements))
root.bind("<c>", lambda evt: cfgmenu(bola))
root.bind("<w>", lambda evt: bluebar.moveUp())
root.bind("<s>", lambda evt: bluebar.moveDown())
root.bind("<i>", lambda evt: redbar.moveUp())
root.bind("<k>", lambda evt: redbar.moveDown())
root.mainloop()