# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QWidget, QDesktopWidget, \
    QMainWindow, QPushButton, QCompleter, QLineEdit, QListWidget, QListView, QHBoxLayout, QAction, \
    QMessageBox, QSpinBox, QComboBox
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QDoubleValidator, QValidator, QStandardItemModel, QFont, \
    QStandardItem
import data_reading, sort_srch_rslts, second_page, data_type, fourth_page


class Recipes(QDialog, QWidget):
    def __init__(self, user_ingredients: list, time: int):
        """Class representing third window of program which displays the recipes filtered by the
        ingredients inputted by the user.

        Instance attributes:
            - #TODO
        """
        super().__init__()
        self.fourth_page = None
        self.user_ingredients = user_ingredients
        self.time = time

        self.ingredient = QLabel("Ingredients", self)
        self.ingredient.move(30, 50)
        self.max_add_label = QLabel("Max number of ingredients", self)

        self.all_label = QLabel("All Ingredients", self)
        self.all_label.move(300, 25)

        # self.time = QLineEdit()

        # self.given_time = QLineEdit()
        # print(self.given_time)

        # self.given_user_ing = QLineEdit()
        # print(self.given_user_i

        self.data = data_reading.read_recipes(data_reading.RECIPES_FILE)
        data_reading.clean_ingredients(self.data)
        self.graph = data_type.load_graph("data/clean_recipes.csv")
        self.sorted_recipes = sort_srch_rslts.ingrdnt_sort(self.data, self.user_ingredients,
                                                           self.graph)

        self.recipes = QListWidget()
        self.recipe_names = [x[1][0] for x in self.sorted_recipes]
        for i in range(len(self.recipe_names)):
            self.recipes.insertItem(i, self.recipe_names[i])

        self.chosen_recipe = QLineEdit(self)

        self.sort_by = QComboBox(self)
        self.sort_by.setFixedSize(100, 25)
        self.sort_by.addItem('Ingredient Sort')
        self.sort_by.addItem('Time Sort')
        # self.sort_by.addItem('Select')
        # self.sort_by.setCurrentText('(Select)')
        self.sort_by.move(100, 70)

        self.sort_time = QComboBox(self)
        self.sort_time.setFixedSize(100, 25)
        self.sort_time.addItem('Descending')
        self.sort_time.addItem('Ascending')
        self.sort_time.move(100, 100)
        self.sort_time.setDisabled(True)

        # self.sort_by.currentIndexChanged(self.manage_time())
        self.manage_time(self.sort_by.currentIndex())

        self.title = "Page 3"
        self.left = 500
        self.top = 200
        self.width = 700
        self.height = 450
        self.InitWindow()
        self.center()

    def InitWindow(self) -> None:
        """Open the third window on the user's screen with the provided dimensions.
        """
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        self.sort_by.currentIndexChanged.connect(self.sort)
        self.sort_by.currentIndexChanged.connect(self.manage_time)

        testing = ['check', 'one', 'two', 'three', 'white pepper', 'blue pepper']
        completer = QCompleter(self.recipe_names)
        completer.setFilterMode(Qt.MatchContains)
        completer.setCaseSensitivity(Qt.CaseInsensitive)

        self.chosen_recipe.setCompleter(completer)
        self.chosen_recipe.move(50, 200)
        self.chosen_recipe.setFixedSize(200, 30)

        choose = QPushButton("Choose", self)
        choose.move(3 * (self.width // 4), self.height + 75)
        choose.clicked.connect(self.choose)

        vbox = QVBoxLayout()
        vbox.setContentsMargins(225, 50, 100, 50)
        self.recipes.setFixedSize(250, 500)
        vbox.addWidget(self.recipes)
        self.setLayout(vbox)

        self.show()

    def sort(self, i: int) -> None:
        """Function to sort recipes by either time or number of ingredients inputted by the user
        utilized in the displayed recipes.

        Representation invariants:
            - i == 0 or i == 1 # TODO: not sure if this is correct
        """
        print('check')
        if i == 0:
            self.recipes.clear()
            sorted_recipes = sort_srch_rslts.ingrdnt_sort(self.data, self.user_ingredients,
                                                          self.graph)
            recipe_names = [x[1][0] for x in sorted_recipes]

            for i in range(len(recipe_names)):
                self.recipes.insertItem(i, recipe_names[i])
        else:
            self.sort_time.setDisabled(False)
            self.helper_time(False)

    def manage_time(self, i: int):  # ascending and descend
        print('test')
        if i == 0:
            print(i)
            self.helper_time(True)
            # descending
        else:
            print(i)
            self.helper_time(False)

    def helper_time(self, decreasing_order: bool = False):
        self.recipes.clear()
        timed_recipes = sort_srch_rslts.time_sort(self.sorted_recipes, self.data,
                                                  self.time,
                                                  decreasing_order)  # , False(increasing)

        recipe_names = [x[1][0] for x in timed_recipes]

        for i in range(len(recipe_names)):
            self.recipes.insertItem(i, recipe_names[i])

    def center(self) -> None:
        """Function to center third window on the provided desktop screen.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def choose(self):
        if self.chosen_recipe.text() == '' or self.chosen_recipe.text() not in self.recipe_names:
            warning = QMessageBox()
            warning.setWindowTitle("Error")
            warning.setText('The inputted information is incorrect.')
            warning.setIcon(QMessageBox.Critical)
            x = warning.exec_()
        else:
            self.hide()
            # self.fourth_page = fourth_page.IndividualRecipe(self.chosen_recipe.text())
            # self.fourth_page.show()

# # import PyQt5.QtWidgets as qtw
# # import PyQt5.QtGui as qtg
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QWidget, QDesktopWidget, \
#     QMainWindow, QPushButton, QCompleter, QLineEdit, QListWidget, QListView, QHBoxLayout, QAction, \
#     QMessageBox, QSpinBox, QComboBox
# from PyQt5.QtCore import Qt
# import sys
# from PyQt5 import QtGui
# from PyQt5.QtGui import QPixmap, QDoubleValidator, QValidator, QStandardItemModel, QFont, \
#     QStandardItem
# import data_reading, sort_srch_rslts, second_page, data_type
#
#
# class Recipes(QDialog, QWidget):
#     """Class representing third window of program which displays the recipes filtered by the
#     ingredients inputted by the user.
#
#     Instance attributes:
#         - #TODO
#     """
#     def __init__(self) -> None:
#         """Initialize an instance of the recipes window.
#         """
#         super().__init__()
#
#         self.ingredient = QLabel("Ingredients", self)
#         self.ingredient.move(30, 50)
#         self.max_add_label = QLabel("Max number of ingredients ", self)
#
#         self.all_label = QLabel("All Ingredients", self)
#         self.all_label.move(300, 25)
#
#         # self.ing = [self.ing1, self.ing2, self.ing3, self.ing4, self.ing5, self.ing6, self.ing7,
#         #             self.ing8, self.ing9, self.ing10]
#         #
#         # self.list = QListWidget()
#         # data = data_reading.read_recipes(data_reading.RECIPES_FILE)
#         # data_reading.clean_ingredients(data)
#         # self.clean = list(data_reading.get_ingredients(data))
#         # for i in range(len(self.clean)):
#         #     self.list.insertItem(i, self.clean[i])
#         # self.list.setResizeMode(QListView_ResizeMode=)
#         self.data = data_reading.read_recipes(data_reading.RECIPES_FILE)
#         data_reading.clean_ingredients(self.data)
#         self.graph = data_type.load_graph("data/clean_recipes.csv")
#
#         self.inputs = QLineEdit()
#         self.time = QLineEdit()
#         self.recipes = QListWidget()
#
#         self.sort_by = QComboBox(self)
#         self.sort_by.setFixedSize(100, 25)
#         self.sort_by.addItem('Ingredient Sort')
#         self.sort_by.addItem('Time Sort')
#         self.sort_by.move(100, 70)
#         self.sort_by.currentIndexChanged.connect(self.sort)
#
#         # self.sort_time = QComboBox(self)
#         # self.sort_time.setFixedSize(100, 100)
#         # self.sort_time.addItem('Descending')
#         # self.sort_time.addItem('Ascending')
#         # self.sort_time.move(100, 70)
#
#         self.title = "Page 3"
#         self.left = 500
#         self.top = 200
#         self.width = 700
#         self.height = 450
#         self.InitWindow()
#         self.center()
#
#     def InitWindow(self) -> None:
#         """Open the third window on the user's screen with the provided dimensions.
#         """
#         self.setGeometry(self.left, self.top, self.width, self.height)
#         self.setWindowTitle(self.title)
#
#         ingr_sort = QPushButton("Ingredient Sort", self)
#         ingr_sort.move(3 * (self.width // 4), self.height // 4)
#         ingr_sort.clicked.connect(self.sort)
#         # ingr_sort.setEnabled(False)
#
#         time_sort = QPushButton("Time Sort", self)
#         time_sort.move(2 * (self.width // 4), self.height // 4)
#         # time_sort.clicked.connect(self.manage_time)
#         # user_ingredients = self.inputs.text().split(',')
#         # sorted_recipes = sort_srch_rslts.ingrdnt_sort(self.data, user_ingredients, self.graph)
#         # # user_ingredients list
#         #
#         # recipe_names = [x[1][0] for x in sorted_recipes]
#         # for i in range(len(recipe_names)):
#         #     self.recipes.insertItem(i, recipe_names[i])
#
#         vbox = QVBoxLayout()
#         vbox.setContentsMargins(225, 50, 100, 50)
#         self.recipes.setFixedSize(250, 500)
#         vbox.addWidget(self.recipes)
#         #
#         # vbox.addWidget(self.sort_by)
#         self.setLayout(vbox)
#
#         self.show()
#
#     # def sort_by(self):
#     #     self.sort_time.clear()
#
#     def sort(self, i: int) -> None:
#         """Function to sort recipes by either time or number of ingredients inputted by the user
#         utilized in the displayed recipes.
#
#         Representation invariants:
#             - i == 0 or i == 1 # TODO: not sure if this is correct
#         """
#         if i == 0:
#             # data = data_reading.read_recipes(data_reading.RECIPES_FILE)
#             # data_reading.clean_ingredients(data)
#             # graph = data_type.load_graph("data/clean_recipes.csv")
#             user_ingredients = self.inputs.text().split(',')
#             sorted_recipes = sort_srch_rslts.ingrdnt_sort(self.data, user_ingredients, self.graph)
#             # user_ingredients list
#
#             recipe_names = [x[1][0] for x in sorted_recipes]
#
#             for i in range(len(recipe_names)):
#                 self.recipes.insertItem(i, recipe_names[i])
#         # else:
#             # # data = data_reading.read_recipes(data_reading.RECIPES_FILE)
#             # # data_reading.clean_ingredients(data)
#             # # graph = data_type.load_graph("data/clean_recipes.csv")
#             # # user_ingredients = self.inputs.text().split(',')
#             # timed_recipes = sort_srch_rslts.time_sort(self.data, self.time.text())
#             #
#             # recipe_names = [x[1][0] for x in timed_recipes]
#             #
#             # for i in range(len(recipe_names)):
#             #     self.recipes.insertItem(i, recipe_names[i])
#
#     def center(self) -> None:
#         """Function to center third window on the provided desktop screen.
#         """
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
