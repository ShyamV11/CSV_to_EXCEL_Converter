#from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import pandas as pd


win = tk.Tk()
win.geometry("350x350")
win.title("Converter")
win.configure(background='black')

file = None
label_style = {"bg":"black","fg":"white","font":"-size 30 -weight bold"}
button_style1 = {"bg":"red","fg":"white","font":"-size 15 -weight bold"}
button_style2 = {"bg":"green","fg":"white","font":"-size 15 -weight bold"}

def browse():
    global file
    file = filedialog.askopenfilename(
            filetypes=(('File','*.csv'), ("All Files",'*')))

def convert():
    try:
        xlsx = file.replace(".csv",".xlsx")
        read_file = pd.read_csv (file)
        read_file.to_excel (xlsx, index = None, header = True)
        messagebox.showinfo("Success!!", "File converted and saved")
    except:
        messagebox.showerror("Error!!!", "Please select file!!!")

label = tk.Lable(win, text='Converter', **label_style)
button1 = tk.Button(win, text='     Choose a csv file    ', command=browse, **button_style1)
button2 = tk.Button(win, text='Convert csv to xlsx', command=convert, **button_style2)

label.place(x = 50 , y = 50)
button1.place(x = 85 , y = 135)
button2.place(x = 85 , y = 190)

win.mainloop()


