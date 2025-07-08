#this is the code of QfiledDialog with filtering

from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QWidget,QPushButton,QGridLayout,QMessageBox,QRadioButton,QFileDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap,QIcon

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("This is the idle dialog systeenm")
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
        
        

        
        self.b1=QPushButton("jpg files")
        self.b1.clicked.connect(self.clickedjpg)
        
        
        self.b2=QPushButton("Python files")
        self.b2.clicked.connect(self.clickedpython)
        
        self.b3=QPushButton("Pdf files")
        self.b3.clicked.connect(self.clickedpdf)
        
        self.b4=QPushButton("cpp files")
        self.b4.clicked.connect(self.clickcpp)
        
        
        
        
        lay.addWidget(self.label)
        lay.addWidget(self.b1)
        lay.addWidget(self.b2)
        lay.addWidget(self.b3)
        lay.addWidget(self.b4)
        
        
        x=QWidget()
        x.setLayout(lay)
        self.setCentralWidget(x)  
       
        
 
        
        
       
        
        
         
        
    def clickedjpg(self):
        file=QFileDialog()
        file.setNameFilter("*.jpg")
        yz=file.exec()
        
        if yz:
            print(yz)
        else :
            print("User Has Cancelled")
            
            
    def clickedpdf(self):
        
        
        file=QFileDialog()
        
        file.setNameFilter("*.pdf")
        yz=file.exec()
        
        if yz :
            print(yz)
            
        else :
            print("User Has Cancelled")
    
    
    
    def clickcpp(self):
        
        
        file=QFileDialog()
        
        
        file.setNameFilter("*.cpp")
        yz=file.exec()
        
        if yz :
            print(yz)
            
        else :
            print("User Has Cancelled")

                
    def clickedpython(self):
        
        
        file=QFileDialog()
        
        
        file.setNameFilter("*.py")
        yz=file.exec()
        
        if yz :
            print(yz)
            
        else :
            print("User Has Cancelled")
            
            
    
    
    
    
    
    
    
        
        
      
       
            
            
app=QApplication([])        
main=main()        
        
        
main.show()       
app.exec()        