from tkinter import *

class Calculadora:

    azulbb = '#6495ED'
    preto = '#000000'

    def __init__(self):
        self.root = root
        self.textoent = ""
        self.configura_tela()
        self.botoes()
        self.entry()
        root.mainloop()


    def configura_tela(self):
        self.root.configure(bg='#000')
        self.root.geometry("400x600")
        self.root.title("Calculadora ")
        self.root.resizable(True, True)
        self.root.minsize(width = 300, height = 500)
        self.root.maxsize(width = 800, height = 800)
        self.root.iconbitmap('icone.ico')


    def entry(self):
        global frame1
        frame1 = StringVar()
        self.frame1 = Entry(self.root, bg = '#fff', font = ("popins", 45),state = 'readonly', textvariable = frame1, bd = 4)
        self.frame1.place(relx=0.05, rely=0.05, relheight=0.2, relwidth=0.86)
        frame1.set(0)




    def botoes(self):
        self.botao1 = Button(self.root, bg = "#fff", text = ("1"), font = ('popins', 30), activebackground = self.azulbb, highlightbackground = self.azulbb, highlightthickness = 3,command = lambda:self.botao_funciona(1), bd = 4)
        self.botao1.place(relx=0.05, rely=0.4, relheight=0.09, relwidth=0.2)

        self.botao2 = Button(self.root,bg = '#fff', text = ('2'), font = ('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona(2), bd = 4 )
        self.botao2.place(relx=0.27, rely=0.4, relheight=0.09, relwidth=0.2)

        self.botao3 = Button(self.root, bg='#fff', text=('3'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona(3), bd = 4 )
        self.botao3.place(relx=0.49, rely=0.4, relheight=0.09, relwidth=0.2)

        self.botao4 = Button(self.root, bg='#fff', text=('4'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona(4), bd = 4 )
        self.botao4.place(relx=0.71, rely=0.4, relheight=0.09, relwidth=0.2)

        self.botao5 = Button(self.root, bg='#fff', text=('5'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona(5), bd = 4 )
        self.botao5.place(relx=0.05, rely=0.5, relheight=0.09, relwidth=0.2)

        self.botao7 = Button(self.root, bg='#fff', text=('7'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona(7), bd = 4 )
        self.botao7.place(relx=0.49, rely=0.5, relheight=0.09, relwidth=0.2)

        self.botao6 = Button(self.root, bg='#fff', text=('6'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona(6), bd = 4 )
        self.botao6.place(relx=0.27, rely=0.5, relheight=0.09, relwidth=0.2)

        self.botao8 = Button(self.root, bg='#fff', text=('8'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona(8), bd = 4 )
        self.botao8.place(relx=0.71, rely=0.5, relheight=0.09, relwidth=0.2)

        self.botao9 = Button(self.root, bg='#fff', text=('9'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona(9), bd = 4 )
        self.botao9.place(relx=0.05, rely=0.6, relheight=0.09, relwidth=0.2)

        self.botao0 = Button(self.root, bg='#fff', text=('0'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona(0), bd = 4 )
        self.botao0.place(relx=0.27, rely=0.6, relheight=0.09, relwidth=0.2)

        self.botao_mais = Button(self.root, bg='#fff', text=('+'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona('+'), bd = 4 )
        self.botao_mais.place(relx=0.49, rely=0.6, relheight=0.09, relwidth=0.2)

        self.botao_menos = Button(self.root, bg='#fff', text=('-'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona('-'), bd = 4 )
        self.botao_menos.place(relx=0.71, rely=0.6, relheight=0.09, relwidth=0.2)

        self.botao_vs = Button(self.root, bg='#fff', text=('X'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona("*"), bd = 4 )
        self.botao_vs.place(relx=0.05, rely=0.7, relheight=0.09, relwidth=0.2)

        self.botao_div = Button(self.root, bg='#fff', text=('/'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona('/'), bd = 4 )
        self.botao_div.place(relx=0.27, rely=0.7, relheight=0.09, relwidth=0.2)

        self.botao_por = Button(self.root, bg='#fff', text=('%'), font=('popins', 30), activebackground = self.azulbb, command = lambda:self.botao_funciona('%'), bd = 4 )
        self.botao_por.place(relx=0.49, rely=0.7, relheight=0.09, relwidth=0.2)

        self.botao_go = Button(self.root, bg='blue', text=('='), font=('popins', 30), activebackground = 'blue', command = lambda:self.igual(), bd = 4 )
        self.botao_go.place(relx=0.71, rely=0.7, relheight=0.09, relwidth=0.2)

        self.botao_apaga = Button(self.root, bg='blue', text=('C'), font=('popins', 30), activebackground='blue',command=lambda: self.apaga(), bd = 4 )
        self.botao_apaga.place(relx=0.05, rely=0.3, relheight=0.09, relwidth=0.86)

        self.botao_apaga = Button(self.root, bg='white', text=('.'), font=('popins', 30), activebackground='blue', command=lambda: self.botao_funciona('.'), bd=4)
        self.botao_apaga.place(relx=0.05, rely=0.8, relheight=0.09, relwidth=0.42)

        self.bot = Button(self.root, bg='white', text=('DEV Nicolino XD'), font=('popins', 15))
        self.bot.place(relx=0.49, rely=0.8, relheight=0.09, relwidth=0.42)


    def apaga(self):
        self.textoent = "0"
        frame1.set(0)


    def botao_funciona(self, n):
        if self.textoent == "":
            self.textoent = self.frame1.get()
        else:
            self.textoent = self.textoent

        if self.textoent == "0" and n == 0:
            pass
        elif self.textoent == "0":
            self.textoent = ""
        self.frame1.delete(0, END)
        self.frame1.insert(END, self.textoent + str(n))
        self.textoent = self.textoent + str(n)
        frame1.set(self.textoent)


    def igual(self):
        try:
            self.textoent = frame1.get()
            self.textoent = str(eval(self.textoent))
            frame1.set(self.textoent)
        except SyntaxError:
            frame1.set("Erro")
            self.apaga()
        except ZeroDivisionError:
            frame1.set("Erro divisão por 0")
            self.apaga()


root = Tk()
Calculadora()

