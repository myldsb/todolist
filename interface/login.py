import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from interface.main import Main
from controller import my_widget

Height = 800
Weight = 1500
Title = "ToDoList"

@my_widget.cache
class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(Weight, Height)
        self.setWindowTitle(Title)
        self.u_h_box = HBox("Username")
        self.p_h_box = HBox("Password")
        self.btn_h_box = BtnBox()
        self.h_box = QVBoxLayout()
        self.h_box.addLayout(self.u_h_box)
        self.h_box.addLayout(self.p_h_box)
        self.h_box.addLayout(self.btn_h_box)
        self.all_box = QVBoxLayout()

        self.all_box.addLayout(self.h_box)

        self.setLayout(self.all_box)
        self.show()


class HBox(QHBoxLayout):

    def __init__(self, line_text):
        super().__init__()
        u_label = QLabel(line_text)
        # u_label.setMinimumSize(200, 30)
        u_label.setAlignment(QtCore.Qt.AlignHCenter)
        u_edit = QLineEdit()
        # u_edit.setMinimumSize(200, 30)
        self.addStretch(1)
        self.addWidget(u_label)
        self.addWidget(u_edit)
        self.addStretch(1)


class BtnBox(QHBoxLayout):

    def __init__(self):
        super().__init__()
        login_btn = QPushButton("Log in")
        # login_btn.setMinimumSize(200, 30)
        siginin_btn = QPushButton("sign in")
        # siginin_btn.setMinimumSize(200, 30)
        self.addStretch(1)
        self.addWidget(login_btn)
        self.addWidget(siginin_btn)
        self.addStretch(1)

        login_btn.clicked.connect(lambda: my_widget.switch("Login", "Main"))
