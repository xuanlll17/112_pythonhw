'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk         #查網站安裝pillow   
from tkinter.simpledialog import Dialog
import yfinance as yf
import csv

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("300x250")
        self.title("Images")  
        
class Getprice(Dialog):
    def body(self, master):
        price = tk.Frame(self)
        tk.Label(master, text='日期:').grid(row=0, sticky=tk.W)
        tk.Label(master, text='開盤價:').grid(row=1, sticky=tk.W)
        tk.Label(master, text='最高價:').grid(row=2, sticky=tk.W)
        tk.Label(master, text='最低價:').grid(row=3, sticky=tk.W)
        tk.Label(master, text='收盤價:').grid(row=4, sticky=tk.W)
        tk.Label(master, text='調整收盤價:').grid(row=5, sticky=tk.W)
        tk.Label(master, text='成交量:').grid(row=6, sticky=tk.W)
        self.DateVar = tk.StringVar()
        tk.Label(master,textvariable=self.DateVar).grid(column=1,row=0,sticky='W')
        self.OpenVar = tk.StringVar()
        tk.Label(master,textvariable=self.OpenVar).grid(column=1,row=1,sticky='W')
        self.HighVar = tk.StringVar()
        tk.Label(master,textvariable=self.HighVar).grid(column=1,row=2,sticky='W')
        self.LowVar = tk.StringVar()
        tk.Label(master,textvariable=self.LowVar).grid(column=1,row=3,sticky='W')
        self.CloseVar = tk.StringVar()
        tk.Label(master,textvariable=self.CloseVar).grid(column=1,row=4,sticky='W')
        self.Adj_CloseVar = tk.StringVar()
        tk.Label(master,textvariable=self.Adj_CloseVar).grid(column=1,row=5,sticky='W')
        self.VolumeVar = tk.StringVar()
        tk.Label(master,textvariable=self.VolumeVar).grid(column=1,row=6,sticky='W')
        #price = Getprice(self)
        


        self.oldpw = tk.Label(master, width=16,text="DateVar")
        self.newpw1 = tk.Label(master, width=16,text="OpenVar")
        self.newpw2 = tk.Label(master, width=16,text="HighVar")
        self.newpw3 = tk.Label(master, width=16,text="LowVar")
        self.newpw4 = tk.Label(master, width=16,text="CloseVar")
        self.newpw5 = tk.Label(master, width=16,text="Adj_CloseVar")
        self.newpw6 = tk.Label(master, width=16,text="VolumeVar")

        self.oldpw.grid(row=0, column=1, sticky=tk.W)
        self.newpw1.grid(row=1, column=1, sticky=tk.W)
        self.newpw2.grid(row=2, column=1, sticky=tk.W)
        self.newpw3.grid(row=3, column=1, sticky=tk.W)
        self.newpw4.grid(row=4, column=1, sticky=tk.W)
        self.newpw5.grid(row=5, column=1, sticky=tk.W)
        self.newpw6.grid(row=6, column=1, sticky=tk.W)
        return self.oldpw

        #def buttonbox(self):
           # '''add standard button box.

            #override if you do not want the standard buttons
            #'''

        #box = tk.Frame(self)

        #w = tk.Button(box, text="確認", width=10, command=self.ok, default=tk.ACTIVE)
        #w.pack(side=tk.LEFT, padx=5, pady=5)
        #w = tk.Button(box, text="取消", width=10, command=self.cancel)
        #w.pack(side=tk.LEFT, padx=5, pady=5)

        #self.bind("<Return>", self.ok)
        #self.bind("<Escape>", self.cancel)

        #box.pack()
        
       

class MyFrame(ttk.LabelFrame):
    def __init__(self,master,title,**kwargs):               
        super().__init__(master,text='股價查詢',**kwargs)        
        self.pack(expand=1,fill="both",padx=10,pady=10)

        self.tree = ttk.Treeview(self,columns=['#1','#2','#3','#4','#5','#6','#7'],show='headings')        
        self.tree.heading('#1',text='日期') 
        self.tree.heading('#2',text='開盤價')
        self.tree.heading('#3',text='最高價')
        self.tree.heading('#4',text='最低價') 
        self.tree.heading('#5',text='收盤價')
        self.tree.heading('#6',text='調整收盤價')
        self.tree.heading('#7',text='成交量')

   
        
        with open('台積電.csv', newline='') as csvfile:
            #reader
            price_reader = csv.reader(csvfile)
            next(price_reader)
            for row in price_reader:
                date = row[0]
                open_v = row[1]
                high = row[2]
                low = row[3]
                close = row[4]
                adj_close = row[5]
                value = row[6]
                self.tree.insert('',tk.END,value=(date,open_v,high,low,close,adj_close,value))

            #DictReader
            #price_reader = csv.DictReader(csvfile)
            #for row in price_reader:
            #    date = row['Date']
            #    open_v = row['Open']
            #    high = row['High']
            #    low = row['Low']
            #    close = row['Close']
            #    adj_close = row['Adj Close']
            #    value = row['Volume']
            #    self.tree.insert('',tk.END,value=(date,open_v,high,low,close,adj_close,value))
            

        self.tree.pack()    

        self.tree.bind('<<TreeviewSelect>>',self.item_selected)  

    def item_selected(self,event):
        item_id = self.tree.selection()[0]
        item_dict = self.tree.item(item_id)
        print(item_dict['values'])
        price= Getprice(self)        
       

    def choised(self):
        print(self.aligement.get())


def main():    
    window = Window()
    myFrame = MyFrame(window,"對齊方式")    
    window.mainloop()


if __name__ == "__main__":
    main()