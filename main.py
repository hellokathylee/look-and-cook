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
import second_page
from typing import Optional


class MainWindow(QDialog, QWidget):
    """Opens the initial starting window for Look and Cook.

    Contains the logo, start button, and code to handle a click event.

    Instance attributes:
        - title: The title of this window
        - left: #TODO complete instance attribute
        - top: #TODO complete instance attribute
        - width: The width of this window
        - height: The height of this window
    """
    title: str
    left: int
    top: int
    width: int
    height: int

    def __init__(self) -> None:
        """Initialize an instance of MainWindow.
        """
        super().__init__()
        self.title = "Look and Cook"
        self.left = 500
        self.top = 200
        self.width = 700
        self.height = 450
        self.InitWindow()
        self.center()
        self.second_page = None
    # Make icon too
    # self.setWindowTitle("Look and Cook")  # Setting a title for the window

    # # To make a label
    # label = qtw.QLabel("hi")
    # # Change Size
    # label.setFont(qtg.QFont("Helvetica", 18))
    # self.layout().addWidget(label)

    def center(self) -> None:
        """Center MainWindow on the provided desktop screen.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def InitWindow(self) -> None:
        """Open the main window on the user's screen with the provided dimensions.
        """
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

    def clicked(self) -> None:
        """Link the start button to the second window displaying ingredient choices.
        """
        self.hide()
        # mydialog = QDialog(self)
        # # mydialog.setModal(True)
        # # mydialog.exec_()
        # # Copied it from center, figure out why it didnt work before
        # mydialog.setGeometry(self.left, self.top, self.width, self.height)
        # qr = mydialog.frameGeometry()
        # cp = QDesktopWidget().availableGeometry().center()
        # qr.moveCenter(cp)
        # mydialog.move(qr.topLeft())
        #
        # # Things in the second window
        # mydialog.label = QLabel('Ingredients')
        # # test = QtWidgets.QWidget()
        # # label = QtWidgets.QLabel(test)
        # # label.setText('Ingredients')
        # mydialog.label.move(500, 70)
        if self.second_page is None:
            self.second_page = second_page.ingredients()
            self.second_page.show()
            # self.second_page.activate

            #        mydialog.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
