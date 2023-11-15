from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from models import *

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