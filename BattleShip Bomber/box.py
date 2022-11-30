from tkinter import *
import util
import random
import settings
import ctypes

class Box:

    all=[]


    box_count = settings.BOX_COUNT
    ship_count = settings.SHIP_NUM

    box_count_label_obj = None
    ship_count_object = None
    over_obj = None
    
    def __init__(self, x, y, is_ship=False):

        self.is_open = False
        self.is_ship = is_ship
        self.box_btn_obj = None
        self.x = x
        self.y = y
        self.c = None
        #append the obj to Box.all list
        Box.all.append(self)

    def create_btn_obj(self,location):
        global btn
        btn = Button(location)
        btn.destroy()
        btn = Button(
            location,
            bg = 'brown',
            width = 12,  #New logic to be placed for dynamic button size per level
            height = 4,
            borderwidth = 5,
            font = ("TimesNewRoman",9)
        )
        btn.bind('<Button-1>', self.left_click_act)  #left click
        btn.bind('<Button-3>', self.right_click_act)  #right click
        self.box_btn_obj = btn


    @staticmethod
    def create_box_count_label(location):
        lbl = Label(
            location,
            bg = 'black',
            fg = 'white',
            text = f"Boxes Left:{Box.box_count}",
            font=("",30)
            )

        Box.box_count_label_obj = lbl


    @staticmethod
    def create_ship_label(location):
        lbl_s = Label(
            location,
            bg = 'black',
            fg = 'white',
            text = f"Ships Left:{Box.ship_count}",
            font=("",30)
            )

        Box.ship_count_object = lbl_s

    @staticmethod
    def create_over_lbl(location):
        text_lbl = Label(location)

        Box.over_obj = text_lbl



    def show_ship(self,photo):
        
        self.box_btn_obj.configure(image = photo,
                                   bg = 'White',
                                   borderwidth = 0,
                                   width = 95,
                                   height = 73                                   
                                )

    def get_box_axis(self, x, y):
        # return box obj in terms of x,y
        for box in Box.all:
            if box.x == x and box.y == y:
                return box

    @property
    def sur_boxes(self):
        
        boxes = [
            self.get_box_axis(self.x - 1, self.y - 1),
            self.get_box_axis(self.x - 1, self.y),
            self.get_box_axis(self.x - 1, self.y + 1),
            self.get_box_axis(self.x, self.y - 1),
            self.get_box_axis(self.x + 1, self.y - 1),
            self.get_box_axis(self.x + 1, self.y),
            self.get_box_axis(self.x + 1, self.y + 1),
            self.get_box_axis(self.x, self.y + 1)                   
        ]
        
        boxes = [box for box in boxes if box is not None]

        return boxes

    @property
    def ships_count(self):
        counter = 0
        for box in self.sur_boxes:
            if box.is_ship:
                counter += 1

        return counter

    def show_box(self):

        if not self.is_open:

            
            self.box_btn_obj.configure(text = self.ships_count,
                                       bg = '#5461FF',
                                       width=12,
                                       height=4,
                                       borderwidth=5
                                       )

            Box.box_count -= 1

            if (Box.box_count == 22):  # Losing logic

                Box.over_obj.configure(
                    text = 'GAME OVER',
                    bg = 'black',
                    fg = 'white',
                    font = ("",100)
                )

                Box.over_obj.place(
                    x=util.width_per(18),
                    y=util.height_per(45)
                )

            #Dynamic Display lebel

            if Box.box_count_label_obj:
                Box.box_count_label_obj.configure(
                    text = f"Boxes Left:{Box.box_count}"
                    )


        self.is_open = True     #marking box as already bombed


    def left_click_act(self, event):
        if self.is_ship:
            global photo
            photo = PhotoImage(file = 'icons/shp.png')
            self.show_ship(photo)

            self.ship_count_object.configure(
                text = "Ships Left:0"
            )

            self.box_btn_obj.unbind('<Button-1>')
            self.box_btn_obj.unbind('<Button-3>')
            
            ctypes.windll.user32.MessageBoxW(0, 'You Bombed the Ship!!', 'Victory', 0)
         
        else:
            if self.ships_count == 0:
                for box_obj in self.sur_boxes:
                    box_obj.show_box()
                    
            self.show_box()

            #Canceling clicks

            self.box_btn_obj.unbind('<Button-1>')
            self.box_btn_obj.unbind('<Button-3>')



    def right_click_act(self, event):
        if self.is_ship:
            global photo
            photo = PhotoImage(file = 'icons/shp.png')
            self.show_ship(photo)

            self.ship_count_object.configure(
                text = "Ships Left:0"
            )

            self.box_btn_obj.unbind('<Button-1>')
            self.box_btn_obj.unbind('<Button-3>')
            
            ctypes.windll.user32.MessageBoxW(0, 'You Bombed the Ship!!', 'Victory', 0)
             
        else:
            self.show_box()

            #Canceling clicks

            self.box_btn_obj.unbind('<Button-1>')
            self.box_btn_obj.unbind('<Button-3>')


    @staticmethod
    def randomize_ship():
        picked_box= random.sample(
            Box.all,
            settings.SHIP_NUM
        )
        for picked in picked_box:
            picked.is_ship = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"