from datetime import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

from controller import my_widget
from model import User,TodoList, Session
from utils import current_time



@my_widget.cache
class Main(QWidget):

    def __init__(self):
        super().__init__()

        splitter = QSplitter(Qt.Horizontal)

        self.box = QHBoxLayout()
        splitter.addWidget(Tree())
        splitter.addWidget(Content())
        splitter.setStretchFactor(0, 2)
        splitter.setStretchFactor(1, 4)

        self.box.addWidget(splitter)
        self.setLayout(self.box)

class Content(QWidget):
    def __init__(self):
        super().__init__()
        box = QVBoxLayout()
        box.addWidget(Tab())
        # box.addStretch(1)
        btn = Btn("新增TODO")
        box.addWidget(btn)
        # box.addStretch(1)
        box.setSpacing(50)
        self.setLayout(box)

        btn.clicked.connect(self.add)

    def add(self):
        session = Session()
        todo = TodoList(title="", body="", time=current_time, owner=1)
        session.add(todo)
        table = my_widget.Table
        table.add_row(table.row, todo)
        session.commit()
        session.close()



class Btn(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("color: red;")


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


class Tab(QTabWidget):

    def __init__(self):
        super().__init__()

        self.calendar = Calendar()
        self.table = Table()

        self.addTab(self.calendar, "日历显示")
        self.addTab(self.table, "列表显示")

        self.resize(5500, 500)


@my_widget.cache
class Table(QTableWidget):
    _Fields = {'id':"id", '问题':"title", '详细描述':"body",
               '时间':"time", '过期未完成是否邮件提醒':"send_email",
               '完成状态':"state", '备注':"remark"}

    def __init__(self, ):
        self.init_table()

    def init_table(self):
        session = Session()
        print(dir(session))
        todolist = session.query(TodoList)

        self.row = 0

        super().__init__(todolist.count(), len(self._Fields))
        self.setHorizontalHeaderLabels(self._Fields)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        # hide the id column
        self.setColumnHidden(0, True)

        for i, record in enumerate(todolist.all()):
            self.add_row(i, record)
        session.close()

    def display(self):
        pass

    def add_row(self, r, item):
        self.setRowCount(self.row+1)
        for c, (k, v) in enumerate(self._Fields.items()):
            if k in ("过期未完成是否邮件提醒", "完成状态"):
                self.setCellWidget(r, c, Combobox(getattr(item, v)))
            else:
                self.setItem(r, c, QTableWidgetItem(getattr(item, v)))
        self.row += 1

    def del_item(self):
        pass

    def update_item(self):
        pass


class Combobox(QComboBox):
    def __init__(self, Yes: bool=False):
        super().__init__()

        self.addItems(['是', '否'])
        if Yes:
            self.setCurrentText('是')
        self.setCurrentText('否')


class Calendar(QCalendarWidget):

    def __init__(self):
        super().__init__()
        # box = QVBoxLayout()
        self.setGridVisible(True)
        # self.setLayout(box)
        # self.clicked[QDate].connect(self.showDate)
