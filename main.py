from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean
Base=declarative_base()
#Base.metadata.create_all(engine)# подгружает бд
class Item(Base):#рассказываем про бд, какого будет формата и что содержать
    __tablename__ = "tasks"
    uid = Column(Integer,primary_key=True)#уникальный ключ primary_key- говорим что у каждой записи,что у каждой записи уникальный id,
    # если его нет, то мы не сможем добавить в бд нового человека
    name=Column(String(50))
    status=Column(String(50))
    ball=Column(Integer)
    def __init__(self,uid,name,status,ball):
        self.uid=uid
        self.name=name
        self.status=status
        self.ball=ball
    def __str__(self):#для вывода
        return f'{self.uid} {self.name.lower()} {self.status.lower()} {self.ball}'