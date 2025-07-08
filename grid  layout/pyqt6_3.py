from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QHBoxLayout,QWidget,QVBoxLayout
from PyQt6.QtGui import QIcon

app=QApplication([])
main=QMainWindow()
main.setMinimumSize(500,500)
main.setWindowTitle("mixture ofLayouts program ")
main.setWindowIcon(QIcon('virat.jpg'))






#creting a mixture of both layouts
parentlay=QVBoxLayout()
lay=QHBoxLayout()

button1=QPushButton("click")
button2=QPushButton("Punch")

lay.addWidget(button1)
lay.addWidget(button2)

parentlay.addLayout(lay)

lable=QLabel("this is a mixture of horizontal and verical widgets")
parentlay.addWidget(lable)

centralw=QWidget()
centralw.setLayout(parentlay)













#vice vera mixture


parentlay1=QHBoxLayout()
lay2 = QVBoxLayout()

lay2.addWidget(button1)
lay2.addWidget(button2)

parentlay1.addLayout(lay2)

parentlay1.addWidget(lable)

centralw.setLayout(parentlay1)



main.setCentralWidget(centralw)





main.show()
app.exec() 