import util.db as db
from util.error_object import ErrorObject

import firebase_admin
from firebase_admin import credentials, auth
import os

cred = credentials.Certificate(os.environ.get('FIREBASE_CREDS_PATH')) # TODO: Add Firebase Admin SDK JSON file path
firebase_admin.initialize_app(cred)

# 토큰 인증
def authenticate(token: str) -> str | ErrorObject:
    # TODO: Implement
    # parameters:
    #   token: str
    # returns:
    #   str | ErrorObject: uid | ErrorObject
    # --------------------------------------------------
    # DB에서 token에 대한 uid 반환
    uid = db.get_uid_from_token(token)
    if isinstance(uid, db.SQLAlchemyError):
        return ErrorObject(503, "DB Error: " + uid._message())
    
    # DB에 token이 없다면
    if uid is None:
        # _renew() 호출해서 uid 반환
        decoded_token = _renew(token)
        
        # uid가 ErrorObject라면
        if isinstance(decoded_token, ErrorObject):
            # return ErrorObject
            return decoded_token
        
        exists = db.is_user_exist(decoded_token['uid'])
        if isinstance(exists, db.SQLAlchemyError):
            return ErrorObject(503, "DB Error: " + exists._message())
        
        # uid가 DB에 없다면
        if not exists:
            # DB에 uid 및 token 정보로 데이터 생성
            result = db.add_user(decoded_token['uid'], decoded_token['name'], token)
            if isinstance(result, db.SQLAlchemyError):
                return ErrorObject(503, "DB Error: " + result._message())
        else:
            # DB에 uid 및 token 정보로 데이터 갱신
            result = db.update_user(decoded_token['uid'], decoded_token['name'], token)
            if isinstance(result, db.SQLAlchemyError):
                return ErrorObject(503, "DB Error: " + result._message())

    # return uid
    return uid

# token에 해당하는 uid를 반환
def _renew(token: str) -> dict | ErrorObject:
    # TODO: Implement
    # parameters:
    #   token: str
    # returns:
    #   str | ErrorObject: uid | ErrorObject
    # --------------------------------------------------
    try:
    # Firebase에 token을 전송하여 uid값 반환
        decoded_token = auth.verify_id_token(token)
        
        return decoded_token
    
    except Exception as e:
        return ErrorObject(503, "Firebase Error: " + str(e))
    # uid가 없다면
        # return ErrorObject
    
    # uid가 있다면
        # return uid