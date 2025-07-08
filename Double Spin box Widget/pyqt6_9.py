from PyQt6.QtWidgets import QWidget,QMainWindow,QApplication,QLabel,QPushButton,QVBoxLayout,QLineEdit,QSpinBox,QDoubleSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setMinimumSize(400,400)
        self.setWindowTitle("This is double Q spinbox")
        self.setWindowIcon(QIcon("pccoe.webp"))
        self.setStyleSheet("background-color:darktblue;")
        
        self.label=QLabel("This is the double spin box ,specially for saving float values",alignment=Qt.AlignmentFlag.AlignTop)
        font=self.font()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red;")
        
        layout = QVBoxLayout()
        
        self.button=QPushButton("Click me")
        self.button.clicked.connect(self.afterclick)
        
        
        self.box=QDoubleSpinBox()
        self.box.setMinimum(5.5)
        self.box.setMaximum(10.5)
    
        self.label2=QLabel("Enter childs age for polio dose",alignment=Qt.AlignmentFlag.AlignCenter)
        self.label2.setStyleSheet("color:yellow;font-size:12px;")
        
        
        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        layout.addWidget(self.box)
        layout.addWidget(self.button)
        
        
        
        xyz=QWidget()
        xyz.setLayout(layout)
        self.setCentralWidget(xyz)
            
            
            
        
        
    def afterclick(self):
        print("clicked")
        self.label2.setText("Thank you you can successfully registerred")
        
        
        
app=QApplication([])        
tru=main()
tru.show()
app.exec()

###the endddddd truuuu
        
        
        
        
        