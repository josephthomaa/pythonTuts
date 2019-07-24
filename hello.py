import tkinter as tk    
from tkinter import ttk    
win = tk.Tk()  
a,b=0,1
win.title("Python GUI App")
while b<10:
   ttk.Label(win, text=b).pack()  
   a,b=b,a+b   
    
  
win.mainloop()   