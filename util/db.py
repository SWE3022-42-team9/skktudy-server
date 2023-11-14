from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from models import *
from config import config

DB_URL = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset=utf8mb4&collation=utf8mb4_general_ci"

engine = create_engine(DB_URL) # TODO: Add database URL
Base.metadata.create_all(engine) #db 테이블 생성
Session = sessionmaker(bind=engine)

def _execute_sql(sql: str) -> dict | SQLAlchemyError:
    # TODO: Implement
    # parameters:
    #   sql: str
    # returns:
    #   dict | SQLAlchemyError: result | error
    session = Session()

    try:
        result = session.execute(text(sql))
        # select문인 경우 결과값 리턴
        if sql.split()[0].upper() == 'SELECT':
            result_dict = result.mappings().all()
        # select문이 아닌 경우 형식 통일을 위해 [] 리턴
        else:
            result_dict = []
            session.commit()
        return result_dict
    
    except SQLAlchemyError as e:
        session.rollback()
        return e
    
    finally:
        session.close()
# --------------------------------------------------

# etc.