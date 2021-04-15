"""CSC111 Final Project, Data Reading

Description
===============================
This module reads the raw data from the csv file and converts it into a usable format.
===============================

This file is provided solely for the personal and private use of TA's and professors
teaching CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 Dana Alshekerchi, Nehchal Kalsi, Kathy Lee, Audrey Yoshino.
"""

# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QWidget, QDesktopWidget, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap


class MainWindow(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Look and Cook"
        self.left = 500
        self.top = 200
        self.width = 700
        self.height = 450
        self.InitWindow()
        self.center()
    # Make icon too
    # self.setWindowTitle("Look and Cook")  # Setting a title for the window

    # # To make a label
    # label = qtw.QLabel("hi")
    # # Change Size
    # label.setFont(qtg.QFont("Helvetica", 18))
    # self.layout().addWidget(label)

    def center(self):  # Used top center the window on the desktop
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def InitWindow(self):
        # self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        vbox = QVBoxLayout()
        # for title image
        Image = QLabel()
        pixmap = QPixmap("testing.png")
        Image.setPixmap(pixmap)
        vbox.addWidget(Image, alignment=Qt.AlignCenter)

        # Button stuff
        b1 = QPushButton("Start", self)
        b1.move((self.width//2)-50, self.height//2 + 100)
        b1.clicked.connect(self.clicked)


        self.setLayout(vbox)
        self.show()  # Opens the window

    def clicked(self):
        self.hide()
        mydialog = QDialog(self)
        # mydialog.setModal(True)
        # mydialog.exec_()
        # Copied it from center, figure out why it didnt work before
        mydialog.setGeometry(self.left, self.top, self.width, self.height)
        qr = mydialog.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        mydialog.move(qr.topLeft())


        mydialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
