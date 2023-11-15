from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from util.models import *

from typing import List

engine = create_engine('') # TODO: Add database URL
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