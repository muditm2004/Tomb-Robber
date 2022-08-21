from tkinter import * #for gui
from tkVideoPlayer import TkinterVideo #for vdos
import pygame #for song

pygame.mixer.init()


window=Tk()
window.geometry('750x450')
window.maxsize(750,450)
window.title('Rookie Coders')
header_lbl=Label(text='Tomb Robbers',font=('harrington 18 bold'))
header_lbl.pack()

bgvdo=TkinterVideo(master=window,scaled=True)
bgvdo.load("C:\\Users\\mudit\\OneDrive\\Desktop\\New folder\\WhatsApp Video 2022-08-21 at 9.45.39 AM.mp4")
bgvdo.pack(expand=True,fill=BOTH)
bgvdo.play()

def death():
    global window
    window.destroy()
    window=Tk()
    window.geometry('750x450')
    window.maxsize(750,450)
    window.title('Rookie Coders')

    header_lbl=Label(text='You Died due to poisonous gas',font=('harrington 18 bold'))
    header_lbl.pack()

    bgvdo=TkinterVideo(master=window,scaled=True)
    bgvdo.load("C:\\Users\\mudit\\OneDrive\\Desktop\\New folder\\video_removal_video_1661057841452_.mp4")
    bgvdo.pack(expand=True,fill=BOTH)
    bgvdo.play()

    window.mainloop()

def treasure():
    global window
    window.destroy()
    window=Tk()
    window.geometry('750x450')
    window.maxsize(750,450)
    window.title('Rookie Coders')

    header_lbl=Label(text='Congrats You found the treasure',font=('harrington 18 bold'))
    header_lbl.pack()

    bgvdo=TkinterVideo(master=window,scaled=True)
    bgvdo.load("C:\\Users\\mudit\\OneDrive\\Desktop\\New folder\\video_removal_video_1661011279991_.mp4")
    bgvdo.pack(expand=True,fill=BOTH)
    bgvdo.play()

    window.mainloop()


def riddle4():
    global window
    window.destroy()

    window=Tk()
    window.geometry('750x450')
    window.maxsize(750,450)
    window.title('Rookie Coders')
    
    head_lbl=Label(text='Choose the Great Pyramid of Giza',font=('Harrington',16,'bold'),background='white')
    head_lbl.pack()

    r1_bg_img=PhotoImage(file="C:\\Users\\mudit\\OneDrive\\Desktop\\New folder\\Constellations (6).png")
    r1_bg=Label(image=r1_bg_img)
    r1_bg.pack()

    btn1=Button(text='Select',cursor='target',background='DarkSalmon',command=treasure)
    btn1.place(x=100,y=190)

    btn3=Button(text='Select',cursor='target',background='DarkSalmon',command=death)
    btn3.place(x=500,y=190)

    btn2=Button(text='Select',cursor='target',background='DarkSalmon',command=death)
    btn2.place(x=320,y=190)

    btn4=Button(text='Select',cursor='target',background='DarkSalmon',command=death)
    btn4.place(x=650,y=190)

    btn5=Button(text='Select',cursor='target',background='DarkSalmon',command=death)
    btn5.place(x=100,y=390)

    btn6=Button(text='Select',cursor='target',background='DarkSalmon',command=death)
    btn6.place(x=290,y=390)

    btn7=Button(text='Select',cursor='target',background='DarkSalmon',command=death)
    btn7.place(x=500,y=390)

    btn8=Button(text='Select',cursor='target',background='DarkSalmon',command=death)
    btn8.place(x=650,y=390)

    window.mainloop()



def gate2r4():
    bgvdo=TkinterVideo(master=window,scaled=True)
    bgvdo.load("C:\\Users\\mudit\\OneDrive\\Desktop\\New folder\\WhatsApp Video 2022-08-21 at 9.45.39 AM.mp4")
    bgvdo.pack(expand=True,fill=BOTH)
    bgvdo.play()

def game_start_intro1():
    global window
    window.destroy()
    window=Tk()
    window.geometry('750x450')
    window.maxsize(750,450)
    window.title('Rookie Coders')
    bgvdo=TkinterVideo(master=window,scaled=True)
    bgvdo.load("C:\\Users\\mudit\\OneDrive\\Desktop\\New folder\\Constellations.mp4")
    bgvdo.pack(expand=True,fill=BOTH)
    bgvdo.play()
    nxt_btn=Button(text='Next',font=('Consolas'),command=intro2,cursor='target')
    nxt_btn.place(x=650,y=380)
    window.mainloop()
    
def intro2():
    global window
    window.destroy()
    window=Tk()
    window.geometry('750x450')
    window.maxsize(750,450)
    window.title('Rookie Coders')
    intro2_bg=TkinterVideo(master=window,scaled=True)
    intro2_bg.load("C:\\Users\\mudit\\OneDrive\\Desktop\\New folder\\123.mp4")
    intro2_bg.pack(expand=True,fill=BOTH)
    intro2_bg.play()
    nxt_btn=Button(text='Next',font=('Consolas'),command=riddle1,cursor='target')
    nxt_btn.place(x=650,y=380)
    window.mainloop()

def riddle3():
    global window
    window.destroy()
    window=Tk()
    window.geometry('750x450')
    window.maxsize(750,450)
    window.title('Rookie Coders')

    head_lbl=Label(text='Choose the correct brick according to your journey till yet',font=('Harrington',16,'bold'),background='white')
    head_lbl.pack()

    r1_bg_img=PhotoImage(file="C:\\Users\\mudit\\OneDrive\\Desktop\\New folder\\Constellations (5).png")
    r1_bg=Label(image=r1_bg_img)
    r1_bg.pack()

    r1_op1_btn=Button(text='Push This Brick',cursor='target',background='DarkSalmon',command=death)
    r1_op1_btn.place(x=100,y=90)

    r1_op2_btn=Button(text='Push This Brick',cursor='target',background='DarkSalmon',command=death)
    r1_op2_btn.place(x=580,y=90)

    r1_op3_btn=Button(text='Push This Brick',cursor='target',background='DarkSalmon',command=riddle4())
    r1_op3_btn.place(x=360,y=90)

    window.mainloop()

def riddle2():
    global window
    window.destroy()
    window=Tk()
    window.geometry('750x450')
    window.maxsize(750,450)
    window.title('Rookie Coders')
    
    head_lbl=Label(text='Push the correct brick to open the secret door',font=('Harrington',18,'bold'),background='white')
    head_lbl.pack()

    r1_bg_img=PhotoImage(file="C:\\Users\\mudit\\OneDrive\\Desktop\\New folder\\Constellations (4).png")
    r1_bg=Label(image=r1_bg_img)
    r1_bg.pack()

    r1_op1_btn=Button(text='Push This Brick',cursor='target',background='DarkSalmon',command=riddle3)
    r1_op1_btn.place(x=200,y=90)

    r1_op2_btn=Button(text='Push This Brick',cursor='target',background='DarkSalmon',command=death)
    r1_op2_btn.place(x=580,y=90)

    r1_op3_btn=Button(text='Push This Brick',cursor='target',background='DarkSalmon',command=death)
    r1_op3_btn.place(x=360,y=90)
    window.mainloop()
def riddle1():  
    global window
    window.destroy()
    window=Tk()
    window.geometry('750x450')
    window.maxsize(750,450)
    window.title('Rookie Coders')

    head_lbl=Label(text='Choose a correct tile to step on..',font=('Harrington',18,'bold'),background='white')
    head_lbl.pack()

    r2_bg_img=PhotoImage(file="C:\\Users\mudit\\OneDrive\Desktop\\New folder\\Constellations (3).png")
    r1_bg=Label(image=r2_bg_img)
    r1_bg.pack()

    r1_op1_btn=Button(text='Step on this tile',cursor='target',background='DarkSalmon',command=death)
    r1_op1_btn.place(x=220,y=210)

    r1_op2_btn=Button(text='Step on this tile',cursor='target',background='DarkSalmon',command=death)
    r1_op2_btn.place(x=460,y=200)

    r1_op3_btn=Button(text='Step on this tile',cursor='target',background='DarkSalmon',command=riddle2)
    r1_op3_btn.place(x=343,y=360)
    # r1_op1_img=PhotoImage(file="C:\\Users\mudit\\OneDrive\\Desktop\\New folder\\chidiya.png")
    # r1_op1_btn=Button(cursor='target',image=r1_op1_img)
    # r1_op1_btn.place(x=250)
    window.mainloop()



# bgimg=PhotoImage(file='C:\\Users\\mudit\\OneDrive\\Desktop\\New folder\\Selgrow.png')
# bglbl=Label(image=bgimg)
# bglbl.pack()


pygame.mixer.music.load("C:\\Users\\mudit\\OneDrive\\Desktop\\New folder\\Middle East.mpeg")
pygame.mixer.music.play()


play_btn=Button(text='Play',font=('11'),width=50,command=game_start_intro1,cursor='target',background='DarkSalmon')
play_btn.place(x=130,y=300)

window.mainloop()

