import tkinter
from tkinter.ttk import *
from tkinter import *  
import random
from tkinter import messagebox

answers = [
    "tulip",
    "daisy",
    "iris",
    "marigold",
    "lotus",
    "lilac",
    "aster",
    "lily",
    "daffodil",
    "dahlia",
    "bougainvillea",
    "jasmine",
    "lavender",
    "orchid",
    "rose",
    "hibiscus",
    "sunflower",
    "tuberose",
    "zinnia",
    "periwinkle",
    "pansy",
    "poppy",
    "cosmos",
    "snowdrop",
    "cornflower",
    ]

words = [
    "ltuip",  
    "dsyia", 
    "rsii",
    "grdoalmi",
    "sotlu",
    "alcli",
    "satre",
    "lyil",
    "fiolfdad",
    "ahaidl",
    "anolibevaiugl",
    "insamje",
    "anleervd",
    "odcirh",
    "soer",
    "ibshucsi",
    "efosnluwr",
    "ouretseb",
    "nainzi",
    "iwikpneelr",
    "nsapy",
    "pypop",
    "ssoomc",
    "dpnowors",
    "floorncrew",
]

num = random.randrange(0,25,1)

s = 0




def res():
    global words,answers,num
    num = random.randrange(0,25,1)
    lbl.config(text=words[num])
    e1.delete(0,END)


def score() :
    global s
    lb3.config(text=s)





def default():
    global words,answers,num
    lbl.config(text = words[num])


def checkans():
    global words,answers,num,s
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("SUCCESS","This is a correct answer!!")
        s = s +1
        score()
        res()
    else:
        messagebox.showerror("ERROR","This is not correct!!")
        e1.delete(0,END)
        ExitApplication()
        


def ExitApplication():
    global words,num,s
    MsgBox = messagebox.askquestion ('Exit Application',' Play Again')
    if MsgBox == 'no':
       root.destroy()
    else:
        messagebox.showinfo('Return','You will now return to the application screen')
        s=0
        lb3.config(text=s)
        num = random.randrange(0,25,1)
        lbl.config(text = words[num])

        
        



root = tkinter.Tk()
root.geometry("350x400")
root.title("Jumbbled")
root.configure(background="#4BCFFA")




lb2 = Label(
    root,
    text = "Your Score :",
    font = ("Constantia", 20),
    bg = "#4BCFFA",
    fg ="#192A56",
)
lb2.pack(pady = 10)




lb3 = Label(
    root,
    text = "0",
    font = ("Constantia", 25),
    bg = "#4BCFFA",
    fg ="#192A56",
)
lb3.pack(pady = 10)



lbl = Label(
    root,
    text = "Your are here",
    font = ("Comic Sans MS", 18),
    bg = "#4BCFFA",
    fg = "#D63031",
)
lbl.pack(pady = 30)



ans1 = StringVar()
e1 = Entry(
    root,
    font = ("Comic Sans MS" , 16),
    textvariable = ans1,
    bg = "white",
    fg = "#BB2CD9",
)
e1.pack()


btncheck = Button(
    root,
    text = "Check",
    width = 16,
    bg = "#DAE0E2",
    fg = "#019031",
    relief = GROOVE,
    command = checkans,
)
btncheck.pack(pady = 40)


btnreset = Button(
    root,
    text = "Reset",
    width = 16,
    bg = "#DAE0E2",
    fg = "#3C40C6",
    relief = GROOVE,
    command = res,
)
btnreset.pack(pady = 5)




button1 = Button (root, text='Exit Application',command=ExitApplication,bg='#DAE0E2',fg='white') 


default()

root.mainloop()

