import tkinter
import random
import time

upTimer = 0
insertnow = 0

gunpey = [
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 4, 0,],
    [0, 0, 0, 0, 0,],
    [1, 2, 3, 4, 0,],
    [0, 0, 0, 0, 0,]
]

def draw_panel():
    for y in range(10):
        for x in range(5):
            if gunpey[y][x] > 0:
                cvs.create_image(x*24+21, y*16+57, image=img_panel[gunpey[y][x]], tag="PANEL")

def in_panel():
    global slot,insertnow
    insertnow = 1
    cvs.create_image(69, 201, image=slot, tag="SLOT")
    insert = [0, 0, 0, 0, 0]
    for x in range(5):
        insert[x] = random.randint(0, 4)
    for x_point in range(60, 0, -1):
        cvs.delete("INSERT")
        for x in range(5):
            cvs.create_image(x*24+21, 201, image=img_panel[insert[x]], tag="INSERT")
            print("hey"+str(x*24+21+x_point) + ":" + str(insertnow) + ":" + str(insert[x]))
        time.sleep(0.1)
        print(x_point)    
    cvs.delete("INSERT")
    for x in range(5):
        gunpey[9][x] = insert[x] # Insert the new panel 9,193
    cvs.delete("SLOT")
    insertnow = 0

def up_panel():
    for y in range(1, 10):
        for x in range(5):
            gunpey[y-1][x] = gunpey[y][x]
            gunpey[y][x] = 0
        
def game_over():
    print("GameOver")

def game_main():
    global upTimer, insertnow
    cvs.delete("CURSOR")
    cvs.delete("PANEL")
    if insertnow == 0:
        draw_panel()
    upTimer += 1
    print(upTimer)
    if upTimer >= 33:
        sum_panel = 0
        for x in range(5):
            sum_panel += gunpey[0][x]
        if sum_panel == 0:
            up_panel()
            in_panel()
        else:
            game_over()
        upTimer = 0
    root.after(100, game_main)

root = tkinter.Tk()
root.title("GUNPEY")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=146, height=226)
cvs.pack()

bg = tkinter.PhotoImage(file="./image/GupPey_GameBoard_Stage.png")
cursor = tkinter.PhotoImage(file="./image/GupPey_GameBoard_Cursor.png")
slot = tkinter.PhotoImage(file="./image/GupPey_GameBoard_Slot.png")
img_panel = [
    None,
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_Z.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_N.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_A.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_V.png"),
]

cvs.create_image(73, 113, image=bg)
game_main()
root.mainloop()
