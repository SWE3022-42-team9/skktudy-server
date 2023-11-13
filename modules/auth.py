import util.db as db
from util.error_object import ErrorObject

# 토큰 인증
def auth(token: str) -> str | ErrorObject:
    # TODO: Implement
    # parameters:
    #   token: str
    # returns:
    #   str | ErrorObject: uid | ErrorObject
    # --------------------------------------------------
    # DB에서 token에 대한 uid 반환
    
    # DB에 token이 없다면
        # _renew() 호출해서 uid 반환
        
        # uid가 ErrorObject라면
            # return ErrorObject
        
        # uid가 DB에 없다면
            # DB에 uid 및 token 정보로 데이터 생성

    # return uid
    pass

# token에 해당하는 uid를 반환
def _renew(token: str) -> str | ErrorObject:
    # TODO: Implement
    # parameters:
    #   token: str
    # returns:
    #   str | ErrorObject: uid | ErrorObject
    # --------------------------------------------------
    # Firebase에 token을 전송하여 uid값 반환
    
    # uid가 없다면
        # return ErrorObject
    
    # uid가 있다면
        # return uid
    pass