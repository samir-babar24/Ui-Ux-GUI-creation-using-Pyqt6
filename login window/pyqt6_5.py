from PyQt6.QtWidgets import QMainWindow,QApplication,QLabel,QWidget,QGridLayout,QLineEdit,QPushButton
from PyQt6.QtCore import  Qt
from PyQt6.QtGui import QIcon,QLinearGradient

app=QApplication([])
main=QMainWindow()

main.setMinimumSize(400,400)
main.setWindowTitle("this is the login page")
main.setWindowIcon(QIcon("pccoee.webp"))





#addeed the layout 
lay=QGridLayout()

#adding pf label of login page
lab=QLabel("Login/signup Page",alignment=Qt.AlignmentFlag.AlignCenter)
font1=main.font()
font1.setBold(True)
font1.setPointSize(15)
lab.setFont(font1)
lay.addWidget(lab,0,0,1,2)

#adding email widget to ato show email adding option
email=QLabel("Email/Phone no:")
font2=main.font()
font2.setBold(False)
font2.setPointSize(12)
email.setFont(font2)
lay.addWidget(email,1,0)


#adding of actual email input
emailin=QLineEdit()
lay.addWidget(emailin,1,1)


#adding paswword widget to ato show email adding option
password=QLabel("Password:")
font2=main.font()
font2.setBold(False)
font2.setPointSize(15)
email.setFont(font2)
lay.addWidget(password,2,0)

#addinf of password input
passin=QLineEdit()
#to hide password
passin.setEchoMode(QLineEdit.EchoMode.Password)
lay.addWidget(passin,2,1)

#adding of submt button
subm=QPushButton("Submitt")
lay.addWidget(subm,3,0,1,2)
subm.setMinimumHeight(30)

#giving prooper hirontal/verticalll spacing
lay.setHorizontalSpacing(50)
lay.setVerticalSpacing(50)

#this is created layout we have stpre it in widget to shoe 
xyz=QWidget()
xyz.setLayout(lay)
main.setCentralWidget(xyz)



#final execution of a code

main.show()
app.exec()