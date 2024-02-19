from levels import levels
from playground import window, canvas, walls, keys, doors, exits, createLevel, players, lavas
from tkinter import *

currentLevel = 0
createLevel(levels[currentLevel])


def playerMove(event):
    global currentLevel
    player = players[0]
    key = event.keysym
    x = 0
    y = 0
    if key == "Up":
        y -= 5
    if key == "Down":
        y += 5
    if key == "Right":
        x += 5
    if key == "Left":
        x -= 5
    canvas.move(player, x, y)

    for wall in walls:
        x1,y1,x2,y2=canvas.coords(wall)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.move(player,-x,-y)

    for key in keys:
        x1, y1, x2, y2 = canvas.coords(key)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.delete(key)
            keys.remove(key)
            if len(keys) == 0:
                for door in doors:
                    canvas.itemconfig(door, fill='green', outline='green')

    for door in doors:
        x1, y1, x2, y2 = canvas.coords(door)
        if canvas.itemcget(door, 'fill') == 'red':
            if player in canvas.find_overlapping(x1, y1, x2, y2):
                canvas.move(player, -x, -y)

    for lava in lavas:
        x1,y1,x2,y2=canvas.coords(lava)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.delete('all')
            createLevel(levels[currentLevel])

    for exit in exits:
        x1, y1, x2, y2 = canvas.coords(exit)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.delete('all')
            currentLevel += 1

            if currentLevel<len(levels):
                createLevel(levels[currentLevel])
            else:
                canvas.unbind_all('<Key>')
                canvas.create_text(200,200,text='You won',font='arial 40',fill='green')
                return



canvas.bind_all('<Key>', playerMove)

window.mainloop()
