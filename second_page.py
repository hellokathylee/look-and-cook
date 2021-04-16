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
import data_reading


class ingredients(QDialog, QWidget):
    def __init__(self):
        super().__init__()




        self.ingredient = QLabel("Ingredients", self)
        self.ingredient.move(30, 50)
        self.max_add_label = QLabel("Max number of ingredients ", self)

        self.max_time_label = QLabel("Max time", self)

        self.all_label = QLabel("All Ingredients", self)
        self.all_label.move(300, 25)

        self.time = QSpinBox(self)
        self.time.setRange(0, 50000)

        self.ing1 = QLineEdit(self)
        self.ing2 = QLineEdit(self)
        self.ing3 = QLineEdit(self)
        self.ing4 = QLineEdit(self)
        self.ing5 = QLineEdit(self)
        self.ing6 = QLineEdit(self)
        self.ing7 = QLineEdit(self)
        self.ing8 = QLineEdit(self)
        self.ing9 = QLineEdit(self)
        self.ing10 = QLineEdit(self)

        self.ing = [self.ing1, self.ing2, self.ing3, self.ing4, self.ing5, self.ing6, self.ing7,
                    self.ing8, self.ing9, self.ing10]

        self.list = QListWidget()
        data = data_reading.read_recipes(data_reading.RECIPES_FILE)
        data_reading.clean_ingredients(data)
        self.clean = list(data_reading.get_ingredients(data))
        for i in range(len(self.clean)):
            self.list.insertItem(i, self.clean[i])
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

        # data = data_reading.read_recipes(data_reading.RECIPES_FILE)
        # data_reading.clean_ingredients(data)
        # clean = list(data_reading.get_ingredients(data))
        testing = ['check', 'one', 'two', 'three', 'white pepper', 'blue pepper']
        completer = QCompleter(self.clean)
        completer.setFilterMode(Qt.MatchContains)

        self.ing1.setCompleter(completer)
        # self.ing1.setFixedSize(100, 50)
        # vbox.addWidget(self.ing1, alignment= Qt.Align)
        self.ing1.move(30, 100)

        self.ing2.setCompleter(completer)
        # self.ing2.setFixedSize(100, 50)
        self.ing2.move(30, 150)
        self.ing2.setDisabled(True)

        self.ing3.setCompleter(completer)
        self.ing3.move(30, 200)
        self.ing3.setDisabled(True)

        self.ing4.setCompleter(completer)
        self.ing4.move(30, 250)
        self.ing4.setDisabled(True)

        self.ing5.setCompleter(completer)
        self.ing5.move(30, 300)
        self.ing5.setDisabled(True)

        self.ing6.setCompleter(completer)
        self.ing6.move(30, 350)
        self.ing6.setDisabled(True)

        self.ing7.setCompleter(completer)
        self.ing7.move(30, 400)
        self.ing7.setDisabled(True)

        self.ing8.setCompleter(completer)
        self.ing8.move(30, 450)
        self.ing8.setDisabled(True)

        self.ing9.setCompleter(completer)
        self.ing9.move(30, 500)
        self.ing9.setDisabled(True)

        self.ing10.setCompleter(completer)
        self.ing10.move(30, 550)
        self.ing10.setDisabled(True)


        self.max_add_label.move(3 * (self.width // 4) - 25, self.height // 4 - 50)
        self.max_add_label.resize(200, 20)
        self.max_time_label.move(3 * (self.width // 4) + 20, (self.height // 4) + 100)
        self.time.move(3 * (self.width // 4), (self.height // 4) + 130)

        # self.ing1.move(30, 75)
        # self.ing2.move(30, 100)
        # Figure out placement
        vbox = QVBoxLayout()
        vbox.setContentsMargins(225, 50, 100, 50)
        self.list.setFixedSize(250, 500)
        vbox.addWidget(self.list)
        self.setLayout(vbox)

        # Add button
        add = QPushButton("Add", self)
        add.move(3 * (self.width // 4), self.height // 4)
        add.clicked.connect(self.add)

        # Delete button
        remove = QPushButton("Remove", self)
        remove.move(3 * (self.width // 4), (self.height // 4) + 50)
        remove.clicked.connect(self.remove)

        label_test = QLabel('Text')
        label_test.move(50, 70)

        clear = QPushButton("Clear All", self)
        clear.move(3 * (self.width // 4), self.height + 25)
        clear.clicked.connect(self.clear)

        submit = QPushButton("Submit", self)
        submit.move(3 * (self.width // 4), self.height + 75)
        submit.clicked.connect(self.submit)

        self.show()

    def add(self):
        for x in range(len(self.ing) - 1, 0, -1):
            if self.ing[x - 1].isEnabled():
                self.ing[x].setDisabled(False)

    def remove(self):
        for x in self.ing[::-1][:-1]:
            if x.isEnabled():
                x.setDisabled(True)
                x.clear()
                return
        # if self.ing10.isEnabled():
        #     self.ing10.setDisabled(True)
        #     self.ing10.clear()
        # elif self.ing9.isEnabled():
        #     self.ing9.setDisabled(True)
        #     self.ing9.clear()
        # elif self.ing8.isEnabled():
        #     self.ing8.setDisabled(True)
        #     self.ing8.clear()
        # elif self.ing7.isEnabled():
        #     self.ing7.setDisabled(True)
        #     self.ing7.clear()
        # elif self.ing6.isEnabled():
        #     self.ing6.setDisabled(True)
        #     self.ing6.clear()
        # elif self.ing5.isEnabled():
        #     self.ing5.setDisabled(True)
        #     self.ing5.clear()
        # elif self.ing4.isEnabled():
        #     self.ing4.setDisabled(True)
        #     self.ing4.clear()
        # elif self.ing3.isEnabled():
        #     self.ing3.setDisabled(True)
        #     self.ing3.clear()
        # elif self.ing2.isEnabled():
        #     self.ing2.setDisabled(True)
        #     self.ing2.clear()

    def clear(self):
        for x in self.ing:
            x.clear()
            if x != self.ing1:
                x.setDisabled(True)
        self.time.clear()

    def submit(self):
        if any([x.isEnabled() and x.text() == '' for x in self.ing]):
            # self.submit.setStyleSheet("border :2px solid ;"
            #                      "border-top-color : red; "
            #                      "border-left-color : red;"
            #                      "border-right-color : red;"
            #                      "border-bottom-color : red")
            warning = QMessageBox()
            warning.setWindowTitle("Error")
            warning.setText('Did not fill all the needed information')
            warning.setIcon(QMessageBox.Critical)
            x = warning.exec_()
        elif not all([x.text() in self.clean for x in self.ing if x.isEnabled()]):
            invalid = QMessageBox()
            invalid.setWindowTitle("Error")
            invalid.setText('One or more of the ingredients are invalid')
            invalid.setIcon(QMessageBox.Critical)
            x = invalid.exec_()
        else:
            print(type(self.time.text()))
            if self.time.text() == '0':
                next_page = QMessageBox()
                next_page.setWindowTitle("Next")
                next_page.setText('You did not set your time, would you still like to submit?')
                next_page.setIcon(QMessageBox.Question)
                # next_page.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
                x = next_page.exec_()

    # def third_page(self, i):
    #     if i == "Yes":


    def center(self):  # Used top center the window on the desktop
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
