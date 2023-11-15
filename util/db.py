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

def create_comment(new_comment: Comment) -> dict | SQLAlchemyError:
    res: dict | SQLAlchemyError
    
    res = {"message": "Comment created successfully"}
    with Session() as session:
        try:
            session.add(new_comment)
            session.commit()
        
        except SQLAlchemyError as e:
            session.rollback()
            res = e
    
    return res