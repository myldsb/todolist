"""
the main box, switch the Login and Main in its central window
"""

import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from controller import my_widget
from interface.login import Login
from utils import static_for


Height = 800
Weight = 1500
Title = "ToDoList"

@my_widget.cache
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(Login())
        self.setWindowIcon(QIcon("./static/todo.ico"))
        self.resize(Weight,Height)
        self.setWindowTitle(Title)
        print(os.path.abspath(static_for("todo.ico")))
        # self.setWindowIcon(QIcon(static_for("./static/todo.ico")))
        self.show()
