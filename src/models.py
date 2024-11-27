from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from datetime import datetime
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=True)
    email = Column(String(100), nullable=False, unique=True)
    posts = relationship('Post', back_populates='user')
    followers = relationship('Follower', foreign_keys='Follower.user_to_id', back_populates='followed')
    following = relationship('Follower', foreign_keys='Follower.user_from_id', back_populates='follower')

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    follower = relationship('User', foreign_keys=[user_from_id], back_populates='following')
    followed = relationship('User', foreign_keys=[user_to_id], back_populates='followers')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='posts')

# Aquí también puedes agregar las tablas Media y Comment si aún no están.

## Generar el diagrama
try:
    result = render_er(Base, 'diagram.png')
    print("¡Diagrama generado exitosamente! Revisa el archivo diagram.png")
except Exception as e:
    print("Hubo un problema al generar el diagrama")
    raise e