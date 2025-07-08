from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QWidget,QPushButton,QGridLayout,QButtonGroup,QCheckBox,QMessageBox,QRadioButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap,QIcon

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("This is Mixture of the widgets")
        self.setWindowIcon(QIcon("virat.jpg"))
        self.setMinimumSize(300,300)
        self.setStyleSheet("background color:lightyellow;")
        
        lay=QGridLayout()
        
        self.label=QLabel("This is the radio buttons and q message box code",alignment=Qt.AlignmentFlag.AlignTop)
        font=self.font()
        font.setPointSize(14)
        
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red;")
        
        
        self.label1=QLabel("This is indian army posting locations so click accordingly",alignment=Qt.AlignmentFlag.AlignCenter)
        font=self.font()
        font.setPointSize(12)
        font.setBold(True)
        self.label1.setFont(font)
        
        
        self.b1=QRadioButton("Guwahati")
        self.b2=QRadioButton("Myanmar")
        self.b3=QRadioButton("assam")
        self.b4=QRadioButton("J&K")
        
        
        self.group=QButtonGroup()
        self.group.addButton(self.b1)
        self.group.addButton(self.b2)
        self.group.addButton(self.b3)
        self.group.addButton(self.b4)
        
        
        self.b5=QPushButton("cclick here to submit")
        self.b5.clicked.connect(self.clicked)
        
        lay.addWidget(self.label)
        lay.addWidget(self.label1)
        lay.addWidget(self.b1)
        lay.addWidget(self.b2)
        lay.addWidget(self.b3)
        lay.addWidget(self.b4)   
        lay.addWidget(self.b5)
        
        
       
        
        
        x=QWidget()
        x.setLayout(lay)
        self.setCentralWidget(x)     
        
    def clicked(self):
        message = QMessageBox()
        message.setText("This is the conirmation call for YOur recruitment")
        message.setIcon(QMessageBox.Icon.Warning)
        message.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        message.setEscapeButton(QMessageBox.StandardButton.Escape)

       
        final= message.exec()
        
        if final == QMessageBox.StandardButton.Ok:
            print("Congratulations  Lieutenant saab")
     
        else:
            print("Go back from here and decide again")
            
            
app=QApplication([])        
main=main()        
        
        
main.show()       
app.exec()        