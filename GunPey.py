import tkinter

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def game_main():
    global cursor_x, cursor_y
    if 9 <= mouse_x and mouse_x < 9+24*5 and 57 <= mouse_y and mouse_y < 49+16*9:
        cursor_x = int((mouse_x-9)/24)
        cursor_y = int((mouse_y-57)/16)
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*24+21, cursor_y*16+65, image=cursor, tag="CURSOR")
    root.after(10, game_main)

root = tkinter.Tk()
root.title("GUNPEY")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
cvs = tkinter.Canvas(root, width=146, height=226)
cvs.pack()

bg = tkinter.PhotoImage(file="./image/GupPey_GameBoard_Stage.png")
cursor = tkinter.PhotoImage(file="./image/GupPey_GameBoard_Cursor.png")
cvs.create_image(73, 113, image=bg)
game_main()
root.mainloop()
