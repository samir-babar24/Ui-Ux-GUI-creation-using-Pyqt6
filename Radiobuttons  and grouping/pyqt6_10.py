from PyQt6.QtWidgets import QWidget,QMainWindow,QApplication,QLabel,QPushButton,QVBoxLayout,QRadioButton,QButtonGroup
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon,QPixmap


class samir(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setMinimumSize(400,400)
        self.setWindowTitle("this is basic of radio buttons")
        self.setWindowIcon(QIcon("pccoee.webp"))
        
        
        #layout
        layout=QVBoxLayout()
        
        
        #lables
        self.label1=QLabel("Rdio buttons tutorial",alignment=Qt.AlignmentFlag.AlignTop)
        font=self.font()
        font.setPointSize(15)
        font.setBold(True)
        self.label1.setStyleSheet("color:red;")
        
        
        self.label2=QLabel("Chose your fav posting from following",alignment=Qt.AlignmentFlag.AlignCenter)
        font=self.font()
        font.setPointSize(13)
        font.setBold(True)
        self.label2.setStyleSheet("color:purple;")
        
        #radio buttons
        self.button1=QRadioButton("Arunachal")
        self.button2=QRadioButton("Sikkim")
        self.button3=QRadioButton("kashmir")
        self.button4=QRadioButton("Rajsthan")
        
        #grouping radion buttons
        self.buttonGroup=QButtonGroup()

        self.buttonGroup.addButton(self.button1)
        self.buttonGroup.addButton(self.button2)    
        self.buttonGroup.addButton(self.button2)   
        self.buttonGroup.addButton(self.button2) 
        
       
        #push button 
        self.button5=QPushButton("Click here toapply for this posting")
        
      
        
        self.button5.clicked.connect(self.clicked)
        
        #adding image
        self.image=QPixmap("army.jpg")
        self.image.setDevicePixelRatio(2.0)

        #adding to layyout
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        
        
        xyz=QWidget()
        xyz.setLayout(layout)
        self.setCentralWidget(xyz)
        
        
        
        
        
        
               
        
        
    def clicked(self):
        print("clicked")
        self.label2.setText("You have hust chosen ur dream posting")
        
        
        
app=QApplication([])
main=samir()

main.show()
app.exec()
