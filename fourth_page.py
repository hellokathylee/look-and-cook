# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QWidget, QDesktopWidget, \
    QMainWindow, QPushButton, QCompleter, QLineEdit, QListWidget, QListView, QHBoxLayout, QAction, \
    QMessageBox, QSpinBox
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QDoubleValidator, QValidator, QIcon
import data_reading, third_page
import urllib


class IndividualRecipe(QDialog, QWidget):
    def __init__(self):
        super().__init__()

        # self.third_page = None

        self.selected_recipe = QLineEdit()  # get recipe id, if possible
        self.data = data_reading.read_recipes(data_reading.RECIPES_FILE)
        data_reading.clean_ingredients(self.data)

        # self.ingredient = QLabel("Ingredients", self)
        # self.ingredient.move(30, 50)
        # self.recipe_name = QLabel("Max number of ingredients ", self)

        # self.time = QLabel("Max time", self)

        # self.author = QLabel("All Ingredients", self)
        # self.author.move(300, 25)

        # self.time = QSpinBox(self)
        # self.time.setRange(0, 50000)

        # self.ing1 = QLineEdit(self)
        # self.ing2 = QLineEdit(self)
        # self.ing3 = QLineEdit(self)
        # self.ing4 = QLineEdit(self)
        # self.ing5 = QLineEdit(self)
        # self.ing6 = QLineEdit(self)
        # self.ing7 = QLineEdit(self)
        # self.ing8 = QLineEdit(self)
        # self.ing9 = QLineEdit(self)
        # self.ing10 = QLineEdit(self)
        #
        # self.ing = [self.ing1, self.ing2, self.ing3, self.ing4, self.ing5, self.ing6, self.ing7,
        #             self.ing8, self.ing9, self.ing10]

        # self.list = QListWidget()
        # data = data_reading.read_recipes(data_reading.RECIPES_FILE)
        # data_reading.clean_ingredients(data)
        # self.clean = list(data_reading.get_ingredients(data))
        # for i in range(len(self.clean)):
        #     self.list.insertItem(i, self.clean[i])
        # self.list.setResizeMode(QListView_ResizeMode=)

        self.title = "Page 4"
        self.left = 500
        self.top = 200
        self.width = 700
        self.height = 450
        self.InitWindow()
        self.center()

        self.line_edit = None
        self.user_input = None

    def InitWindow(self):
        # self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        recipe_name = QLabel(f"{self.data[self.selected_recipe.text()][0]}", self)
        recipe_name.move(3 * (self.width // 4) - 25, self.height // 4 - 50)
        recipe_name.resize(200, 20)

        author = QLabel(f"{self.data[self.selected_recipe.text()][3]}", self)
        author.move(3 * (self.width // 4) - 25, self.height // 4 - 50)

        scores_dict = data_reading.get_review_scores("data/clean_reviews.csv")
        review_score = QLabel(f"{scores_dict[self.selected_recipe]}", self)
        review_score.move(3 * (self.width // 4) - 25, self.height // 4 - 50)

        url = self.data[self.selected_recipe.text()][2]
        pic_data = urllib.urlopen(url).read()
        picture = QLabel()
        pixmap = QPixmap()
        pixmap.loadFromData(pic_data)
        # icon = QIcon(pixmap)
        picture.setPixmap(pixmap)
        # picture = QLabel(f"{self.data[self.selected_recipe.text()][2]}", self)

        # add for loop or something to separate ings and directions
        recipe_ingredients = QLabel(f"{self.data[self.selected_recipe.text()][7]}", self)
        recipe_ingredients.setWordWrap(True)

        directions = QLabel(f"{self.data[self.selected_recipe.text()][8]}", self)
        directions.setWordWrap(True)

        # self.in

        # data = data_reading.read_recipes(data_reading.RECIPES_FILE)
        # data_reading.clean_ingredients(data)
        # clean = list(data_reading.get_ingredients(data))
        # testing = ['check', 'one', 'two', 'three', 'white pepper', 'blue pepper']
        # completer = QCompleter(self.clean)
        # completer.setFilterMode(Qt.MatchContains)
        # completer.setCaseSensitivity(Qt.CaseInsensitive)

        # self.ing1.setCompleter(completer)
        # self.ing1.move(30, 100)
        # self.ing1.setFixedSize(150, 30)
        #
        # height = 150
        # for x in self.ing[1:]:
        #     x.setCompleter(completer)
        #     x.move(30, height)
        #     x.setFixedSize(150, 30)
        #     x.setDisabled(True)
        #     height += 50

        # self.recipe_name.move(3 * (self.width // 4) - 25, self.height // 4 - 50)
        # self.recipe_name.resize(200, 20)
        # self.time.move(3 * (self.width // 4) + 20, (self.height // 4) + 100)
        # self.time.move(3 * (self.width // 4), (self.height // 4) + 130)

        # self.ing1.move(30, 75)
        # self.ing2.move(30, 100)
        # Figure out placement

        # vbox = QVBoxLayout()
        # vbox.setContentsMargins(225, 50, 100, 50)
        # self.list.setFixedSize(250, 500)
        # vbox.addWidget(self.list)
        # self.setLayout(vbox)

        # Add button
        # add = QPushButton("Add", self)
        # add.move(3 * (self.width // 4), self.height // 4)
        # add.clicked.connect(self.add)

        # Delete button
        # remove = QPushButton("Remove", self)
        # remove.move(3 * (self.width // 4), (self.height // 4) + 50)
        # remove.clicked.connect(self.remove)

        # label_test = QLabel('Text')
        # label_test.move(50, 70)

        review_button = QPushButton("Reviews", self)
        review_button.move(3 * (self.width // 4), self.height + 25)
        review_button.clicked.connect(self.user_reviews())

        submit = QPushButton("Submit", self)
        submit.move(3 * (self.width // 4), self.height + 75)
        submit.clicked.connect(self.submit)

        self.show()

    # def add(self):
    #     for x in range(len(self.ing) - 1, 0, -1):
    #         if self.ing[x - 1].isEnabled():
    #             self.ing[x].setDisabled(False)
    #
    # def remove(self):
    #     for x in self.ing[::-1][:-1]:
    #         if x.isEnabled():
    #             x.setDisabled(True)
    #             x.clear()
    #             return

    def user_reviews(self):
        # ask dana
        # how to open a new window
        reviews_dict = data_reading.get_reviews("data/reviews.csv")

        reviews = QLabel(f"{reviews_dict[self.selected_recipe]}", self)
        reviews.setWordWrap(True)

    # def submit(self):
    #     set_of_ing = set()
    #     duplicates = ''
    #     count = 0
    #     for x in self.ing:
    #         if x.isEnabled() and x.text() in set_of_ing:
    #             duplicates += x.text()
    #             count += 1
    #         else:
    #             set_of_ing.add(x.text())
    #
    #     if len(duplicates) != 0:
    #         contains_duplicates = QMessageBox()
    #         contains_duplicates.setWindowTitle("Error")
    #         if count == 1:
    #             contains_duplicates.setText(f'Ingredient {duplicates} appears more than once.')
    #         else:
    #             contains_duplicates.setText(f'Ingredients {duplicates} appear more than once.')
    #         contains_duplicates.setIcon(QMessageBox.Critical)
    #         x = contains_duplicates.exec_()
    #
    #     elif any([x.isEnabled() and x.text() == '' for x in self.ing]):
    #         # self.submit.setStyleSheet("border :2px solid ;"
    #         #                      "border-top-color : red; "
    #         #                      "border-left-color : red;"
    #         #                      "border-right-color : red;"
    #         #                      "border-bottom-color : red")
    #         warning = QMessageBox()
    #         warning.setWindowTitle("Error")
    #         warning.setText('Did not fill all the needed information.')
    #         warning.setIcon(QMessageBox.Critical)
    #         x = warning.exec_()
    #
    #     elif not all([x.text() in self.clean for x in self.ing if x.isEnabled()]):
    #         invalid_ingrdnt = ''
    #         count = 0
    #         for x in self.ing:
    #             if x.text() not in self.clean and x.isEnabled():
    #                 invalid_ingrdnt += x.text() + ', '
    #
    #                 count += 1
    #         invalid_ingrdnt = invalid_ingrdnt.strip(', ')
    #
    #         invalid = QMessageBox()
    #         invalid.setWindowTitle("Error")
    #         # invalid.setText('One or more of the ingredients are invalid')
    #         if count == 1:
    #             invalid.setText(f"The ingredient '{invalid_ingrdnt}' is invalid.")
    #         else:
    #             invalid.setText(f"The ingredients '{invalid_ingrdnt}' are invalid.")
    #         invalid.setIcon(QMessageBox.Critical)
    #         x = invalid.exec_()
    #
    #     else:
    #         self.hide()
    #         if self.third_page is None:
    #             # self.user_input = [x.text() for x in self.ing if x.isEnabled()]
    #             # self.third_page = third_page.Recipes()
    #             # temp= ''
    #             # for x in self.ing:
    #             #     if x.isEnabled():
    #             #         temp += x.text() +
    #             user_input = ','.join([x.text() for x in self.ing if x.isEnabled()])
    #             time = self.time.text()
    #             self.third_page.time.setText(time)
    #             self.third_page.inputs.setText(user_input)
    #             self.third_page.show()

    # if self.time.text() == '0':
    #     # next_page = QMessageBox()
    #     # next_page.setWindowTitle("Next")
    #     # next_page.setText('You did not specify the maximum time,'
    #     #                   ' would you still like to submit?')
    #     # next_page.setIcon(QMessageBox.Question)
    #     # next_page.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
    #     # # next_page.buttonClicked.connect(self.third_page)
    #
    #     check = QMessageBox.Question(self, 'testing', 'hopefully it works')
    #     # if check == QMessageBox.Yes:
    #     #     print('yay')

    # x = next_page.exec_()

    # def open(self):

    # def third_page(self, i):
    #     print(i.text())
    #     # if i == "Yes":
    #     #     self.hide()
    #     #     if self.third_page is None:
    #     #
    #     #         self.third_page = third_page.Recipes()
    #     #         self.third_page.show()

    def center(self):  # Used top center the window on the desktop
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
