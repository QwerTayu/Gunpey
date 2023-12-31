import tkinter

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

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

def game_main():
    global cursor_x, cursor_y, mouse_c
    if 9 <= mouse_x and mouse_x < 9+24*5 and 57 <= mouse_y and mouse_y < 49+16*9:
        cursor_x = int((mouse_x-9)/24)
        cursor_y = int((mouse_y-57)/16)
        if mouse_c == 1:
            mouse_c = 0
            tmp = 0
            tmp = gunpey[cursor_y][cursor_x]
            gunpey[cursor_y][cursor_x] = gunpey[cursor_y+1][cursor_x]
            gunpey[cursor_y+1][cursor_x] = tmp
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*24+21, cursor_y*16+65, image=cursor, tag="CURSOR")
    cvs.delete("PANEL")
    draw_panel()
    root.after(100, game_main)

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
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_Z.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_N.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_A.png"),
    tkinter.PhotoImage(file="./image/Panels/GupPey_GameBoard_Panels_V.png"),
]

cvs.create_image(73, 113, image=bg)
game_main()
root.mainloop()
