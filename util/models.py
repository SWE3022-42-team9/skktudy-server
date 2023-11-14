from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, SmallInteger, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Board(Base):
    __tablename__ = 'board'
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    course_name = Column(String(100), nullable = False)
    course_num = Column(String(100), nullable = False)
    professor = Column(String(100), nullable = False)
    semester_year = Column(Integer, nullable = False)
    semester_num = Column(SmallInteger, nullable = False)

    posts = relationship('Post')

class User(Base):
    __tablename__ = 'user'
    
    id = Column(String(100), primary_key=True)
    token = Column(String(100), nullable = False)
    name = Column(String(100), nullable = False)

    posts = relationship('Post')
    comments = relationship('Comment')
    postlikes = relationship('PostLike')
    commentlikes = relationship('CommentLike')

class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String(100), nullable = False)
    content = Column(String(100), nullable = False)
    image = Column(String(100), nullable = True)
    date = Column(DateTime, nullable = False)
    
    board_id = Column(Integer, ForeignKey('board.id'), nullable = False)
    user_id = Column(String(100), ForeignKey('user.id'), nullable = False)

    comments = relationship('Comment')
    postlikes = relationship('PostLike')

class Comment(Base):
    __tablename__ = 'comment'
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    content = Column(String(100), nullable = False)
    date = Column(DateTime, nullable = False)
    
    post_id = Column(Integer, ForeignKey('post.id'), nullable = False)
    user_id = Column(String(100), ForeignKey('user.id'), nullable = False)

    commentlikes = relationship('CommentLike')

class PostLike(Base):
    __tablename__ = 'post_like'
    
    post_id = Column(Integer, ForeignKey('post.id'), nullable = False)
    user_id = Column(String(100), ForeignKey('user.id'), nullable = False)
    
    __table_args__ = (
        PrimaryKeyConstraint('post_id', 'user_id'),
    ) # Composite PK
    

class CommentLike(Base):
    __tablename__ = 'comment_like'
    
    comment_id = Column(Integer, ForeignKey('comment.id'), nullable = False)
    user_id = Column(String(100), ForeignKey('user.id'), nullable = False)
    
    __table_args__ = (
        PrimaryKeyConstraint('comment_id', 'user_id'),
    ) # Composite PK