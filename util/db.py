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

def create_comment_like(new_comment_like: CommentLike) -> dict | SQLAlchemyError:
    res: dict | SQLAlchemyError
    
    res = {"message": "Comment like successfully"}
    with Session() as session:
        try:
            session.add(new_comment_like)
            session.commit()
        
        except SQLAlchemyError as e:
            session.rollback()
            res = e
    
    return res

#특정 댓글의 좋아요 수를 반환합니다.
def get_comment_likes_count(comment_id: int) -> int | SQLAlchemyError:
    res: int | SQLAlchemyError

    with Session() as session:
        try:
            res = session.query(CommentLike) \
                    .filter(CommentLike.comment_id == comment_id) \
                    .count()
        
        except SQLAlchemyError as e:
            session.rollback()
            res = e
    
    return res