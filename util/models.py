from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Board(Base):
    # TODO: Implement
    pass

class User(Base):
    # TODO: Implement
    pass

class Post(Base):
    # TODO: Implement
    pass

class Comment(Base):
    # TODO: Implement
    pass

class PostLike(Base):
    # TODO: Implement
    pass

class CommentLike(Base):
    # TODO: Implement
    pass