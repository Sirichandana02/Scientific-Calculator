
from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("GUI Sceintific Calculator")
#root.configure(background='red')
root.resizable(width=True, height=True)
root.geometry("440x760+500+10")
#root.geometry("440x688+500+10")
calc = Frame(root)
calc.grid()


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "modulus":
            self.total %= self.current
        if self.op == "pow":
            self.total=pow(self.total,self.current)
        if self.op == "lcm":
            self.maximum=max(self.total,self.current)
            while(True):
                if(self.maximum%self.total==0 and self.maximum%self.current==0):
                    self.total=self.maximum
                    break
                else:
                    self.maximum=self.maximum+1
        if self.op == "gcd":
            i=1
            while(i<=self.total and i<=self.current):
                if(self.total%i==0 and self.current%i==0):
                    self.gcd=i
                i=i+1
            self.total=self.gcd
        if self.op == "npr":
            fact = 1
            i = 1
            while i <= self.total:
                fact = i * fact
                i = i + 1

            self.numerator = fact  # n!
            self.sub = self.total - self.current  # (n-r)
            fact = 1
            i = 1
            while i <= self.sub:
                fact = i * fact
                i = i + 1
            self.denominator = fact  # (n-r)!
            self.perm = self.numerator / self.denominator
            self.total=self.perm
        if self.op ==  "ncr":
            fact=1
            i=1
            while i <= self.total:
                fact = i * fact
                i = i + 1
            self.numerator = fact  # n!
            self.sub = self.total - self.current  # (n-r)
            fact = 1
            i = 1
            while i <= self.sub:
                fact = i * fact
                i = i + 1
            self.denominator = fact #(n-r)!
            fact=1
            i=1
            while i<=self.current:
                fact=i*fact
                i=i+1
            self.denominator2=fact
            self.comb = self.numerator / (self.denominator2*self.denominator)
            self.total = self.comb



        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.total=float(self.total)
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False
    def backspace(self):
        numlen=len(txtDisplay.get())
        txtDisplay.delete(numlen-1,'end')
        if numlen == 1:
            txtDisplay.insert(0,"0")
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
    def inverse(self):
        self.result = False
        self.firstnum = (float(1))
        self.secondnum = (float(txtDisplay.get()))
        self.current = (self.firstnum / self.secondnum)
        self.display(self.current)
    def xsquare(self):
        self.result = False
        self.firstnum = (float(txtDisplay.get()))
        self.secondnum = (float(txtDisplay.get()))
        self.current = (self.firstnum * self.secondnum)
        self.display(self.current)
    def factorial(self):
        self.result=False
        self.firstnum = (int(txtDisplay.get()))
        self.f = 1
        for i in range(1, self.firstnum + 1):
            self.f = self.f * i
        self.current = (self.f)
        self.display(self.current)
    def sin(self):
        self.result=False
        self.firstnum=(float(txtDisplay.get()))
        self.result=math.sin(math.radians((self.firstnum)))
        self.current=self.result
        self.display(self.current)
    def cos(self):
        self.result=False
        self.firstnum=(float(txtDisplay.get()))
        self.result=math.cos(math.radians((self.firstnum)))
        self.current=self.result
        self.display(self.current)
    def tan(self):
        self.result=False
        self.firstnum=(float(txtDisplay.get()))
        self.result=math.tan(math.radians((self.firstnum)))
        self.current=self.result
        self.display(self.current)
    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)
    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def summation(self):
        self.result=False
        self.firstnum=(int(txtDisplay.get()))
        self.f=0
        for i in range(1,self.firstnum+1):
            self.f=self.f+i
        self.current=(self.f)
        self.display(self.current)
    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def e(self):
        self.result =  False
        self.current = math.e
        self.display(self.current)
    #def combination(self):




added_value = Calc()

txtDisplay = Entry(calc, font=('gainsboro', 20, 'bold'),
                   bg='black', fg='white',
                   bd=24, width=26, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []
for j in range(7,10):
    for k in range(3):
        btn.append(Button(calc, width=8, height=2,
                          bg='black', fg='white',
                          font=('gainsboro', 14 , 'bold'),
                          bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1
btnDel=Button(calc,text="",width=8,height=2,bg='gainsboro',font=('Helvetica',14,'bold'),bd=4,
                 command=added_value.backspace)
btnDel.grid(row=1,column=0)
btnClear = Button(calc, text=chr(67), width=8,
                  height=2, bg='sky blue',
                  font=('Helvetica', 14 , 'bold')
                  , bd=4, command=added_value.Clear_Entry
                  ).grid(row=1, column=1, pady=1)

btnAllClear = Button(calc, text=chr(67) + chr(69),
                     width=8, height=2,
                     bg='sky blue',
                     font=('Helvetica', 14, 'bold'),
                     bd=4,
                     command=added_value.All_Clear_Entry
                     ).grid(row=1, column=2, pady=1)
btnPM = Button(calc, text=chr(177), width=8,
               height=2, bg='gainsboro', font=('Helvetica', 14, 'bold'),
               bd=4, command=added_value.mathPM
               ).grid(row=1, column=3, pady=1)
btnsq = Button(calc, text="\u221A", width=8, height=2,
               bg='gainsboro', font=('Helvetica',
                                       14, 'bold'),
               bd=4, command=added_value.squared
               ).grid(row=2, column=0, pady=1)
btnx2=Button(calc,text="x^2",width=8,height=2,bg='gainsboro',
             font=('Helvetica',14,'bold'),bd=4,
                command=added_value.xsquare)
btnx2.grid(row=2,column=1)
btn1x=Button(calc,text="1/x",width=8,height=2,bg='gainsboro',
               font=('Helvetica',14,'bold'),
               bd=4, command=added_value.inverse)
btn1x.grid(row=2,column=2)
btnpi=Button(calc,text="π",width=8,height=2,bg='gainsboro',
               font=('Helvetica',14,'bold'),
               bd=4, command=added_value.pi)
btnpi.grid(row=2,column=3)


btnAdd = Button(calc, text="+", width=8, height=2,
                bg='gainsboro',
                font=('Helvetica', 14, 'bold'),
                bd=4, command=lambda: added_value.operation("add")
                ).grid(row=7, column=3, pady=1)

btnSub = Button(calc, text="-", width=8,
                height=2, bg='gainsboro',
                font=('Helvetica', 14, 'bold'),
                bd=4, command=lambda: added_value.operation("sub")
                ).grid(row=8, column=3, pady=1)

btnMul = Button(calc, text="*", width=8,
                height=2, bg='gainsboro',
                font=('Helvetica', 14, 'bold'),
                bd=4, command=lambda: added_value.operation("multi")
                ).grid(row=9, column=3, pady=1)

btnDiv = Button(calc, text="/", width=8,
                height=2, bg='gainsboro',
                font=('Helvetica', 14, 'bold'),
                bd=4, command=lambda: added_value.operation("divide")
                ).grid(row=10, column=3, pady=1)

btnZero = Button(calc, text="0", width=8,
                 height=2, bg='black', fg='white',
                 font=('Helvetica', 14, 'bold'),
                 bd=4, command=lambda: added_value.numberEnter(0)
                 ).grid(row=10, column=0, pady=1)

btnDot = Button(calc, text=".", width=8,
                height=2, bg='black',fg='white',
                font=('Helvetica', 14, 'bold'),
                bd=4, command=lambda: added_value.numberEnter(".")
                ).grid(row=10, column=1, pady=1)


btnEquals = Button(calc, text="=", width=8,
                   height=2, bg='sky blue',
                   font=('gainsboro', 14, 'bold'),
                   bd=4, command=added_value.sum_of_total
                   ).grid(row=10, column=2, pady=1)
btnfact = Button(calc, text="x!", width=8,
                   height=2, bg='gainsboro',
                   font=('gainsboro', 14, 'bold'),
                   bd=4, command=added_value.factorial
                   ).grid(row=3, column=0, pady=1)
btnMod = Button(calc, text="%", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica', 14, 'bold'),
                        bd=4, command=lambda: added_value.operation("modulus")
                        ).grid(row=3, column=2, pady=1)
btnsummation= Button(calc, text="Σx", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica', 14, 'bold'),
                        bd=4, command=lambda: added_value.summation()
                        ).grid(row=3, column=1, pady=1)
btnxpowery= Button(calc, text="x^y", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica', 14, 'bold'),
                        bd=4, command=lambda: added_value.operation("pow")
                        ).grid(row=3, column=3, pady=1)
btnxlcm= Button(calc, text="lcm", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica', 14, 'bold'),
                        bd=4, command=lambda: added_value.operation("lcm")
                        ).grid(row=4, column=0, pady=1)
btngcd= Button(calc, text="gcd", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica',14, 'bold'),
                        bd=4, command=lambda: added_value.operation("gcd")
                        ).grid(row=4, column=1, pady=1)
btnnpr= Button(calc, text="npr", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica',14, 'bold'),
                        bd=4, command=lambda: added_value.operation("npr")
                        ).grid(row=4, column=2, pady=1)
btnncr= Button(calc, text="ncr", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica',14, 'bold'),
                        bd=4, command=lambda: added_value.operation("ncr")
                        ).grid(row=4, column=3, pady=1)
btnsin= Button(calc, text="sin", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica',14, 'bold'),
                        bd=4, command=lambda: added_value.sin()
                        ).grid(row=5, column=0, pady=1)
btncos= Button(calc, text="cos", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica',14, 'bold'),
                        bd=4, command=lambda: added_value.cos()
                        ).grid(row=5, column=1, pady=1)
btntan= Button(calc, text="Tan", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica',14, 'bold'),
                        bd=4, command=lambda: added_value.tan()
                        ).grid(row=5, column=2, pady=1)
btnlog= Button(calc, text="ln", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica',14, 'bold'),
                        bd=4, command=lambda: added_value.log()
                        ).grid(row=5, column=3, pady=1)
btnsinh= Button(calc, text="sinh", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica',14, 'bold'),
                        bd=4, command=lambda: added_value.sinh()
                        ).grid(row=6, column=0, pady=1)
btncosh= Button(calc, text="cosh", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica',14, 'bold'),
                        bd=4, command=lambda: added_value.cosh()
                        ).grid(row=6, column=1, pady=1)
btntanh= Button(calc, text="tanh", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica',14, 'bold'),
                        bd=4, command=lambda: added_value.tanh()
                        ).grid(row=6, column=2, pady=1)
btne= Button(calc, text="e", width=8,
                        height=2, bg='gainsboro',
                        font=('Helvetica',14, 'bold'),
                        bd=4, command=lambda: added_value.e()
                        ).grid(row=6, column=3, pady=1)

root.mainloop()
