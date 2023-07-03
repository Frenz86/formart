from sqlalchemy import Column, Integer, String
from database import Base
 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    position = Column(String(150))
    office = Column(String(150))