from tkinter import *
from box import Box
import settings
import util

root = Tk()
# settings override
root.configure(bg="#5461FF")
root.iconbitmap('icons/icon_main.ico')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Battleship Bomber')
root.resizable(False,False)


top_sec = Frame(                        #top frame
    root,
    bg='#5461FF',
    width=util.settings.WIDTH,
    height=util.height_per(20)
)
top_sec.place(x=0,y=0)

bg= PhotoImage(file = 'icons/C64_bg.png')     #Top label
top_label = Label(top_sec, image=bg)
top_label.place(
    x=-2,
    y=0,
)

left_sec =Frame(              #left frame
    root,
    bg='#5461FF',
    width=util.width_per(25),
    height=util.height_per(80)
)
left_sec.place(x=0,y=util.height_per(21))

main_sec =Frame(                #center frame
    root,
    bg = '#5461FF',
    width=util.width_per(75),
    height=util.height_per(79)
)

main_sec.place(
    x=util.width_per(25),
    y=util.height_per(21)
)

def place_boxes():

    settings.G_SIZE = 6

    for x in range(settings.G_SIZE):                        #Boxes placed
        for y in range(settings.G_SIZE):
            b= Box(x, y)
            b.create_btn_obj(main_sec)

            b.box_btn_obj.grid(
                column=x,
                row=y
            )

    Box.randomize_ship()
    for b in Box.all:                   # randomizing ship
        print(b.is_ship)

    Box.box_count = 36
    Box.ship_count = 1
    Box.create_box_count_label(left_sec)
    Box.box_count_label_obj.place(x=2, y=50)  # Boxes Left LABEL


    Box.create_ship_label(left_sec)
    Box.ship_count_object.place(x=2, y=140)  # Ships Left LABEL

    #b.destroy()


place_boxes()

Box.create_over_lbl(root)

def refresh():
    #b.box_btn_obj.destroy()
    place_boxes()
    Box.over_obj.destroy()
    #pop_up.no_msg()                                    #refresh



def help_window():                                       #Help window
    new = Tk()
    new.geometry('490x350')
    new.title('Help')
    new.configure(bg='black')
    new.iconbitmap('icons/icon_main.ico')
    new.resizable(False, False)

    top_lb = Label(
        new,
        text='How to Play:',
        font=('Helvetica', 25),
        bg='black',
        fg='white'
    )
    top_lb.grid(row=0, column=0)

    sml_txt = Label(
        new,
        text='A random Battle Ship is placed in the boxes,\nyou have to bomb the ship within limited\nnumber of moves',
        font=('arial', 18),
        bg='black',
        fg='white'
    )
    sml_txt.grid(row=1, column=0)

    sec_lb = Label(
        new,
        text='Controls:',
        font=('Helvetica', 25),
        bg='black',
        fg='white'
    )
    sec_lb.grid(row=2, column=0)

    con_txt = Label(
        new,
        text='You can bomb the boxes by clicking on them\nLeft click will create a blast\nRight click will only bomb one box',
        font=('arial', 18),
        bg='black',
        fg='white'
    )
    con_txt.grid(row=3, column=0)

    ok_btn = Button(
        new,
        text='ok',
        font=("", 19),
        bg="brown",
        fg='yellow',
        command=new.destroy
    )
    ok_btn.grid(row=4, column=0, pady=25)

    new.mainloop()


new_game = PhotoImage(file='icons/newgame.png')
New_game = Button(
    left_sec,
    image=new_game,                                          #New Game
    bg='#5461FF',
    width = 150,
    height = 73,
    borderwidth=0,
    command=refresh
)
New_game.place(x=25, y=360)


help_img = PhotoImage(file='icons/help.png')                 #Help button
help_btn = Button(
    left_sec,
    image=help_img,
    bg='#5461FF',
    width=150,
    height=73,
    borderwidth=0,
    command=help_window
)
help_btn.place(x=25, y=260)

quit_game = PhotoImage(file='icons/quit.png')                 #Quit button
Q_game = Button(
    left_sec,
    image=quit_game,
    bg='#5461FF',
    width = 150,
    height = 73,
    borderwidth=0,
    command=root.destroy
)
Q_game.place(x=25, y=460)



# Windows Run
root.mainloop()