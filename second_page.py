# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QWidget, QDesktopWidget, \
    QMainWindow, QPushButton, QCompleter, QLineEdit
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap


class ingredients(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Page 2"
        self.left = 500
        self.top = 200
        self.width = 700
        self.height = 450
        self.InitWindow()
        self.center()

        # Ask Nehchnehch
        self.lineedit = None

        # Label stuff wasnt working in initwidow so i put it here
        self.label1 = QLabel("Ingredients", self)
        self.label1.move(50, 60)

        # why isnt the number showing
        self.max_label = QLabel("Max number is 4953", self)
        self.max_label.move(3 * (self.width // 4), (self.height // 4) - 40)

    def InitWindow(self):
        # self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        vbox = QVBoxLayout()
        testing = ['check', 'one', 'two', 'three', 'white pepper', 'blue pepper']
        completer = QCompleter(testing)
        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)
        vbox.addWidget(self.lineedit)
        self.setLayout(vbox)

        # Add button
        add = QPushButton("Add", self)
        add.move(3 * (self.width // 4), self.height // 4)
        # add.clicked.connect(self.clicked)

        # Delete button
        delete = QPushButton("Delete", self)
        delete.move(3 * (self.width // 4), (self.height // 4) + 50)

        label_test = QLabel('Text')
        label_test.move(50,70)

        # label = QLabel('Ingredients')
        # label.move(80,200)
        # vbox.addWidget(label)
        # self.setLayout(vbox)
        #
        # w = QtWidgets.QWidget()
        # label = QtWidgets.QLabel(w)
        # label.setText("testing")

    def center(self):  # Used top center the window on the desktop
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
