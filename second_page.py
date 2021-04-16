# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QWidget, QDesktopWidget, \
    QMainWindow, QPushButton, QCompleter, QLineEdit, QListWidget, QListView, QHBoxLayout
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import data_reading


class ingredients(QDialog):
    def __init__(self):
        super().__init__()

        self.ingredient = QLabel("Ingredients", self)
        self.ingredient.move(30, 50)
        self.max_add_label = QLabel("Max number is 4953", self)
        self.max_add_label.move(5, 10)
        self.max_time_label = QLabel("Max time", self)
        self.max_time_label.move(100, 59)
        self.all_label = QLabel("All Ingredients", self)
        self.all_label.move(200, 70)
        self.list = QListWidget()
        data = data_reading.read_recipes(data_reading.RECIPES_FILE)
        data_reading.clean_ingredients(data)
        clean = list(data_reading.get_ingredients(data))
        for i in range(len(clean)):
            self.list.insertItem(i, clean[i])
        # self.list.setResizeMode(QListView_ResizeMode=)

        self.title = "Page 2"
        self.left = 500
        self.top = 200
        self.width = 700
        self.height = 450
        self.InitWindow()
        self.center()

        self.line_edit = None


    def InitWindow(self):
        # self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        # vbox = QVBoxLayout()
        # testing = ['check', 'one', 'two', 'three', 'white pepper', 'blue pepper']
        # completer = QCompleter(testing)
        # completer.setFilterMode(Qt.MatchContains)
        # self.line_edit = QLineEdit()
        # self.line_edit.setCompleter(completer)
        # vbox.addWidget(self.line_edit, alignment=Qt.AlignLeft)
        # vbox.addWidget(self.list, alignment=Qt.AlignCenter)
        # self.setLayout(vbox)

        # Figure out placement
        vbox = QVBoxLayout()
        vbox.setContentsMargins(100, 150, 100, 100)
        self.list.setFixedSize(300, 150)
        vbox.addWidget(self.list)
        self.setLayout(vbox)

        # Add button
        add = QPushButton("Add", self)
        add.move(3 * (self.width // 4), self.height // 4)
        # add.clicked.connect(self.clicked)

        # Delete button
        delete = QPushButton("Delete", self)
        delete.move(3 * (self.width // 4), (self.height // 4) + 50)

        label_test = QLabel('Text')
        label_test.move(50, 70)

        self.show()

    def center(self):  # Used top center the window on the desktop
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
