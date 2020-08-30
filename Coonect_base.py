#создание бд
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from main import Base,Item
engine=create_engine("sqlite:///C:\\Users\\Win10Pro\\PycharmProjects\\base_train_1\\tasks.db", echo=True)#путь до бд.апи (какой диалект используем)
Base.metadata.create_all(engine)# создаём саму базу по лекалу в мейне
Session=sessionmaker(bind=engine)#механизм для обращения к бд, поддерживает транзакции(если одно обращение успешно, то гарантирует что все остальные успешно)
s=Session()
# t=Item(321,"Миша","У",1)#описывается команда
# s.add(t)#добавляется в базу

# t=s.query(Item).first()#запрос к таблице
# print(t)#вывод через принт
k=s.query(Item).filter(Item.uid==123).first()# находим, что меняем и меняем одно на другое //в first указываем limit
k.name="Петя"#задаём что меняем

t=s.query(Item).all()#запрос к таблице all для всего
a=0
for i in t:
    a+=i.ball#суммирование в цикле
    print(i)#вывод через принт всё
print(a)#суммируем баллы

n=s.query(func.sum(Item.ball)).first()#суммирование в запросе
print(n)

s.commit()# принять все изменения который были до сих пор