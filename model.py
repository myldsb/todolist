"""
model and init sql func.
"""

import sqlite3

from sqlalchemy import Column, VARCHAR, INTEGER, BOOLEAN, CHAR, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utils import current_time

Base = declarative_base()
engine = create_engine("sqlite:///todolist.db")
Session = sessionmaker(bind=engine)


class TodoList(Base):
    __tablename__ = 'todolist'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(255), nullable=False)
    body = Column(VARCHAR(255), nullable=False)
    time = Column(CHAR(16), nullable=False, default=current_time())
    send_email = Column(BOOLEAN, nullable=False, default=False)
    state = Column(BOOLEAN, nullable=False, default=False)
    remark = Column(VARCHAR(255), nullable=False, default="")
    owner = Column(INTEGER, ForeignKey("user.id"))

    user = relationship("User", back_populates="todolist")

class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(20), nullable=False, unique=True)
    passwd = Column(VARCHAR(36), nullable=False)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    isDeleted = Column(BOOLEAN, default=False, nullable=False)

    todolist = relationship("TodoList", order_by="-TodoList.id", back_populates="user")


def init_model():
    # the func that init the todolist.db when the __name__ is __main__
    conn = sqlite3.connect("todolist.db")
    cursor = conn.cursor()

    with open("schema.sql") as f:
        for sql in f.read().split(";"):
            cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_model()