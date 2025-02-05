from math import ceil
from tkinter import *
import random
from tkinter import font
from tkinter import messagebox

# ===== GLOBAL Variables =======
auth_index=top_level_destroyed=lbl_index=0
main=main_color=root=fav=list_box=canvas=filled=manual_fill=entry=curser_index=show_canvas=None
obj=win=fg_color=bg_color=selected_label=main_hex_label=exhibit_label=exhibit_label_fg=exhibit_label_bg=None
members=[[0,0,[]],]
labels=[]
#====== clases ======
# -------- Field -----------
class Field:
    count_=0
    def __init__(self,name,window):
        Label(window,text=f'{name} : ',font='arial 20 bold').place(x=10,y=10+Field.count_*60)
        self.entry=Entry(window,width=20,font='arial 15 bold')
        self.entry.place(x=165,y=15+Field.count_*60)
        Field.count_ +=1

# ------- button change size ------
def configer(obj,font_size):
    obj.btn.config(font=f'arial {font_size} bold')

# ------ custom button defintion -------
class CustomButton:
    def __init__(self,window,dir,place_x,place_y,magic,width,color_,duty):
        self.btn=Button(window,text=dir,font='arial 20 bold',width=width,bg=color_, command=self.button_duty)
        self.btn.place(x=place_x,y=place_y)
        self.magic=magic
        self.duty=duty
        

    def button_duty(self):
        global selected_label, lbl_index,curser_index,entry,labels,main_color,main_hex_label,manual_fill,canvas

        # ======= magnifier =========
        if self.duty=='magnifier':
            wiget_font=font.Font(font=selected_label.cget('font'))
            font_size=wiget_font.cget('size')
            if self.magic[0]: 
                font_size +=2
            elif self.magic[1]: 
                font_size -=2
            selected_label.config(font=f'arial {font_size} bold')
        
        # ======= change color ======
        elif self.duty=='change_color':
            color='#'+''.join(random.choices('0123456789abcdef',k=6))
            if self.magic[0]==2:
                selected_label.config(bg=main_color)
            elif self.magic[0]:
                if self.magic[1]:
                    selected_label.config(bg=color)
                else:
                    selected_label.config(fg=color)
            else:
                main_color = color 
                root.config(bg=color)
                  
        # ======= transport ============ 
        elif self.duty=='transpose': 
            if self.magic[0]:
                x_place=selected_label.winfo_x()
                x_place -= self.magic[0]*15
                selected_label.place(x=x_place)

            if self.magic[1]:
                y_place=selected_label.winfo_y()
                y_place -=self.magic[1]*15
                selected_label.place(y=y_place)

        # ======== submit =========
        elif self.duty=='submit':
            entered_text=entry.get()
            label_=Label(root,text=entered_text,font='arial 20 bold',bg='yellow',fg='blue')
            label_.pack()
            labels.append(label_)
            entry.delete(0,END)
        # ======= sweatch ========
        elif self.duty=='sweatch':
            quantity =len(labels)
            if quantity > lbl_index +1:
                lbl_index=(lbl_index+1)%quantity
            elif quantity == lbl_index+1:
                lbl_index=0
            selected_label=labels[lbl_index]
        
        # ====== remove ========
        elif self.duty=='remove':
            labels.remove(selected_label)
            selected_label.destroy()
            lbl_index -=1
            try:
                selected_label=labels[lbl_index] 
            except:
                selected_label=labels[0]

        # ======== update ======== 
        elif self.duty=='update':
            entered_text=entry.get()
            selected_label.config(text=entered_text)

        # ======= add fav =======
        elif self.duty=='add_fav':
            rewatch_colors()
            if self.magic[1]==0:
                col=fg_color
            elif self.magic[1]==1:
                col=bg_color
            elif self.magic[1]==2:
                col=root.cget('bg')
            elif self.magic[1]== 3:
                ent=obj.entry.get().lower()
                if ent =="#"+''.join(list(filter(lambda x: x in '0123456789abcdef',ent ))) and len(ent)==7:
                    col=ent
            if col in (x := members[auth_index][2]):
                pass
            else:
                x.append(col)
                list_box.insert(END,col)
                color_colection()

        # ======= remove favorite color ========
        elif self.duty=='remove_fav':
            if curser_index := list_box.curselection():
                list_box.delete(curser_index)
                color_colection()

        # ====== manual ========
        elif self.duty=='manual':   
            ent=obj.entry.get().lower()
            if ent =="#"+''.join(list(filter(lambda x: x in '0123456789abcdef',ent ))) and len(ent)==7:
                if self.magic[0]==0:
                    canvas.itemconfig(manual_fill,fill=ent)
                elif self.magic[0]==1:
                    selected_label.config(fg=ent)
                elif self.magic[0]==2:
                    selected_label.config(bg=ent)
                elif self.magic[0]==3:
                    root.config(bg=ent)

        # ======== use favorite colors =======
        elif self.duty =='fav_as':
            if curser_index := list_box.curselection():
                col=list_box.get(curser_index)
                if self.magic[0]==1:
                    selected_label.config(fg=col)
                elif self.magic[0]==2:
                    selected_label.config(bg=col)
                elif self.magic[0]==3:
                    root.config(bg=col)
                  
        exhibit()


# ===== main ========
main=Tk()
main.geometry('400x300')

# ----- main fields ------
username= Field('username',main)
password= Field('password',main)

# ----- create register & login buttons
main.update()
x_place=(main.winfo_width()/2)-30
y_place=main.winfo_height()-30
btn_login=Button(main,text='login',font='arial 10 bold',command='login_form')
btn_register=Button(main,text='register',font='arial 20 bold',command='register_')
btn_login.place(x=x_place,y=y_place)
btn_register.place(x=x_place,y=y_place/2)

#----- create main label -----
lbl=Label(main,text='you have an account ?')
lbl.place(x=10,y=y_place)

# ---- functions ------
def clear():
    global username,password
    username.entry.delete(0,END)
    password.entry.delete(0,END)
    username.entry.focus_set()

def register_form():
    clear()
    global lbl,btn_login,btn_register
    main.title('register')
    lbl.config(text='you have an account')
    btn_login.config(text='login',command=login_form)
    btn_register.config(text='register',command=register_)
    
def register_():
    user=username.entry.get()
    passcode=password.entry.get()
    users=[ member[0] for member in members] 
    if user in users:
        messagebox.showerror('ALERT','you registered before')
    elif len(user)<5 or len(passcode)<5:
        messagebox.showerror('ALERT','enter more charecters')
    else:
        members.append([user,passcode,[]])
        login_form()
    clear()

def login_form():
    clear()
    global username,password,lbl,btn_login,btn_register
    main.title('login')
    lbl.config(text='you dont have an account?')
    btn_login.config(text='register',command=register_form)
    btn_register.config(text='login',command=login)

def login():
    global auth_index,list_box

    # ---- get entries ------
    user=username.entry.get()
    passcode=password.entry.get()
    
    # ----- authenticate ------
    found=False
    for i,member in enumerate(members):
       if user==member[0] and passcode==member[1]:
           win.deiconify()
           root.deiconify()
           fav.title(f'{user} - favorite colors')
           fav.deiconify()
           main.withdraw()
           auth_index=i
           for i in members[auth_index][2]:
               list_box.insert(0,i)
           color_colection()
           list_box.bind('<<ListboxSelect>>',show_color)
           found=True
           
    if not found:
        messagebox.showerror('ALERT','username or password is incorect')       



# ===== root ======

def high():
    root.update()
    return root.winfo_height()-30 

def create_root():
    global main_color,root,labels,selected_label,main_hex_label
    
    # ----- create root -------
    main_color='#'+''.join(random.choices('0123456789abcdef',k=6))
    root=Toplevel()
    root.withdraw()
    root.geometry('700x600+527+70')
    root.config(bg=main_color)
    root.title('screen')
    
    # ---- create hex label & hello! ------
    main_hex_label=Label(root,text=root.cget('bg'),fg=root.cget('bg'),font='arial 20 bold')
    main_hex_label.place(x=0,y=high())
    label=Label(root,text='hello',font='arial 20 bold',bg='black',fg='red')
    label.place(x=200,y=150)
    
    labels=[label,]
    selected_label=label
    configer(CustomButton(root,'+',120,root.winfo_height()-30,(0,2),4,'red','add_fav'),12)
    
# ---- rewatch colors ----- 
def rewatch_colors():
    global fg_color,bg_color
    fg_color=selected_label.cget("fg")
    bg_color=selected_label.cget('bg') 

create_root()

# ===== fav =======
def color_colection():
    size=list_box.size()
    for i in range(size):
        show_canvas.create_rectangle((i%7)*30,(i//7)*30,((i%7)+1)*30,((i//7)+1)*30,fill=list_box.get(i))
    for i in range(size,43,1):
        show_canvas.create_rectangle((i%7)*30,(i//7)*30,((i%7)+1)*30,((i//7)+1)*30,fill='white')


def create_fav():
    global fav,list_box,canvas,filled,manual_fill,obj,show_canvas
    fav=Toplevel()
    fav.withdraw()
    fav.geometry('490x287+20+383')
    fav.resizable(0,0)

    # ------ list_box ---------
    frame=Frame(fav)
    frame.place(x=415,y=10,width=70,height=260)
    list_box=Listbox(frame,font='arial 10 bold')
    list_box.place(x=0,y=0,width=65,height=260)
    skrolbar=Scrollbar(frame,orient=VERTICAL,command=list_box.yview)
    skrolbar.place(x=57,y=0,height=260,width=20)
    list_box.config(yscrollcommand=skrolbar.set)

    # ------ canvas ----------
    canvas=Canvas(fav,width=40,height=270)
    filled =canvas.create_rectangle(0,0,25,260,fill='white',outline='black')
    manual_fill=canvas.create_rectangle(0,130,25,260,fill='white')
    canvas.place(x=372,y=10)
    show_canvas=Canvas(fav,width=210,height=180)
    show_canvas.place(x=10,y=100)

    #  ------  hex field ------
    Field.count_=0
    obj=Field('hex',fav)
    obj.entry.config(width=20)
    obj.entry.place(x=100,y=15)
    
    # ------ fav botons -----
    configer(CustomButton(fav,'delete',230,250,(0,0),10,'red','remove_fav'),16)
    configer(CustomButton(fav,'fav_as_fg',230,100,(1,0),10,'#12349a','fav_as') ,16)  
    configer(CustomButton(fav,'fav_as_bg',230,150,(2,0),10,'#12349a','fav_as'),16)
    configer(CustomButton(fav,'fav_as_main',230,200,(3,0),10,'#12349a','fav_as'),16)
    configer(CustomButton(fav,'as_fg',10,50,(1,0),6,'#3b3b3b','manual'),16)  
    configer(CustomButton(fav,'as_bg',100,50,(2,0),6,'#3b3b3b','manual'),16)
    configer(CustomButton(fav,'as_main',190,50,(3,0),6,'#3b3b3b','manual'),16)
    configer(CustomButton(fav,'show',280,50,(0,0),6,'#3b3b3b','manual'),16)
    configer(CustomButton(fav,'+',330,18,(0,3),4,'red','add_fav'),8)
create_fav()

#====== create win =========

def exhibit():
    global exhibit_label,exhibit_label_bg,exhibit_label_fg,fg_color,bg_color
    
    rewatch_colors()
    main_bg=root.cget('bg')
    
    #  ----- exhibite labels -------
    exhibit_label_fg.config(text=fg_color,fg=fg_color)
    exhibit_label_bg.config(text=bg_color,fg=bg_color)
    exhibit_label.config(text=selected_label.cget('text'))

    # ------ main hex lable --------
    main_hex_label.config(text=main_bg,fg=main_bg)
    main_hex_label.place(x=0,y=high())

def create_win():
    global win,entry,exhibit_label,exhibit_label_bg,exhibit_label_fg

    win=Toplevel()
    win.withdraw()
    win.geometry("490x275+20+70")
    win.config(bg='#7F8498')
    win.title('just enjoy!')
    win.resizable(0,0)

    rewatch_colors()
    # ----- exhibite create --------
    exhibit_label=Button(win,text=selected_label.cget('text'),width=15,font='arial 20 bold')
    exhibit_label_fg=Button(win,text=fg_color,fg=fg_color,width=6,font='arial 12 bold')
    exhibit_label_bg=Button(win,text=bg_color,fg=bg_color,width=6,font='arial 12 bold')
    exhibit_label.place(x=200,y=10)
    exhibit_label_bg.place(x=200,y=50)
    exhibit_label_fg.place(x=270,y=50)

    # -----win entry ------
    font_=font.Font(family='helvetica',size=20)
    entry=Entry(win,font=font_,width=20)
    entry.place(x=0,y=230)

    # -----win buttons -----
    up=CustomButton(win,'^',60,55,(0,1),3,'#3b3b3b','transpose')
    down=CustomButton(win,'v',60,165,(0,-1),3,'#3b3b3b','transpose')
    right=CustomButton(win,'>',120,110,(-1,0),3,'#3b3b3b','transpose')
    up_right=CustomButton(win,'R1',120,55,(-1,1),3,'#3b3b3b','transpose')
    down_right=CustomButton(win,'R2',120,165,(-1,-1),3,'#3b3b3b','transpose')
    left=CustomButton(win,'<',0,110,(1,0),3,'#3b3b3b','transpose')
    up_left=CustomButton(win,'l1',0,55,(1,1),3,'#3b3b3b','transpose')
    down_left=CustomButton(win,'l2',0,165,(1,-1),3,'#3b3b3b','transpose')
    big_scale=CustomButton(win,'+',103,-2,(1,0),4,'#3b3b3b',duty='magnifier')
    small_scale=CustomButton(win,'-',0,-2,(0,1),4,'#3b3b3b',duty='magnifier')
    text_change_color=CustomButton(win,'f#',190,105,(1,0),3,'#3b3b3b',duty='change_color')
    win_change_color=CustomButton(win,'w#',190,165,(0,0),3,'#3b3b3b',duty='change_color')
    back_like_win=CustomButton(win,'wb#',255,165,(2,0),3,'#3b3b3b',duty='change_color')
    text_back_change_color=CustomButton(win,'b#',255,105,(1,1),3,'#3b3b3b',duty='change_color')
    submit=CustomButton(win,'enter',340,210,(0,0),7,'#6c91c2','submit')  
    sweath_text=CustomButton(win,'*',60,110,(0,0),3,'#3b3b3b','sweatch') 
    remove=CustomButton(win,'delete',340,80,(0,0),7,'red','remove') 
    update=CustomButton(win,'update',340,150,(0,0),7,'#3c6e47','update')
    configer(CustomButton(win,'+',285,75,(0,0),4,'red','add_fav'),8)
    configer(CustomButton(win,'+',215,75,(0,1),4,'red','add_fav'),8)
    
create_win()

#  ======== events ===========
def color_percent(color):
    #  ----- calculations ------
    color=color[1:]
    rgb=(color[0:2],color[2:4],color[4:])
    numbers_='0123456789abcdef'
    numeric=[numbers_.find(i[0])*16+numbers_.find(i[1]) for i in rgb ]
    rgb_units=list(map(lambda x : ceil(x * 260 /sum(numeric)),numeric))
    couple_sum=rgb_units[0]+rgb_units[1]

    #  ----- create percent regtangle ---------
    canvas.create_rectangle(25,0,60,rgb_units[0],fill='#ff0000')
    canvas.create_rectangle(25,rgb_units[0],60,couple_sum,fill='#00ff00')
    canvas.create_rectangle(25,couple_sum,60,260,fill='#0000ff')

# ------ fill show and percent regtangle with selected color -------
def show_color(event):
    global show_canvas
    curser_index=list_box.curselection()
    col=list_box.get(curser_index)
    canvas.itemconfig(filled,fill=col)
    color_percent(col)
    
# ----- create fav,root,win windows again --------
def destroyed(event):
    global top_level_destroyed,main
    if event.widget== fav or event.widget==win or event.widget== root:
        if top_level_destroyed < 2 :
            top_level_destroyed +=1
            
        else:
            create_fav()
            create_root()
            create_win()
            main.deiconify()
            clear()
            top_level_destroyed=0
            destroy_set()

# ------ set destroy --------
def destroy_set():
    fav.bind('<Destroy>',destroyed)
    root.bind('<Destroy>',destroyed)
    win.bind('<Destroy>',destroyed) 

list_box.bind('<<ListboxSelect>>',show_color)
destroy_set()             
register_form()
main.mainloop()