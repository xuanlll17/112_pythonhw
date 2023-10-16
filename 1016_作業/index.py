'''
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import Dialog
import csv
import yfinance

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("台積電股價")

class GetdataInfo(Dialog):

    def body(self, master):
        self.title("查看詳情")

        tk.Label(master, text='Date:').grid(row=0, sticky=tk.W)
        tk.Label(master, text='Open:').grid(row=1, sticky=tk.W)
        tk.Label(master, text='High:').grid(row=2, sticky=tk.W)
        tk.Label(master, text='Low:').grid(row=3, sticky=tk.W)
        tk.Label(master, text='Close:').grid(row=4, sticky=tk.W)
        tk.Label(master, text='AdjClose:').grid(row=5, sticky=tk.W)
        tk.Label(master, text='Volume:').grid(row=6, sticky=tk.W)
        self.Datevar = tk.StringVar()
        tk.Label(master, textvariable=self.Datevar).grid(column=1, row=0, sticky=tk.E)
        self.Openvar = tk.StringVar()
        tk.Label(master, textvariable=self.Openvar).grid(column=1, row=1, sticky=tk.E)
        self.Highvar = tk.StringVar()
        tk.Label(master, textvariable=self.Highvar).grid(column=1, row=2, sticky=tk.E)
        self.Lowvar = tk.StringVar()
        tk.Label(master, textvariable=self.Lowvar).grid(column=1, row=3, sticky=tk.E)
        self.Closevar = tk.StringVar()
        tk.Label(master, textvariable=self.Closevar).grid(column=1, row=4, sticky=tk.E)
        self.AdjClosevar = tk.StringVar()
        tk.Label(master, textvariable=self.AdjClosevar).grid(column=1, row=5, sticky=tk.E)
        self.Volumevar = tk.StringVar()
        tk.Label(master, textvariable=self.Volumevar).grid(column=1, row=6, sticky=tk.E)


       
    
    def buttonbox(self):
        '''add standard button box.

        override if you do not want the standard buttons
        '''

        box = tk.Frame(self)

        w = tk.Button(box, text="確認", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="取消", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)

        self.tree = ttk.Treeview(self,columns=['#1', '#2', '#3', '#4', '#5', '#6', '#7'],show="headings")
        self.tree.heading('#1', text="Date")
        self.tree.heading('#2', text="Open")
        self.tree.heading('#3', text="High")
        self.tree.heading('#4', text="Low")
        self.tree.heading('#5', text="Close")
        self.tree.heading('#6', text="AdjClose")
        self.tree.heading('#7', text="Volume")
        
        self.scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.tree.yview)
        
        self.scrollbar.pack(side='right',fill='y')
        self.pack(expand=1,fill='both',padx=10,pady=10)
        
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        with open('台積電.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Date = row['Date']
                Open = row['Open']
                High = row['High']
                Low = row['Low']
                Close = row['Close']
                AdjClose = row['Adj Close']
                Volume = row['Volume']
                self.tree.insert('',tk.END,value=(Date, Open, High, Low, Close, AdjClose, Volume))
        
        self.tree.pack()

        self.tree.bind('<<TreeviewSelect>>',self.item_selected)
     
    def item_selected(self,event):
        item_id = self.tree.selection()[0]
        item_dict = self.tree.item(item_id)
        print(item_dict['values'])
        dialog = GetdataInfo(self)
        dialog.Datevar.set(item_dict[0])
        

def main():    
    window = Window()
    myFrame = MyFrame(window,"台積電")
    window.mainloop()

if __name__ == "__main__":
    main()