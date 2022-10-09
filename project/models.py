from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models, db


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)

class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)

class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    trailer = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(String(100), nullable=False)
    genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'))
    director_id = Column(Integer, ForeignKey(f'{Director.__tablename__}.id'))
    genre = relationship('Genre')
    director = relationship('Director')

#внешний ключ добавил
#убрал
class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=False, nullable=False)
    password = Column(String(500), nullable=False)
    name = Column(String(100), unique=False, nullable=False)
    surname = Column(String(100))
    favorite_genre = Column(String(100))
    genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'))
    genre = relationship('Genre')



