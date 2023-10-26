import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource
from threading import Timer

class Window(tk.Tk):                       #繼承tkinter裡的Tk
    def __init__(self, **kwargs):          #keyword = kw, args = 引數
        super().__init__(**kwargs)         #呼叫父類別的__init__, self不用寫 
        try:
            datasource.update_sqlite_data()
        except Exception as e:                     
            messagebox.showerror(e)
            self.destroy()                 #關閉視窗
    

t = None
def main():
    def on_closing():
        print("window關閉")
        t.cancel()
        window.destroy()

    
    def update_data()->None:
        datasource.update_sqlite_data()
        global t
        t = Timer(3600,update_data)
        t.start()  

    window = Window()
    window.title('空氣品質')
    window.geometry('600x300')
    window.resizable(width=False,height=False)
    update_data()
    window.protocol("WM_DELETE_WINDOW",on_closing)      
    window.mainloop()



if __name__ == '__main__':
    main()