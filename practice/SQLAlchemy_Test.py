from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+pymysql://root@localhost:3306/olimpiadas', pool_recycle=3600, echo=True)

engine.connect()


Base = declarative_base()

t = Table('mytable', metadata,
  Column('id', Integer, primary_key=True),
  Column('descipcion', String),
  Column('tipo_sens', String),
  Column('valor', Integer)
  )

t.create()


"""
t = Table(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
    return "<User(name='%s', fullname='%s', password='%s')>" % (
        self.name, self.fullname, self.password)
"""
