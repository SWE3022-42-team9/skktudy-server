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

# post_id로 지정된 post의 metadata를 반환합니다
def get_post_metadata(post_id: int) -> Post | SQLAlchemyError | None:
    res: Post | SQLAlchemyError | None
    
    with Session() as session:
        try:
            res = session.query(Post) \
                    .filter(Post.id == post_id) \
                    .first()
        
        except SQLAlchemyError as e:
            session.rollback()
            res = e
    
    return res

# post_id로 지정된 post의 댓글 목록을 반환합니다
def get_post_comments(post_id: int) -> List[Comment] | SQLAlchemyError:
    res: List[Comment] | SQLAlchemyError
    
    with Session() as session:
        try:
            res = session.query(Comment) \
                    .filter(Comment.post_id == post_id) \
                    .order_by(Comment.id) \
                    .all()
        
        except SQLAlchemyError as e:
            session.rollback()
            res = e

    return res