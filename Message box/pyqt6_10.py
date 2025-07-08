#this is messge box after clicking the buttons

from PyQt6.QtWidgets import QMainWindow,QApplication,QPushButton,QMessageBox,QLabel,QGridLayout
from PyQt6.QtCore import Qt

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("This is samir's 11th code")
        self.setMinimumSize(200,200)
        
        self.label=QLabel("Here what we are doing is connecting the push button to the ok/cancle button thats it",alignment=Qt.AlignmentFlag.AlignTop)
        self.button=QPushButton("If you want to submit /cancle ur application  click here")
        self.button.setMinimumSize(20,10)
        
        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.afterclick)
        self.setMenuWidget(self.label)
        
        
    def afterclick(self):
            message=QMessageBox()
            message.setText("You want to continue sir?")
            message.setIcon(QMessageBox.Icon.Question)
            message.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            
            clicked=message.exec()
            
            if clicked == QMessageBox.StandardButton.Ok:
                print("Your apllications is submitted")
            else:
                print("WE are going back to home screenn")
                
            
            
                                           
                                           
                                           
                                           
app=QApplication([]) 
main=main()


main.show()
app.exec()                                          
                                           