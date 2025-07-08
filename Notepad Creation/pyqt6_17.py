#making of notepad using pyqt6
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow,QApplication,QFileDialog,QLabel,QPushButton,QGridLayout,QTextEdit,QWidget

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Notepad By samir")
        self.setMinimumSize(300,300)
        
        lay=QGridLayout()
        
        self.text=QTextEdit()
        self.b1=QPushButton("Save")
        self.b1.clicked.connect(self.aftersave)
        
        self.b2=QPushButton("Open")
        self.b2.clicked.connect(self.afteropen)
        
        
        lay.addWidget(self.b1,1,0,alignment=Qt.AlignmentFlag.AlignCenter)
        lay.addWidget(self.b2,1,1,alignment=Qt.AlignmentFlag.AlignCenter)
        lay.addWidget(self.text,0,0,1,2)
        
        x= QWidget()
        x.setLayout(lay)
        self.setCentralWidget(x)

    def aftersave(self):
        file=QFileDialog()
        file.setNameFilter("Text file (.txt)")       
        savesuccess=file.exec()
        
        if savesuccess:
            filelocation=file.selectedFiles()[0]                                  
              
            with open(filelocation,mode='w') as file1:
                file1.write(self.text.toPlainText())  
            
            
                                                                                        
                
    def afteropen(self):
        file=QFileDialog()
        file.setNameFilter("Text file (.txt)")
        file.setFileMode(QFileDialog.FileMode.ExistingFile)
      
        
        success=file.exec()
        
        if success:
            file=file.selectedFiles()[0]
            with open(file) as file1:
                self.text.setText(file1.read())
                
app=QApplication([])
wid=main()

wid.show()
app.exec()        
        
        
        
        
        
