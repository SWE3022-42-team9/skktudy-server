from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

import os

from util.models import *

from typing import List

DB_URL = f"mysql+mysqlconnector://{os.environ.get('USER')}:{os.environ.get('PASSWORD')}@{os.environ.get('HOST')}:{os.environ.get('PORT')}/{os.environ.get('DATABASE')}?charset=utf8mb4&collation=utf8mb4_general_ci"

engine = create_engine(DB_URL) # TODO: Add database URL
Session = sessionmaker(bind=engine)

def _execute_sql(sql: str) -> dict | SQLAlchemyError:
    # TODO: Implement
    # parameters:
    #   sql: str
    # returns:
    #   dict | SQLAlchemyError: result | error
    session = Session()
    
    try:
        result = session.execute(sql)
        result_dict = [dict(r) for r in result]
        session.commit()
        return result_dict
    
    except SQLAlchemyError as e:
        session.rollback()
        return e
    
    finally:
        session.close()
# --------------------------------------------------

# etc.

# post_id에 해당하는 post가 존재하는지 확인
def is_post_exist(post_id: int) -> bool | SQLAlchemyError:
    res: bool | SQLAlchemyError
    
    with Session() as session:
        try:
            res = session.query(Post) \
                    .filter(Post.id == post_id) \
                    .first() is not None
        except SQLAlchemyError as e:
            session.rollback()
            res = e

    return res

def get_post_comments(post_id: int) -> dict | SQLAlchemyError:
    res: dict | SQLAlchemyError = {}

    with Session() as session:
        try:
            res = session.query(Post) \
                    .filter(Post.id == post_id) \
                    .first() \
                    .to_dict()
            
            res["comments"] = session.query(Comment) \
                    .filter(Comment.post_id == post_id) \
                    .order_by(Comment.id.desc()) \
                    .all()
        except SQLAlchemyError as e:
            session.rollback()
            res = e
            
    return res

# post_id에 해당하는 post에 uid가 좋아요를 눌렀는지 확인
def get_post_like(post_id: int, uid: str) -> bool | SQLAlchemyError:
    res: bool | SQLAlchemyError
    
    with Session() as session:
        try:
            res = session.query(PostLike) \
                    .filter(PostLike.post_id == post_id) \
                    .filter(PostLike.user_id == uid) \
                    .first() is not None
        except SQLAlchemyError as e:
            session.rollback()
            res = e
            
    return res

# post_id에 해당하는 post에 uid가 좋아요를 누름
def add_post_like(post_id: int, uid: str) -> bool | SQLAlchemyError:
    res: bool | SQLAlchemyError = False
    
    with Session() as session:
        try:
            session.add(PostLike(post_id=post_id, user_id=uid))
            session.commit()
            res = True
        except SQLAlchemyError as e:
            session.rollback()
            res = e
    
    return res
 
def get_board_metadata(board_id: int) -> Board | SQLAlchemyError | None:
    res: Board | SQLAlchemyError | None
    
    with Session() as session:
        try:
            res = session.query(Board) \
                    .filter(Board.id == board_id) \
                    .first()
        
        except SQLAlchemyError as e:
            session.rollback()
            res = e
    
    return res

# board_id로 지정된 board의 metadata와 offset과 limit으로 지정된 범위의 게시글 목록을 반환합니다
def get_board_posts(board_id: int, offset: int, limit: int) -> List[Post] | SQLAlchemyError:
    # get_board_metadata 호출 후 사용하기 때문에 board_id로 지정된 board가 존재한다고 가정합니다
    res: List[Post] | SQLAlchemyError
    
    with Session() as session:
        try:
            res = session.query(Post) \
                    .filter(Post.board_id == board_id) \
                    .order_by(Post.id.desc()) \
                    .offset(offset) \
                    .limit(limit) \
                    .all()
        
        except SQLAlchemyError as e:
            session.rollback()
            res = e

    return res

def get_board_posts_count(board_id: int) -> int | SQLAlchemyError:
    # get_board_metadata 호출 후 사용하기 때문에 board_id로 지정된 board가 존재한다고 가정합니다
    res: int | SQLAlchemyError
    
    with Session() as session:
        try:
            res = session.query(Post) \
                    .filter(Post.board_id == board_id) \
                    .count()
        
        except SQLAlchemyError as e:
            session.rollback()
            res = e
    
    return res

# board_id에 해당하는 board가 존재하는지 확인
def is_board_exist(board_id: int) -> bool | SQLAlchemyError:
    res: bool | SQLAlchemyError
    
    with Session() as session:
        try:
            res = session.query(Board) \
                    .filter(Board.id == board_id) \
                    .first() is not None
        except SQLAlchemyError as e:
            session.rollback()
            res = e

    return res