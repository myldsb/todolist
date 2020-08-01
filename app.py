import sys

from PyQt5.QtWidgets import QApplication

# the my_widget will init at first, so there is it though it won't be used.
from controller import my_widget
from interface.window import Window


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())