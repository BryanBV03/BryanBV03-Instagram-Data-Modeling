import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    userName = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    content = Column(String(200), nullable=False)
    url= Column(String(250))
    post_id= Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(String(60), primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))



class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    description= Column(String(25000))
    user_id= Column(Integer, ForeignKey('user.id'))
    post_id= Column(Integer, ForeignKey('post.id'))    




class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('person.id'), nullable=False)
    followed_id = Column(Integer, ForeignKey('person.id'), nullable=False)

    follower = relationship("Person", foreign_keys=[follower_id])
    followed = relationship("Person", foreign_keys=[followed_id])


    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
