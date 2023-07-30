import tkinter


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
                cvs.create_image(x*24+21, y*16+57, image=img_panel[gunpey[y][x]])

root = tkinter.Tk()
root.title("GUNPEY")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=146, height=226)
cvs.pack()

bg = tkinter.PhotoImage(file="gunpey_stage.png")
img_panel = [
    None,
    tkinter.PhotoImage(file="gunpey_panel_Z.png"),
    tkinter.PhotoImage(file="gunpey_panel_N.png"),
    tkinter.PhotoImage(file="gunpey_panel_A.png"),
    tkinter.PhotoImage(file="gunpey_panel_V.png"),
]

cvs.create_image(73, 113, image=bg)
draw_panel()
root.mainloop()
