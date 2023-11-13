import util.db as db
from util.error_object import ErrorObject

# 토큰 인증
def auth(token: str) -> str | ErrorObject:
    # TODO: Implement
    # parameters:
    #   token: str
    # returns:
    #   str | ErrorObject: uid | ErrorObject
    pass

# token에 해당하는 uid를 반환
def _renew(token: str) -> str | ErrorObject:
    # TODO: Implement
    # parameters:
    #   token: str
    # returns:
    #   str | ErrorObject: uid | ErrorObject
    pass