from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QHBoxLayout,QWidget,QVBoxLayout
from PyQt6.QtGui import QIcon


app=QApplication([])
main=QMainWindow()


main.setMinimumSize(500,500)
main.setWindowTitle("Layouts program ")
main.setWindowIcon(QIcon('virat.jpg'))


#creating two buttons
button1=QPushButton("Click here broo")
font=main.font()
font.setBold(True)
font.setPointSize(11)
button1.setFont(font)

button2=QPushButton("punch here")
font=main.font()
font.setBold(True)
font.setPointSize(11)
button2.setFont(font)


#creating of horizontal bot=x layout
layout=QHBoxLayout()
layout.addWidget(button2)
layout.addWidget(button1)

centralw=QWidget()
centralw.setLayout(layout)

main.setCentralWidget(centralw)

#creating a vertical box layout
layout2=QVBoxLayout()
layout2.addWidget(button1)
layout2.addWidget(button2)

centralw=QWidget()
centralw.setLayout(layout)

main.setCentralWidget(centralw)









main.show()
app.exec()