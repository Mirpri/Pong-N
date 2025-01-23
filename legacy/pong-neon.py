from tkinter import *
from tkinter.ttk import*
import keyboard
import _thread
import time
import random
from subprocess import run

root = Tk()
root.title('pong neon by Mirpri')


#root.option_add('*background','#002255')
#root.option_add('*foreground','ivory')
#root.config(background='#002255')

p_name=['balanced','large','friction','swift','(test)']
p_width=[40,55,30,25,1000]
p_fric=[100,100,50,200,100]
p_speed=[9,8,8,12,0]
p_color=['gray','tan','darkseagreen','orchid','white']
p1t=p2t=0
def drawpad():    
    M.coords(p1p,(p1-p_width[p1t],700,p1+p_width[p1t],710))
    M.coords(p2p,(p2-p_width[p2t],90,p2+p_width[p2t],100))
    M.itemconfig(p1p,fill=p_color[p1t])
    M.itemconfig(p2p,fill=p_color[p2t])

def todrawpad(x):
    global p1t,p2t
    p1t=p_name.index(C1.get())
    p2t=p_name.index(C2.get())
    drawpad()

F1=Frame(root)
L1=Label(F1)
C1=Combobox(F1,values=p_name,width=8)
C1.set(p_name[0])
C1.bind("<<ComboboxSelected>>",todrawpad)
C1.pack(side='left')
L1.pack(side='left')
F2=Frame(root)
L2=Label(F2)
C2=Combobox(F2,values=p_name,width=8)
C2.set(p_name[0])
C2.bind("<<ComboboxSelected>>",todrawpad)
C2.pack(side='left')
L2.pack(side='left')

M=Canvas(root,height=800,width=600,bg='white')
F2.pack()
M.pack(padx=5)
F1.pack()

#keyboard.press_and_release('shift')

p1=300
p2=300
p1p=M.create_rectangle(0,0,0,0)
p2p=M.create_rectangle(0,0,0,0)
ball=M.create_oval(300-10,400-10,300+10,400+10,fill='red')
drawpad()

gaming=0
def match(ii=5):
    global gaming
    gaming=1
    s1=s2=0
    L1.config(text='  |  '+'⚫'*s1+'⚪'*(ii-s1))
    L2.config(text='  |  '+'⚫'*s2+'⚪'*(ii-s2))
    while gaming:
        win=game()
        if not gaming:
            break
        if win==1:
            s1+=1
        else:
            s2+=1
        L1.config(text='  |  '+'⚫'*s1+'⚪'*(ii-s1))
        L2.config(text='  |  '+'⚫'*s2+'⚪'*(ii-s2))
        if s1==ii or s2==ii:
            gaming=0     
    F3.pack(pady=5)      
    B1.config(state=NORMAL)
    C1.config(state=NORMAL)
    C2.config(state=NORMAL)
    return



def game():
    p1=300
    p2=300
    x,y=300,400
    a=0
    M.coords(ball,(x-10,y-10,x+10,y+10))
    drawpad()
    vx,vy=3*(2*random.randint(0,1)-1),4*(2*random.randint(0,1)-1)
    root.update()
    #keyboard.wait('space')
    while gaming:
        if keyboard.is_pressed('space'):
            break
        time.sleep(0.02)
    while gaming:
        s_t=time.time()
        v1,v2=0,0
        x_c,y_c=x,y
        vx+=a
        if keyboard.is_pressed('a') and p1>p_width[p1t]:
            p1-=p_speed[p1t]
            v1-=1
            M.move(p1p,-p_speed[p1t],0)
        if keyboard.is_pressed('d') and p1<600-p_width[p1t]:
            p1+=p_speed[p1t]
            v1+=1
            M.move(p1p,p_speed[p1t],0)
        if keyboard.is_pressed('4') and p2>p_width[p2t]:
            p2-=p_speed[p2t]
            v2-=1
            M.move(p2p,-p_speed[p2t],0)
        if keyboard.is_pressed('6') and p2<600-p_width[p2t]:
            p2+=p_speed[p2t]
            v2+=1
            M.move(p2p,p_speed[p2t],0)

        x,y=x+vx,y+vy
        if x<10:
            vx=-vx
            x=10
        elif x>590:
            vx=-vx
            x=590

        if 80<y<110 and abs(p2-x)<p_width[p2t]+10:
            if y<90 and abs(x-p2)>p_width[p2t]+5:
                if x>p2:
                    vx=abs(vx)
                else:
                    vx=-abs(vx)
                vy*=1.5
                vx*=1.5
                print('p2^')
            vy=-vy+1
            vx+=v2*p_speed[p2t]/4
            a=(v2*p_speed[p2t]-vx)/p_fric[p2t]
            y=110
        elif 720>y>690 and abs(p1-x)<p_width[p1t]+10:
            if y>710 and abs(x-p1)>p_width[p1t]+5:
                if x>p1:
                    vx=abs(vx)
                else:
                    vx=-abs(vx)
                vy*=1.5
                vx*=1.5
                print('p1^')
            vy=-vy-1
            vx+=v1*p_speed[p1t]/4
            a=(v1*p_speed[p1t]-vx)/p_fric[p1t]
            y=690
        M.move(ball,x-x_c,y-y_c)
        
        if vy>19:
            vy=19
            print(vy)
        elif vy<-19:
            vy=-19
            print(vy)
        if y<0:
            return 1
        elif y>800:
            return 2

        root.update()
        #print(0.02-time.time()+s_t)
        sleep_t=0.02-time.time()+s_t
        if sleep_t>0:
            time.sleep(sleep_t)
        else:
            print(sleep_t,'!')

started=False
def startmatch():
    global gaming,started
    if not started:       
        keyboard.press_and_release('shift')
        started=True
    if gaming:
        return
    C1.set(p_name[p1t])
    C2.set(p_name[p2t])
    F3.forget()
    B1.config(state=DISABLED)
    C1.config(state=DISABLED)
    C2.config(state=DISABLED)
    _thread.start_new_thread(match,())

def opengp():
    run("start GP.lnk", shell=True)

F3=Frame(root)
F3.pack(pady=5)
B1=Button(F3,text='Start',width=20,command=startmatch)
B1.pack(side='left')
B2=Button(F3,text='GP',command=opengp,width=3)
B2.pack()
#keyboard.is_pressed('a')
#_thread.start_new_thread(game,())

def forcestop(x):
    global gaming
    gaming=0

root.bind('<Escape>',forcestop)
root.mainloop()