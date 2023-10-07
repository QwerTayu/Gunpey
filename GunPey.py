import tkinter
import random
import time

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0
gameTime = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

normalPanel = [
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,]
]

def new_panel():

    weights = [8, 1, 1, 1, 1]

    isPanelExist = False
    
    while isPanelExist == False:
        newPanel = random.choices(range(5), weights=weights, k=5)
        for x in range(5):
            if newPanel[x] != 0:
                isPanelExist = True
                break

    for y in range(1, 10):
        for x in range(5):
            normalPanel[y-1][x] = normalPanel[y][x]

    normalPanel[9] = newPanel

def draw_panel(panel):
    for y in range(10):
        for x in range(5):
            if panel[y][x] > 0:
                cvs.create_image(x*24+21, y*16+57, image=img_panel[panel[y][x]], tag="PANEL")

def handleClickChange(normalPanel):
    global cursor_x, cursor_y, mouse_c
    if 9 <= mouse_x and mouse_x < 9+24*5 and 57 <= mouse_y and mouse_y < 49+16*9:
        cursor_x = int((mouse_x-9)/24)
        cursor_y = int((mouse_y-57)/16)
        if mouse_c == 1:
            mouse_c = 0
            tmp = 0
            tmp = normalPanel[cursor_y][cursor_x]
            normalPanel[cursor_y][cursor_x] = normalPanel[cursor_y+1][cursor_x]
            normalPanel[cursor_y+1][cursor_x] = tmp

def game_main():
    global cursor_x, cursor_y, mouse_c, gameTime
    handleClickChange(normalPanel)
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*24+21, cursor_y*16+65, image=cursor, tag="CURSOR")
    cvs.delete("PANEL")
    draw_panel(normalPanel)
    cvs.tag_raise("SLOT")
    root.after(100, game_main)
    gameTime += 1
    if gameTime % (10 * 10) == 0: # 10秒ごとにパネルを生成
        new_panel()
        cvs.create_image(2*24+21, 8.5*16+65, image=slot, tag="SLOT")
    if gameTime % (10 * 10) == 3:
        cvs.delete("SLOT") 

root = tkinter.Tk()
root.title("GUNPEY")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
cvs = tkinter.Canvas(root, width=146, height=226)
cvs.pack()

bg = tkinter.PhotoImage(file="./image/GupPey_GameBoard_Stage.png")
cursor = tkinter.PhotoImage(file="./image/GupPey_GameBoard_Cursor.png")
img_panel = [
    None,
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_Z_0.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_N_0.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_A_0.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_V_0.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_Z_1.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_N_1.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_A_1.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_V_1.png"),
]
slot = tkinter.PhotoImage(file="./image/GupPey_GameBoard_Slot.png")

cvs.create_image(73, 113, image=bg)
game_main()
root.mainloop()
