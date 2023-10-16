import yfinance as yf
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
from tkinter import messagebox
import csv

#抓股票
data = yf.download("0050.TW", start='2023-01-01')
data.to_csv("0050.csv")

#版面設定
class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("小小股票介面")

#樹狀
class Frame(ttk.LabelFrame):
    def __init__(self,master,title, **kwargs):
        super().__init__(master=master,text=title,**kwargs)
        self.tree=ttk.Treeview(self,columns=["date","open","high","low","close","adjclose","volume"],show="headings")
        self.tree.heading("date",text="日期")
        self.tree.heading("open",text="開盤價")
        self.tree.heading("high",text="最高價")
        self.tree.heading("low",text="最低價")
        self.tree.heading("close",text="收盤價")
        self.tree.heading("adjclose",text="調整後收盤價")
        self.tree.heading("volume",text="成交量")

        with open('0050.csv', 'r', encoding='UTF-8') as file:
            data=csv.reader(file)
            next(data)
            text=[]
            text.append([f"日期：{0}",f"開盤價：{1}",f"最高價：{2}",f"最低價：{3}"
                        ,f"收盤價：{4}",f"調整後收盤價：{5}",f"成交量：{6}"])
            
            for t in data:
                self.tree.insert("",tk.END,values=t)
            self.tree.pack()

        self.tree.bind("<<TreeviewSelect>>",self.item)

        self.pack(expand=1,fill="both",padx=10,pady=20)
    
    def item(self,event):
        item_id=self.tree.selection()[0]
        item_dict=self.tree.item(item_id)

    def choise(self):
        print(self.user.get())


#還沒辦法顯示
class GetPassword(Dialog,Frame):
    def body(self, master):
        self.title(f"0050{Frame.date}資料")

        data1=tk.Label(master, text='開盤價：').grid(row=0, sticky=tk.W)
        data2=tk.Label(master, text='最高價：').grid(row=1, sticky=tk.W)
        data3=tk.Label(master, text='最低價：').grid(row=2, sticky=tk.W)
        data4=tk.Label(master, text='收盤價：').grid(row=3, sticky=tk.W)
        data5=tk.Label(master, text='調整後收盤價：').grid(row=4, sticky=tk.W)
        data6=tk.Label(master, text='成交量：').grid(row=5, sticky=tk.W)

        data1.grid(row=0, column=1, sticky=tk.W)
        data2.grid(row=1, column=1, sticky=tk.W)
        data3.grid(row=2, column=1, sticky=tk.W)
        data4.grid(row=3, column=1, sticky=tk.W)
        data5.grid(row=4, column=1, sticky=tk.W)
        data6.grid(row=5, column=1, sticky=tk.W)
        self.pack(expand=1,fill="both",padx=10,pady=20)

    #確認/取消鍵
    def buttonbox(self):
        box = tk.Frame(self)

        w = tk.Button(box, text="確認", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="取消", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

'''
不知道這啥
root = Tk()
dialog = GetPassword(root)
'''



def main():
    window=Window()
    frame=Frame(window,"0050")
    window.mainloop()

if __name__ == "__main__":
    main()