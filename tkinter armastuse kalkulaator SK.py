from tkinter import *

def calculation():
    s1=entry1.get().lower().replace(" ","")
    s2=entry2.get().lower().replace(" ","")
    s=s1+"Loves"+s2
    s1=""
    l=""
    
    for i in s:
        if i not in s1:
            l+=str(s.count(i))
            s1+=i
    
    
            
    while len(l)!=2:
        s1=l
        l=""
        
        for i in range(len(s1)//2):
            l+=str(int(s1[i])+int(s1[-(i+1)]))
            
        if len(s1)%2!=0:
            l+=str(s1[len(s1)//2])
            
    entry3.insert(END,1)
    
def clear():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

    entry1.focus_set()

if __name__=="__main__":
    gui=Tk()
    gui.title("Love Calculator")
    gui.configure(background="red")
    gui.geometry("300x300")
    
    label1=Label(gui,text="First name",fg="white",bg="black",font="Times")
    label1.grid(row=0,column=0)
    entry1=Entry(gui)
    entry1.grid(row=0,column=1)
    
    label2=Label(gui,text="Second name",fg="white",bg="black",font="Times")
    label2.grid(row=1,column=0)
    entry2=Entry(gui)
    entry2.grid(row=1,column=1)
    
    label3=Label(gui,text="Love Precentage",fg="white",bg="black",font="Times")
    label3.grid(row=3,column=0)
    entry3=Entry(gui)
    entry3.grid(row=3,column=1)
    
    button1=Button(gui,text="Calculate",bg="white",command=calculation)
    button1.grid(row=2,column=1)
    
    button2=Button(gui,text="Clear",bg="white",command=clear)
    button2.grid(row=5,column=1)
    
    
    gui.mainloop()