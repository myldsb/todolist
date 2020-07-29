from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from controller import my_widget

@my_widget.cache
class Main(QWidget):

    def __init__(self):
        super().__init__()

        splitter = QSplitter(Qt.Horizontal)

        self.box = QHBoxLayout()
        splitter.addWidget(Tree())
        splitter.addWidget(Calendar())
        splitter.setStretchFactor(0, 2)
        splitter.setStretchFactor(1, 4)

        self.box.addWidget(splitter)
        self.setLayout(self.box)


class Tree(QTreeWidget):

    def __init__(self):
        super().__init__()
        root = QTreeWidgetItem(self)


        all = QTreeWidgetItem()
        all.setText(0, "全部")
        done = QTreeWidgetItem()
        done.setText(0, "已完成")
        undo = QTreeWidgetItem()
        undo.setText(0, "待完成")

        root.addChildren([all, done, undo])

        self.addTopLevelItem(root)
        self.expandAll()


class Calendar(QCalendarWidget):

    def __init__(self):
        super().__init__()
        # box = QVBoxLayout()
        self.setGridVisible(True)
        # self.setLayout(box)
        # self.clicked[QDate].connect(self.showDate)
