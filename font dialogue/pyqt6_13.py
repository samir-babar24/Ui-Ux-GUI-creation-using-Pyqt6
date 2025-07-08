from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QPushButton, QMessageBox,
    QLabel, QVBoxLayout, QFontDialog, QWidget
)
from PyQt6.QtCore import Qt

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("This is Samir's 11th code")
        self.setMinimumSize(300, 300)
        
        lay = QVBoxLayout()
        
        self.label = QLabel("Hello, this is a tutorial of dialog input")
        self.button = QPushButton("If you want to submit/cancel your application, click here")
        
        self.button.clicked.connect(self.afterclick)
        
        lay.addWidget(self.label)
        lay.addWidget(self.button)
        
        x = QWidget()
        x.setLayout(lay)
        
        self.setCentralWidget(x)  
        
    def afterclick(self):
        dialog = QFontDialog()
        clicked = dialog.exec()
        
        if clicked:
            font = dialog.selectedFont()
            self.label.setFont(font)

# Application setup
app = QApplication([])
mainwindow = main()
mainwindow.show()  
app.exec()
