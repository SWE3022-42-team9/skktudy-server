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
    # _renew() 호출해서 uid 및 name 반환
    decoded_data = _renew(token)
    
    # uid가 ErrorObject라면
    if isinstance(decoded_data, ErrorObject):
        # return ErrorObject
        return decoded_data
    
    uid, name = decoded_data
    
    if name is None:
        name = 'Anonymous ' + uid[:4]
    
    exists = db.is_user_exist(uid)
    if isinstance(exists, db.SQLAlchemyError):
        return ErrorObject(500, "DB Error: " + str(exists))
    
    # uid가 DB에 없다면
    if not exists:
        # DB에 uid 및 token 정보로 데이터 생성
        result = db.add_user(uid, name, '')
        if isinstance(result, db.SQLAlchemyError):
            return ErrorObject(500, "DB Error: " + str(result))
    else:
        # DB에 uid 및 token 정보로 데이터 갱신
        result = db.update_user(uid, name, '')
        if isinstance(result, db.SQLAlchemyError):
            return ErrorObject(500, "DB Error: " + str(result))

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
        
        user = auth.get_user(decoded_token['uid'])
        
        return decoded_token['uid'], user.display_name
    
    except Exception as e:
        return ErrorObject(500, "Firebase Error: " + str(e))
    # uid가 없다면
        # return ErrorObject
    
    # uid가 있다면
        # return uid