from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from flask import jsonify

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
                    .all()
        except SQLAlchemyError as e:
            session.rollback()
            res = e

    return res