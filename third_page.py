# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QWidget, QDesktopWidget, \
    QMainWindow, QPushButton, QCompleter, QLineEdit, QListWidget, QListView, QHBoxLayout, QAction, \
    QMessageBox, QSpinBox
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QDoubleValidator, QValidator
import data_reading, second_page

class Recipes(QDialog, QWidget):
    def __init__(self):
        super().__init__()

        self.ingredient = QLabel("Ingredients", self)
        self.ingredient.move(30, 50)
        self.max_add_label = QLabel("Max number of ingredients ", self)


        self.all_label = QLabel("All Ingredients", self)
        self.all_label.move(300, 25)


        # self.ing = [self.ing1, self.ing2, self.ing3, self.ing4, self.ing5, self.ing6, self.ing7,
        #             self.ing8, self.ing9, self.ing10]
        #
        # self.list = QListWidget()
        # data = data_reading.read_recipes(data_reading.RECIPES_FILE)
        # data_reading.clean_ingredients(data)
        # self.clean = list(data_reading.get_ingredients(data))
        # for i in range(len(self.clean)):
        #     self.list.insertItem(i, self.clean[i])
        # self.list.setResizeMode(QListView_ResizeMode=)

        self.title = "Page 3"
        self.left = 500
        self.top = 200
        self.width = 700
        self.height = 450
        self.InitWindow()
        self.center()

    def InitWindow(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)



        self.show()

    def center(self):  # Used top center the window on the desktop
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
