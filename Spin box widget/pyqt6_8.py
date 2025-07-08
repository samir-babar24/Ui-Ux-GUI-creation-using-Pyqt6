#starting with qspin box



from PyQt6.QtWidgets import QWidget,QMainWindow,QApplication,QLabel,QPushButton,QVBoxLayout,QLineEdit,QSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(300,300)
        self.setWindowTitle("Qspin box")
        
        
        layout=QVBoxLayout()
        
        self.label=QLabel("This is Qspinbox for user input of digits",alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.label2=QLabel("Enter your age for proceeding your army entry application")
        
        
        self.button=QPushButton("Click meeeee")
        self.button.clicked.connect(self.buttonclicked)
        self.box=QSpinBox()
        self.box.setMinimum(18)
        self.box.setMaximum(50)
        self.box.setSingleStep(1)
        
        
        layout.addWidget(self.label)  
        layout.addWidget(self.label2)
        layout.addWidget(self.box)
        layout.addWidget(self.button)
        
     

        
        
        xyz=QWidget()
        xyz.setLayout(layout)
        self.setCentralWidget(xyz)
        
        
        
        
    
    def buttonclicked(self):
        print("you just clicked the button")
        
app=QApplication([])
main=main()

main.show()
app.exec()
