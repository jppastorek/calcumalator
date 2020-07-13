import tkinter as tk

window = tk.Tk()

#title
title = tk.Label(text='Calcumalator')
title.grid(row=0, column=1)

#entry declaration
entry = tk.Entry()
entry.grid(row=1, column=1)

#variables for calculation
firstnum = 0
secondnum = 0
first = True
answer = 0
add = False
subtract = False
multiply = False
divide = False


#button commands
def one():
    entry.delete(0, tk.END)
    if first:
        global firstnum
        firstnum = (firstnum*10)+1
        entry.insert(0, firstnum)
    else:
        global secondnum
        secondnum = (secondnum*10)+1
        entry.insert(0, secondnum)

def two():
    entry.delete(0, tk.END)
    if first:
        global firstnum
        firstnum = (firstnum*10)+2
        entry.insert(0, firstnum)
    else:
        global secondnum
        secondnum = (secondnum*10)+2
        entry.insert(0, secondnum)

def three():
    entry.delete(0, tk.END)
    if first:
        global firstnum
        firstnum = (firstnum*10)+3
        entry.insert(0, firstnum)
    else:
        global secondnum
        secondnum = (secondnum*10)+3
        entry.insert(0, secondnum)

def four():
    entry.delete(0, tk.END)
    if first:
        global firstnum
        firstnum = (firstnum*10)+4
        entry.insert(0, firstnum)
    else:
        global secondnum
        secondnum = (secondnum*10)+4
        entry.insert(0, secondnum)

def five():
    entry.delete(0, tk.END)
    if first:
        global firstnum
        firstnum = (firstnum*10)+5
        entry.insert(0, firstnum)
    else:
        global secondnum
        secondnum = (secondnum*10)+5
        entry.insert(0, secondnum)

def six():
    entry.delete(0, tk.END)
    if first:
        global firstnum
        firstnum = (firstnum*10)+6
        entry.insert(0, firstnum)
    else:
        global secondnum
        secondnum = (secondnum*10)+6
        entry.insert(0, secondnum)

def seven():
    entry.delete(0, tk.END)
    if first:
        global firstnum
        firstnum = (firstnum*10)+7
        entry.insert(0, firstnum)
    else:
        global secondnum
        secondnum = (secondnum*10)+7
        entry.insert(0, secondnum)

def eight():
    entry.delete(0, tk.END)
    if first:
        global firstnum
        firstnum = (firstnum*10)+8
        entry.insert(0, firstnum)
    else:
        global secondnum
        secondnum = (secondnum*10)+8
        entry.insert(0, secondnum)

def nine():
    entry.delete(0, tk.END)
    if first:
        global firstnum
        firstnum = (firstnum*10)+9
        entry.insert(0, firstnum)
    else:
        global secondnum
        secondnum = (secondnum*10)+9
        entry.insert(0, secondnum)

def clearOperand():
    add = False
    subtract = False
    multiply = False
    divide = False

def add():
    global add
    global subtract
    global multiply
    global divide
    clearOperand()
    add = True
    #entry.delete(0, tk.END)
    global first
    first = False

def subtract():
    global add
    global subtract
    global multiply
    global divide
    clearOperand()
    subtract = True
    #entry.delete(0, tk.END)
    global first
    first = False

def multiply():
    global add
    global subtract
    global multiply
    global divide
    clearOperand()
    multiply = True
    #entry.delete(0, tk.END)
    global first
    first = False

def divide():
    global add
    global subtract
    global multiply
    global divide
    clearOperand()
    divide = True
    #entry.delete(0, tk.END)
    global first
    first = False

def decimal():
    entry.delete(0, tk.END)
    global firstnum




def solve():
    global answer
    global add
    global subtract
    global multiply
    global divide
    global firstnum
    global secondnum
    global first
    if add:
        answer = firstnum + secondnum
    elif subtract:
        answer = firstnum - secondnum
    elif multiply:
        answer = firstnum * secondnum
    else:
        answer = firstnum / secondnum
    entry.delete(0, tk.END)
    entry.insert(0, answer)
    firstnum = answer
    secondnum = 0
    first = True
    clearOperand()


def clear():
    global firstnum
    firstnum = 0
    global secondnum
    secondnum = 0
    entry.delete(0, tk.END)
    global first
    first = True
    global add
    global subtract
    global multiply
    global divide
    clearOperand()




#-------------------------LAYOUT-----------------------------------------

#button declarations
btn1 = tk.Button(text='1',fg='white',bg='black',command=one)
btn2 = tk.Button(text='2',fg='white',bg='black',command=two)
btn3 = tk.Button(text='3',fg='white',bg='black',command=three)
btn4 = tk.Button(text='4',fg='white',bg='black',command=four)
btn5 = tk.Button(text='5',fg='white',bg='black',command=five)
btn6 = tk.Button(text='6',fg='white',bg='black',command=six)
btn7 = tk.Button(text='7',fg='white',bg='black',command=seven)
btn8 = tk.Button(text='8',fg='white',bg='black',command=eight)
btn9 = tk.Button(text='9',fg='white',bg='black',command=nine)
btnplus = tk.Button(text='+',fg='white',bg='black',command=add)
btnminus = tk.Button(text='-',fg='white',bg='black',command=subtract)
btntimes = tk.Button(text='*',fg='white',bg='black',command=multiply)
btndivide = tk.Button(text='/',fg='white',bg='black',command=divide)
btndecimal = tk.Button(text='.',fg='white',bg='black',command=decimal)
btnequals = tk.Button(text='=',fg='white',bg='black',command=solve)
btnclear = tk.Button(text='C',fg='white',bg='black',command=clear)


#buttons 123
btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)
#buttons 456
btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
#buttons 789
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
#buttons +-*/C
btnplus.grid(row=2, column=3)
btnminus.grid(row=3, column=3)
btntimes.grid(row=4, column=3)
btndivide.grid(row=5, column=3)
btnequals.grid(row=6, column=3)
btnclear.grid(row=7, column=3)







window.mainloop()
