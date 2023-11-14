from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from models import *

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

# offset과 limit으로 지정된 범위의 Board의 목록을 반환합니다
def get_board_list(offset: int, limit: int) -> List[Board] | SQLAlchemyError:
    res: List[Board] | SQLAlchemyError
    
    with Session() as session:
        try:
            res = session.query(Board) \
                    .order_by(Board.id.asc()) \
                    .limit(limit) \
                    .offset(offset) \
                    .all()
        
        except SQLAlchemyError as e:
            session.rollback()
            res = e
    
    return res

# Board의 전체 갯수를 반환합니다
def get_board_list_size() -> int | SQLAlchemyError:
    count: int | SQLAlchemyError
    
    with Session() as session:
        try:
            count = session.query(Board).count()
        
        except SQLAlchemyError as e:
            session.rollback()
            count = e
    
    return count