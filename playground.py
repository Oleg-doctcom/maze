from tkinter import *
import random

window = Tk()
window.geometry('800x600')
window.title('Canvas')

canvas=Canvas(height=450, width=450,relief=SOLID,bd=1,bg='white')

walls=[]
doors=[]
keys=[]
exits=[]
secrets=[]
lavas=[]
players=[]

def createLevel(level):
    walls.clear()
    keys.clear()
    doors.clear()
    exits.clear()
    secrets.clear()
    lavas.clear()
    players.clear()


    x=0
    y=0
    side=25
    for line in level:
        for block in line:
            if block=='W':
                wall=canvas.create_rectangle(x,y,x+side,y+side,fill='black',outline='black')
                walls.append(wall)
            if block=='K':
                key=canvas.create_rectangle(x,y,x+side,y+side,fill='yellow',outline='yellow')
                keys.append(key)
            if block=='D':
                door=canvas.create_rectangle(x,y,x+side,y+side,fill='red',outline='red')
                doors.append(door)
            if block=='E':
                exit=canvas.create_rectangle(x,y,x+side,y+side,fill='orange',outline='orange')
                exits.append(exit)
            if block=='S':
                secret=canvas.create_rectangle(x,y,x+side,y+side,fill='#111111',outline='#111111')
                secrets.append(secret)
            if block=='L':
                lava=canvas.create_rectangle(x,y,x+side,y+side,fill='#f74600',outline='#f74600')
                lavas.append(lava)
            if block=='P':
                player=canvas.create_rectangle(x+1,y+1,x+side-1,y+side-1,fill='blue',outline='blue')
                players.append(player)
            x+=side
        y+=side
        x=0

canvas.pack(expand=True)

if __name__=='__main__':
    window.mainloop()