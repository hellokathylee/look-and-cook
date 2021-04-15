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
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Look and Cook"
        self.left = 500
        self.top = 200
        self.width = 700
        self.height = 450
        self.InitWindow()
# Make icon too
        #self.setWindowTitle("Look and Cook")  # Setting a title for the window

        # # To make a label
        # label = qtw.QLabel("hi")
        # # Change Size
        # label.setFont(qtg.QFont("Helvetica", 18))
        # self.layout().addWidget(label)


    def InitWindow(self):
        # self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        vbox = QVBoxLayout()
        Image = QLabel(self)
        pixmap = QPixmap("data/testing.png")
        Image.setPixmap(pixmap)
        vbox.addWidget(Image)
        self.setLayout(vbox)
        self.show()  # Opens the window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec())

