# -*- coding:utf-8 -*-
from Tkinter import *
import socket
import time
from threading import *

ip = "127.0.0.1"
port = 30000
username = ""
global f
f = True


class mainApp:
    def __init__(self, Master):
        self.master = Master
        Master.geometry("410x600")
        self.mainFrame = Frame(self.master)
        self.mainFrame.pack(fill=X)

        self.frame1 = Frame(self.mainFrame)
        self.frame1.pack(fill=X)

        self.text = Text(self.frame1)
        self.scroll1 = Scrollbar(self.frame1)
        self.scroll1.pack(side=RIGHT, fill=Y)
        self.text.config(width=56, height=38, state='disabled', yscrollcommand=self.scroll1.set)

        self.text.pack(side=LEFT, fill=BOTH, expand=YES)
        self.scroll1.config(command=self.text.yview)

        self.frame2 = Frame(self.mainFrame)
        self.frame2.pack(fill=X)

        self.label1 = Label(self.frame2, text="my name")
        self.label1.pack(side=LEFT)
        self.entryname = Entry(self.frame2, bd=1, width=10)
        self.entryname.pack(side=LEFT)
        self.sendbutton = Button(self.frame2, text="Send", width=6, height=1, command=self.sendmessage)
        self.sendbutton.pack(side=LEFT)

        self.frame3 = Frame(self.mainFrame, padx=2, pady=1)
        self.frame3.pack(fill=X)
        self.textentry = Text(self.frame3, width=48, height=4)
        self.textentry.pack(side=LEFT)
        self.sendbutton = Button(self.frame3, text="Send", width=6, height=3, command=self.sendmessage)
        self.sendbutton.pack(side=LEFT)
        self.textentry.pack(side=LEFT)
        self.sendbutton.bind("<Return>", self.buttonclick_sub)
        self.textentry.bind("<KeyRelease-Return>", self.buttonclick_sub)

    def textrefresh(self, message):
        self.text.config(state="normal")
        self.text.insert(END, "\n" + message)

        self.text.config(state="disabled")

    def buttonclick_sub(self):
        self.sendmessage()

    def sendmessage(self):
        global f
        if f:
            message = self.entryname.get()
            f = False
        else:
            message = self.textentry.get(1.0, END)

        sock.send(message.encode('utf-8'))
        self.textentry.delete(1.0, END)


class subApp:
    def __init__(self, Master):
        self.master = Master
        Master.title("서버 연결")
        Master.geometry("220x100")
        self.submainFrame = Frame(self.master)
        self.submainFrame.pack(fill=X)
        self.label1 = Label(self.submainFrame, text="서버 연결")
        self.label1.pack(side=TOP)

        self.submainFrame1 = Frame(self.master)
        self.submainFrame1.pack(fill=X)
        self.submainFrame2 = Frame(self.master)
        self.submainFrame2.pack(fill=X)
        self.submainFrame3 = Frame(self.master)
        self.submainFrame3.pack(fill=X)
        self.submainFrame4 = Frame(self.master)
        self.submainFrame4.pack(fill=X)
        self.label1 = Label(self.submainFrame1, text="server ip")
        self.label1.pack(side=LEFT)
        self.entry1 = Entry(self.submainFrame1, bd=1, width=10)
        self.entry1.pack(side=LEFT)
        self.label2 = Label(self.submainFrame2, text="server port")
        self.label2.pack(side=LEFT)
        self.entry2 = Entry(self.submainFrame2, bd=1, width=5)
        self.entry2.pack(side=LEFT)
        ''' self.label3 = Label(self.submainFrame3, text="user name")
        self.label3.pack(side=LEFT)
        self.entry3 = Entry(self.submainFrame3, bd=1, width=5)
        self.entry3.pack(side=LEFT)'''

        self.button = Button(self.submainFrame4, text="연결", width=10, height=2, command=self.connectserver)
        self.button.pack(side=TOP)

    def connectserver(self):
        global ip, port, username
        ip = self.entry1.get()
        port = int(self.entry2.get())
        #username = self.entry3.get()

        self.master.quit()
        self.master.destroy()


def chatting():
    root.mainloop()


def connect():
    print(ip)
    sock.connect((ip, port))

    while True:
        data = sock.recv(65535)
        if data:
            app2.textrefresh(data)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
root2 = Tk()
app2 = subApp(root2)
root2.mainloop()
root = Tk()
app2 = mainApp(root)

th1 = Thread(target=chatting)
th2 = Thread(target=connect)
th1.start()
th2.start()

