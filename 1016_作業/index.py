'''
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import Dialog
import csv


class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("台積電股價")

class GetdataInfo(Dialog):

    def body(self, master):
        self.title("查看")

        tk.Label(master, text='Date:').grid(row=0, sticky=tk.W)
        tk.Label(master, text='Open:').grid(row=1, sticky=tk.W)
        tk.Label(master, text='High:').grid(row=2, sticky=tk.W)
        tk.Label(master, text='Low:').grid(row=3, sticky=tk.W)
        tk.Label(master, text='Close:').grid(row=4, sticky=tk.W)
        tk.Label(master, text='AdjClose:').grid(row=5, sticky=tk.W)
        tk.Label(master, text='Volume:').grid(row=6, sticky=tk.W)


        self.datevar = tk.StringVar()
        self.openvar = tk.StringVar()
        self.highvar = tk.StringVar()
        self.lowvar = tk.StringVar()
        self.closevar = tk.StringVar()
        self.adjclosevar = tk.StringVar()
        self.volumevar = tk.StringVar()

        tk.Label(master, textvariable=self.datevar).grid(row=0,column=1, sticky=tk.E)
        tk.Label(master, textvariable=self.openvar).grid(row=1,column=1, sticky=tk.E)
        tk.Label(master, textvariable=self.highvar).grid(row=2,column=1, sticky=tk.E)
        tk.Label(master, textvariable=self.lowvar).grid(row=3,column=1, sticky=tk.E)
        tk.Label(master, textvariable=self.closevar).grid(row=4,column=1, sticky=tk.E)
        tk.Label(master, textvariable=self.adjclosevar).grid(row=5,column=1, sticky=tk.E)
        tk.Label(master, textvariable=self.volumevar).grid(row=6,column=1, sticky=tk.E)
        

    def buttonbox(self):

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

        #Treeview------------------------------------------------------------------------
        self.tree = ttk.Treeview(self,columns=['#1', '#2', '#3', '#4', '#5', '#6', '#7'],show="headings")
        self.tree.heading('#1', text="Date")
        self.tree.heading('#2', text="Open")
        self.tree.heading('#3', text="High")
        self.tree.heading('#4', text="Low")
        self.tree.heading('#5', text="Close")
        self.tree.heading('#6', text="AdjClose")
        self.tree.heading('#7', text="Volume")
    
        #scrollbar-----------------------------------------------------------------------
        self.scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side='right',fill='y')
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        #insert data---------------------------------------------------------------------
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
        
        self.pack(expand=1,fill='both',padx=10,pady=10)
        self.tree.pack()

        #bind-----------------------------------------------------------------------------
        self.tree.bind('<<TreeviewSelect>>',self.item_selected)
     
    def item_selected(self,event):
        item_id = self.tree.selection()[0]
        item_dict = self.tree.item(item_id)
        value = item_dict['values']
        print(value[0],value[1],value[2],value[3],value[4],value[5],value[6])
        
        dialog = GetdataInfo(self)
        dialog.datevar.set(value[0])
        dialog.openvar.set(value[1])
        

def main():    
    window = Window()
    myFrame = MyFrame(window,"台積電")
    window.mainloop()

if __name__ == "__main__":
    main()