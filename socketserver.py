# -*- coding:utf-8 -*-
from Tkinter import *
import socket
import time
from threading import *

global client_sock2,client_sock1
ip='127.0.0.1'
port=20000
client_sock1=''
client_sock2=''
name1=''
name2=''
class subApp:
    def __init__(self,Master):
        self.master=Master
        Master.title("서버 구축")
        Master.geometry("220x100")
        self.submainFrame=Frame(self.master)
        self.submainFrame.pack(fill=X)
        self.label1 = Label(self.submainFrame, text="서버 열기")
        self.label1.pack(side=TOP)

        self.submainFrame1 = Frame(self.master)
        self.submainFrame1.pack(fill=X)
        self.submainFrame2 = Frame(self.master)
        self.submainFrame2.pack(fill=X)
        self.submainFrame3 = Frame(self.master)
        self.submainFrame3.pack(fill=X)

        self.label1 = Label(self.submainFrame1, text="server ip")
        self.label1.pack(side=LEFT)
        self.entry1 = Entry(self.submainFrame1, bd=1, width=10)
        self.entry1.pack(side=LEFT)
        self.label2 = Label(self.submainFrame2, text="server port")
        self.label2.pack(side=LEFT)
        self.entry2 = Entry(self.submainFrame2, bd=1, width=5)
        self.entry2.pack(side=LEFT)
        self.button=Button(self.submainFrame3,text="연결",width=10,height=2,command=self.openserver)
        self.button.pack(side=TOP)

    def openserver(self):
        global ip,port
        ip = self.entry1.get()
        port = int(self.entry2.get())
        self.master.quit()
        self.master.destroy()
root=Tk()
app=subApp(root)
root.mainloop()
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(ip,port)
server_sock.bind((ip, port))
server_sock.listen(2)
count = 0
connection=0

def socket1():
    global client1,addr1,name1,count,connection
    count+=1
    client1, addr1 = server_sock.accept()
    print("[알림] :"+str(addr1[1])+" 연결")
    connection+=1
    name1=client1.recv(65535)
    sendmessage("[System]", name1+"님이 입장하셨습니다. ")
    while True:
        data1 = client1.recv(65535)
        if data1:
            print(data1)
            sendmessage(name1,data1)
    count-=1
    connection-=1
    client1.close()

def socket2():
    global client2, addr2, name2, count, connection
    count += 2
    client2, addr2 = server_sock.accept()
    print("[알림] :" + str(addr2[1]) + " 연결")
    connection += 2
    name2 = client2.recv(65535)
    sendmessage("[System]", name2 + "님이 입장하셨습니다. ")
    # client_sock2.send(("[알림]",name1," joined!").encode("utf-8","ignore"))
    while True:
        data2 = client2.recv(65535)
        if data2:
            print(data2)
            sendmessage(name2,data2)
    count -= 2
    connection -= 2
    client.close()

def sendmessage(name,data):
    message=name+" : "+data
    print(message)
    if connection==1:
        client1.send(message)
    if connection==2:
        client2.send(message)
    if connection == 3:
        client1.send(message)
        client2.send(message)
sock1=Thread(target=socket1)
sock2=Thread(target=socket2)
sock1.start()
sock2.start()