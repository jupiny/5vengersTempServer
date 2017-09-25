from sqlalchemy import Column, Integer, String

from ovengers.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(20))
    step = Column(Integer, default=0)
    heart_rate = Column(Integer, default=0)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)
