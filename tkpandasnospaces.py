import sys
import os
import pandas as pd
from tkinter import filedialog, Tk, Button, Label, TOP
import tkinter as tk


def upload():

        path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx")])
        file_name = os.path.basename(path)
        file = os.path.splitext(file_name)      
        if path:
            #print(path)
            df = pd.read_excel(path)
            df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
            #print (df)
            #print(file[0]+"_nospaces.xlsx")
            df.to_excel (file[0]+"_nospaces.xlsx", index=False)

        if not file:
            return
        #else:
            #print("Done!") 

class MyApp:
        root = Tk()
        l = Label(root, text = "Fact of the Day")
        root.geometry('400x300')
        button = Button(root, text = 'Upload', command = upload)
        button.pack(side = TOP, pady = 105)           



tk.mainloop()

