#this is the input dialogue box



from PyQt6.QtWidgets import QMainWindow,QApplication,QPushButton,QMessageBox,QLabel,QInputDialog
from PyQt6.QtCore import Qt

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("This is samir's 11th code")
        self.setMinimumSize(200,200)
        
        self.label=QLabel("HEloo this is tutorial of dialoginput",alignment=Qt.AlignmentFlag.AlignTop)
        self.button=QPushButton("If you want to submit /cancle ur application  click here")
        self.button.setMinimumSize(20,10)
        
        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.afterclick)
        self.setMenuWidget(self.label)
        
        
    def afterclick(self):
            input=QInputDialog()
            input.setLabelText(" Enter your Job expectation salary")
            
            clicked=input.exec()
            
            if clicked == 1:
                print(input.textValue)
            else : 
                print("User Havent Clicked")
         
            
                                           
                                           
                                           
                                           
app=QApplication([]) 
main=main()


main.show()
app.exec()                                          
                                           