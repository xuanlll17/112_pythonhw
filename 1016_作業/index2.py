import dataSource   #自訂module
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):    #繼承tk.TK
    def __init__(self, **kwargs):   #**kwargs 轉換為引數名稱呼叫(沒有限定數量)    #父類別有default value時
        #super() 執行父類別
        super().__init__(**kwargs)  #super().__init__ 繼承父類別的__init__
        self.title("鄉鎮人口統計")
        self.configure(background='#81C7D4')    #設定背景色

        topFrame = tk.Frame(self, background='#0089A7')
        label = ttk.Label(topFrame,text="鄉鎮人口統計", font=('Helvetica', '30'))
        label.pack(padx=20,pady=20)
        topFrame.pack()

        bottomFrame = tk.Frame(self, background='#2E5C6E')
        choices = dataSource.cityNames()
        choicesvar = tk.StringVar(value=choices)
        self.listbox = tk.Listbox(bottomFrame, listvariable=choicesvar, width=15)
        self.listbox.pack(pady=20)
        bottomFrame.pack(expand=True, fill='x')
        self.listbox.bind("<<ListboxSelect>>", self.user_selected) #self.user_selected要有self,沒有會出錯

        #grid 表格
        resultFrame = tk.Frame(self)
        tk.Label(resultFrame,text="年度:").grid(column=0,row=0,sticky='E',pady=5)
        tk.Label(resultFrame,text="地區:").grid(column=0,row=1,sticky='E',pady=5)
        tk.Label(resultFrame,text="人口數:").grid(column=0,row=2,sticky='E',pady=5)
        tk.Label(resultFrame,text="土地面積:").grid(column=0,row=3,sticky='E',pady=5)
        tk.Label(resultFrame,text="人口密度:").grid(column=0,row=4,sticky='E',pady=5)
        self.yearVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.yearVar).grid(column=1,row=0,sticky='W')
        self.cityVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.cityVar).grid(column=1,row=1,sticky='W')
        self.populationVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.populationVar).grid(column=1,row=2,sticky='W')
        self.areaVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.areaVar).grid(column=1,row=3,sticky='W')
        self.densityVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.densityVar).grid(column=1,row=4,sticky='W')
        resultFrame.pack()

    def user_selected(self, event):  
        #event 名稱(可以更改) 點選listbox內容後會回傳值到event 
        #沒設定,點擊listbox內容會出現錯誤
        selectedIndex = self.listbox.curselection()[0] #抓出所有鄉鎮的資料存成tuple,[0]是抓出鄉鎮的名字顯示出來
        cityName = self.listbox.get(selectedIndex) #抓出點擊鄉鎮的資料
        datalist = dataSource.info(cityName)
        self.yearVar.set(datalist[0])   
        self.cityVar.set(datalist[1])
        self.populationVar.set(datalist[2])
        self.areaVar.set(datalist[3])
        self.densityVar.set(datalist[4])
        
        

def main():
   window = Window()
   window.mainloop()


if __name__ == "__main__":
    main()  #呼叫main function