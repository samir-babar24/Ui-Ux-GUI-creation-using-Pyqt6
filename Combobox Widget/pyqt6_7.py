#combobox  for user input

from PyQt6.QtWidgets import QWidget,QMainWindow,QApplication,QLabel,QPushButton,QVBoxLayout,QLineEdit,QComboBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setMinimumSize(400,400)
        self.setWindowIcon(QIcon("virat.jpg"))
        self.setWindowTitle("Using of a combobox")
        
        
        layout=QVBoxLayout()
         
         
        self.label=QLabel("Select regiment which You want to enter in",alignment=Qt.AlignmentFlag.AlignCenter)
        
        
        
        self.combo=QComboBox()
        self.button=QPushButton("click here to proceed")
        self.button.clicked.connect(self.click_output)
        
        self.combo.addItem("Gorkha")
        self.combo.addItem("Rashtriya Rifles")
        self.combo.addItem("Rajputana Rifles")
        self.combo.addItem("10 paraf")
        self.combo.addItem("1 para sf")
        self.combo.addItem("Maratha light infrrantary")
        
        layout.addWidget(self.combo)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        
        xyz=QWidget()
        xyz.setLayout(layout)
        self.setCentralWidget(xyz)
        
    def click_output(self):
        print("you clicked the button")
        self.label.setText("You have clicked the button")
            
            
            
            
            
            

app=QApplication([])
main=main()
  
  
main.show()
app.exec()
      
            
         
            
            
    
    
    
    
    
        