from tkinter import * 
import tkinter as ttk
import datetime as datetime

Window = Tk()
Window.title('Loan Calculator form NEO!')
Window.geometry('600x400')
#Window.configure(background='light gray')
#Window.resizable(False, False) 

#photo = PhotoImage(file='iccalc.png')

#lblFrame = LabelFrame(Window, width=100, height=100, text='Loan', )
#lblFrame.place(x=113, y=11)
 
frm = LabelFrame(Window,text='Loan')
frm.pack(side=LEFT,ipadx=11,ipady=31)



#lbl88 = Label(Window, text='Hi NEO', background='red')
#lbl88.grid(row=0, column=9, padx=11,pady=3)

Loan = 4000
intRate = 24
Period = 12
LLoan = Loan
dT = datetime.datetime.now()

pmt = (Loan*intRate/100/12)/(1-(1+intRate/100/12)**-Period)
ipmt = Loan*intRate/100/12
ppmt = pmt-ipmt

smm=pmt*Period

label10 = Label(frm, text=f"{dT:%Y.%m.%d}")
label10.grid(column=1, padx=1,pady=3)

label11 = Label(frm, text=LLoan)
label11.grid(column=5,row=0, padx=1,pady=3)

for i in range(1,Period+1):
    label1 = Label(frm, text=i)
    label1.grid(row=i, column=0, padx=11,pady=3)

    label2 = Label(frm, text=f"{dT:%Y.%m.%d}")
    label2.grid(row=i, column=1, padx=1,pady=3)

    label3 = Label(frm, text=round(ipmt, 2))
    label3.grid(row=i, column=2, padx=11,pady=3)

    label4 = Label(frm, text=round(ppmt, 2))
    label4.grid(row=i, column=3, padx=1)   

    label5 = Label(frm, text=round(pmt, 2))
    label5.grid(row=i, column=4, padx=11) 

    label6 = Label(frm, text=round(Loan - ppmt, 2))
    label6.grid(row=i, column=5) 

    Loan = Loan - ppmt
    ipmt = Loan * intRate / 100 / 12
    ppmt = pmt - ipmt    

label7 = Label(frm, text=round(smm-LLoan, 2))
label7.grid(row=i+1, column=2, padx=11, pady=2)    

label8 = Label(frm, text=round(LLoan, 2))
label8.grid(row=i+1, column=3, padx=11, pady=2) 

label9 = Label(frm, text=round(smm, 2))
label9.grid(row=i+1, column=4, padx=11, pady=2)


    






Window.mainloop()