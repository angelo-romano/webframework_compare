from sqlalchemy import (
    create_engine, Column, Integer, String, Float, ForeignKey)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
engine = create_engine(
    'postgresql://angelo:ciaobella@localhost/trip2', echo=False)
Base = declarative_base(bind=engine)

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    wikiname = Column(String(96))
    slug = Column(String(32))
    name = Column(String(96))
    code = Column(String(5))
    currency = Column(String(32))

 
class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    wikiname = Column(String(96))
    slug = Column(String(32))
    name = Column(String(96))
    rankings_1 = Column(Float)
    rankings_2 = Column(Float)
    rankings_3 = Column(Float)
    rankings_4 = Column(Float)
    total_ranking = Column(Float)
    timezone = Column(String(16))
    latitude = Column(Float)
    longitude = Column(Float)
    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship('Country', backref=backref('cities', lazy='dynamic'))
