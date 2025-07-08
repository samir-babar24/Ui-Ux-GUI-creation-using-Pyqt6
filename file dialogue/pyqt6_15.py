#this is the code of QfiledDialog

from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QWidget,QPushButton,QGridLayout,QMessageBox,QRadioButton,QFileDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap,QIcon

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("this is file dialog system")
        self.setWindowIcon(QIcon("virat.jpg"))
        self.setMinimumSize(200,200)
        self.setStyleSheet("background color:lightyellow;")
        
        lay=QGridLayout()
        
        self.label=QLabel("This is the file opening code and window",alignment=Qt.AlignmentFlag.AlignCenter)
        font=self.font()
        font.setPointSize(14)
        
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red;")
        
        

        
        self.b5=QPushButton("cclick here to open files")
        self.b5.clicked.connect(self.clicked)
        
        lay.addWidget(self.label)
        lay.addWidget(self.b5)
        
 
        
        
       
        
        
        x=QWidget()
        x.setLayout(lay)
        self.setCentralWidget(x)     
        
    def clicked(self):
        
        
        file=QFileDialog()
        
        
        open=file.exec()
        
        if open==1:
            
         print(open)
         
         
        else:
            
            print("User has cancelled")
        
        
      
       
            
            
app=QApplication([])        
main=main()        
        
        
main.show()       
app.exec()        