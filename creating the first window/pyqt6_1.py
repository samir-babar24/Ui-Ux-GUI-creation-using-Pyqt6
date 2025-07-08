 
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

#setting up a window  we need Qapplication,QmainWindow,
app=QApplication([])

main= QMainWindow()

main.setMinimumSize(700,400)


main.setWindowTitle("This is samir's first window")

#settign main image of a window
main.setWindowIcon(QIcon('download.jpg'))


#adding the first widget , we need Qlable,Qt
from PyQt6.QtCore import Qt

lable=QLabel("enter your name lieutenant",alignment=Qt.AlignmentFlag.AlignCenter)
#setting up the font
font=main.font()
font.setBold(True)
font.setPointSize(20)

lable.setFont(font)
main.setCentralWidget(lable)


#setting up a image 
#initialize pixmap

from PyQt6.QtGui import QPixmap
lable2=QLabel()
lable2.setPixmap(QPixmap('download.jpg'))
main.setCentralWidget(lable2)


#creating a push button with importing QPushButton
button=QPushButton("CLICK HERE")
button.setFont(font)
button.setFixedSize(300,300)
main.setCentralWidget(button)




main.show()
app.exec()


