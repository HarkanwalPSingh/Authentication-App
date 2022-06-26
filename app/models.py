from sqlalchemy import Column, String, Date, Integer
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String, unique = True)
    password = Column(String)
    registered_on = Column(Date)
