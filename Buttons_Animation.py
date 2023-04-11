from tkinter import *
import time


win=Tk()
win.title("Jhanvi's App") 

X1=180
Y1=10
X2=270
Y2=100
X3=170
Y3=200
X4=70
Y4=100
M1x=1
M1y=1
M2x=1
M2y=1
M3x=1
M3y=1
M4x=1
M4y=1
click=0
count=0
def swap():
  global X1,Y1,M1x,M1y,X2,Y2,X3,Y3,X4,Y4
  global M2x,M2y,M3x,M3y,M4x,M4y,count
  if(count==0):
    X1=X1+M1x
    Y1=Y1+M1y
  
    B1.place(x=X1,y=Y1)
    B2.place(x=X2,y=Y2)
    B3.place(x=X3,y=Y3)
    B4.place(x=X4,y=Y4)
    
    if(Y1==100):
      M1x=0
      M1y=0
      X2=X2-M2x
      Y2=Y2+M2y
    if(Y2==200):
      M2x=0
      M2y=0
      X3=X3-M3x
      Y3=Y3-M3y
    if(Y3==100):
      M3x=0
      M3y=0
      X4=X4+M4x
      Y4=Y4-M4y
    if(Y4==10):
      M4x=0
      M4y=0
      count=count+1
      M1x=M1y=M2x=M2y=M3x=M3y=M4x=M4y=1
      
      return False
  if(count==1):
    X1=X1-M1x
    Y1=Y1+M1y
  
    B1.place(x=X1,y=Y1)
    B2.place(x=X2,y=Y2)
    B3.place(x=X3,y=Y3)
    B4.place(x=X4,y=Y4)
    if(Y1==200):
      M1x=0
      M1y=0
      X2=X2-M2x
      Y2=Y2-M2y
    if(Y2==100):
      M2x=0
      M2y=0
      X3=X3+M3x
      Y3=Y3-M3y
    if(Y3==10):
      M3x=0
      M3y=0
      X4=X4+M4x
      Y4=Y4+M4y
    if(Y4==100):
      M4x=0
      M4y=0
      count=count+1
      M1x=M1y=M2x=M2y=M3x=M3y=M4x=M4y=1
      return False 
  
  if(count==2):
    X1=X1-M1x
    Y1=Y1-M1y
  
    B1.place(x=X1,y=Y1)
    B2.place(x=X2,y=Y2)
    B3.place(x=X3,y=Y3)
    B4.place(x=X4,y=Y4)
    if(Y1==100):
      M1x=0
      M1y=0
      X2=X2+M2x
      Y2=Y2-M2y
    if(Y2==10):
      M2x=0
      M2y=0
      X3=X3+M3x
      Y3=Y3+M3y
    if(Y3==100):
      M3x=0
      M3y=0
      X4=X4-M4x
      Y4=Y4+M4y
    if(Y4==200):
      M4x=0
      M4y=0
      count=count+1
      M1x=M1y=M2x=M2y=M3x=M3y=M4x=M4y=1
      return False
  if(count==3):
    X1=X1+M1x
    Y1=Y1-M1y
  
    B1.place(x=X1,y=Y1)
    B2.place(x=X2,y=Y2)
    B3.place(x=X3,y=Y3)
    B4.place(x=X4,y=Y4)
    if(Y1==10):
      M1x=0
      M1y=0
      X2=X2+M2x
      Y2=Y2+M2y
    if(Y2==100):
      M2x=0
      M2y=0
      X3=X3-M3x
      Y3=Y3+M3y
    if(Y3==200):
      M3x=0
      M3y=0
      X4=X4-M4x
      Y4=Y4-M4y
    if(Y4==100):
      M4x=0
      M4y=0
      count=count+1
      M1x=M1y=M2x=M2y=M3x=M3y=M4x=M4y=1
      count=0
      return False  
  win.after(10,swap)
  
B1=Button(win,text="button 1")
B1.place(x=180,y=10)
B2=Button(win,text="button 2")
B2.place(x=270,y=100)
B3=Button(win,text="button 3")
B3.place(x=170,y=200)
B4=Button(win,text="button 4")
B4.place(x=70,y=100)
SwapB=Button(win,text="swap",command=swap) 
SwapB.place(x=200,y=250)
win.mainloop()

