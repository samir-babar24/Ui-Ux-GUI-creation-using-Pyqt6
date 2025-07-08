#signals,events and slots


from PyQt6.QtWidgets import QWidget,QMainWindow,QApplication,QLabel,QPushButton,QVBoxLayout,QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon



#we are moving for the signals

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        layout=QVBoxLayout()
        
        self.setMinimumSize(400,400)
        self.setWindowTitle("window to check wheratger buton is clixked or not") 
        
           
        self.lineedit=QLineEdit()
        self.lineedit.setPlaceholderText("Enter wanything here")
        self.label=QLabel("This is samirrr over here!!",alignment=Qt.AlignmentFlag.AlignCenter)
        self.button=QPushButton("Click me broo")
        self.button.clicked.connect(self.third_s)
        
        
        layout.addWidget(self.label)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.button)
        
        
        xyz=QWidget()
        xyz.setLayout(layout)
        self.setCentralWidget(xyz)
        
     # first signal   
    def output_button(self):
        print("you justclicked the button mann")
        
    #second signal
    def second_s(self):
        print("clicked")
        
    #third signal
    def third_s(self):
        print("toggled")
        self.label.setText("You have just toggled the button")
        
            
        



        

    
    
    
    
    
app=QApplication([])    
main=Main()    



main.show()
app.exec()