from sqlalchemy import Boolean, Column, Integer, String

from db import DB_Base

class Todo(DB_Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)


# CREATE TABLE todo (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     title VARCHAR(30) NOT NULL,
#     description TEXT,
#     completed BOOLEAN NOT NULL DEFAULT 0
# );