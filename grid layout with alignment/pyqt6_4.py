from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QGridLayout,QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


app=QApplication([])
main=QMainWindow()

main.setMinimumSize(500,500)
main.setWindowTitle("This is the window of grid layout exampls")
main.setWindowIcon(QIcon("download.jpg"))

#adding the main grid layout

parentl=QGridLayout()

#giving label to it 

lab=QLabel("THIS  is the window of grid layout",alignment=Qt.AlignmentFlag.AlignCenter)
font=main.font()
font.setBold(True)
font.setPointSize(13)
lab.setFont(font)
parentl.addWidget(lab,0,0,1,2)  #here the 0 ,0 mean     sfirst row and first column


#row, column, rowSpan, columnSpan==( ,  , ,)

button1=QPushButton( "this is the first push button" )
button2=QPushButton("this is the second push button")
parentl.addWidget(button1,1,0) #second row first column
parentl.addWidget(button2,1,1) #secong row and seconf columnss

parentl.setHorizontalSpacing(60)


#aligning everything at center

xyz=QWidget()
xyz.setLayout(parentl)

main.setCentralWidget(xyz)



main.show()
app.exec()