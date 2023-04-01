import tkinter as tk
from tkinter import filedialog
import openpyxl

class ExcelApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Excel White Space Remover')
        self.root.geometry('600x200')
        
        # Create the GUI elements
        self.label_file = tk.Label(self.root, text='Select an Excel file:')
        self.label_file.place(x=20, y=20)
        self.button_file = tk.Button(self.root, text='Browse', command=self.select_file)
        self.button_file.place(relx=.5, y=60, anchor="center")
        
        self.button_remove = tk.Button(self.root, text='Remove White Spaces', command=self.remove_spaces)
        self.button_remove.place(relx=.5, y=100, anchor="center")
        
        self.label_status = tk.Label(self.root, text='')
        self.label_status.place(relx=.5, y=140, anchor="center")
        self.label_status.config(width=40)
        
    def select_file(self):
        # Open a file dialog to select an Excel file
        filename = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx')])
        if filename:
            self.label_file.config(text='Selected file: ' + filename)
            self.filename = filename
        
    def remove_spaces(self):
        # Remove white spaces from all cells in the Excel file, including merged cells
        try:
            # Load the Excel file
            wb = openpyxl.load_workbook(self.filename)
            
            for sheet in wb:
                # Iterate over all rows and columns in the sheet
                for row in sheet.iter_rows():
                    for cell in row:
                        # Remove white spaces from the cell value
                        if isinstance(cell.value, str):
                            cell.value = cell.value.strip()
            
            # Save the updated Excel file
            wb.save(self.filename)
            
            self.label_status.config(text='White spaces removed!')
        except Exception as e:
            self.label_status.config(text='Error: ' + str(e))

root = tk.Tk()
app = ExcelApp(root)
root.mainloop()