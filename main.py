"""CSC111 Winter 2021 Project Phase 2: Final Submission, Main Program Window (1)

Description
===============================
This Python module contains the visualization of the main title program window.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of TAs and professors
teaching CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Dana Al Shekerchi, Nehchal Kalsi, Kathy Lee, and Audrey Yoshino.
"""
# import PyQt5.QtWidgets as qtw TODO remove this and the following???
# import PyQt5.QtGui as qtg
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QWidget, QDesktopWidget, \
    QPushButton  # QMainWindow TODO remove???
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QIcon, QFont
import second_page

# TEAL = rgb(35, 87, 77) TODO remove before submitting
# CORAL = rgb(211, 104, 80)
# YELLOW = rgb(210, 146, 68)
# MINT = rgb(35, 87, 77)
# PINK = rgb(224, 182, 157)
# BEIGE = rgb(240, 225, 204)


class MainWindow(QDialog, QWidget):
    """Opens the initial starting window for Look and Cook.

    Contains the logo, start button, and code to handle a click event.
    """
    def __init__(self) -> None:
        """Initialize an instance of MainWindow.
        """
        super().__init__()
        self.title = "Look and Cook"
        self.left = 500
        self.top = 200
        self.width = 700
        self.height = 700
        self.init_window()
        self.center()
        self.second_page = None
        self.setFixedSize(700, 700)
        self.setStyleSheet("background-color: rgb(240, 225, 204)")
        self.setWindowIcon(QIcon('visuals/L&C Icon.PNG'))
    # self.setWindowTitle("Look and Cook")  # Setting a title for the window

    # # To make a label
    # label = qtw.QLabel("hi")
    # # Change Size
    # label.setFont(qtg.QFont("Helvetica", 18))
    # self.layout().addWidget(label)

    def center(self) -> None:
        """Center MainWindow on the provided desktop screen.
       """
        # Creates a window in the center of the screen using the screen size
        frame = self.frameGeometry()
        window = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(window)
        self.move(frame.topLeft())

    def init_window(self) -> None:
        """Open the main window on the user's screen with the provided dimensions.
        """
        # Sets up screen
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        vbox = QVBoxLayout()
        # for title image
        image = QLabel()
        pixmap = QPixmap("visuals/L&C Logo.png").scaled(500, 500, 1)
        image.setPixmap(pixmap)

        vbox.addWidget(image, alignment=Qt.AlignCenter)

        # Start button
        btn_start = QPushButton("Start!", self)
        btn_start.setGeometry((self.width // 2) - 50, self.height // 2 + 200, 100, 100)
        btn_start.move((self.width // 2) - 50, self.height // 2 + 200)
        btn_start.setStyleSheet("border-radius: 50; background-color: rgb(210, 146, 68); "
                                "color: rgb(240, 225, 204)")
        btn_start.setFont(QFont('Georgia', 12, weight=QtGui.QFont.Bold))

        btn_start.clicked.connect(self.clicked)

        self.setLayout(vbox)
        self.show()  # Opens the window

    def clicked(self) -> None:
        """Link the start button to the second window displaying ingredient choices.
        """
        self.hide()
        # mydialog = QDialog(self)
        # mydialog = QDialog(self)
        # # mydialog.setModal(True)
        # # mydialog.exec_()
        # # Copied it from center, figure out why it didn't work before
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
            self.second_page = second_page.Ingredients()
            self.second_page.show()
            # self.second_page.activate

            #        mydialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['E1136'],
        'extra-imports': ['data_type'],
        'max-nested-blocks': 4
    })
