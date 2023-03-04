import sys
import os
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("SpaceTrim ")
        self.setGeometry(400, 400, 400, 200)
        self.UiComponents()
        self.show()

    def UiComponents(self):
  
        button = QPushButton("Upload excel", self)
        button.move(150, 70)
        button.clicked.connect(self.upload)
        text = QLabel(self)
        text.setText(" Your new created excel file name:'Your file name'_nospaces.xlsx")
        text.resize(400, 100)
        text.move(0, 110)

    def upload(self):

        path, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                                "", "Excel Files (*.xlsx)")
        file_name = os.path.basename(path)
        file = os.path.splitext(file_name)      
        if check:
            print(path)
            df = pd.read_excel(path)
            df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
            print (df)
            print(file[0]+"_nospaces.xlsx")
            a = file[0]+"_nospaces.xlsx"
            df.to_excel(file[0]+"_nospaces.xlsx", index=False)
        if not file:
            return


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

