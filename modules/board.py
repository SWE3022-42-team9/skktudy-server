import util.db as db
from util.error_object import ErrorObject

# /board
def board_list(uid: str, offset: int, limit: int) -> dict | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   offset: int
    #   limit: int
    # returns:
    #   dict | ErrorObject: board_list | ErrorObject
    # --------------------------------------------------
    # DB에서 ID 역순으로 offset부터 limit개의 게시판 목록 반환

    # 게시판 목록이 비었다면
        # 게시판 갯수 반환
        
        # offset이 게시판 갯수보다 크다면
            # ErrorObject 반환(404)

    # return 게시판 목록
    pass

# /board/{BOARD_ID}
def board_get(uid: str, board_id: int, offset: int, limit: int) -> dict | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   board_id: int
    #   offset: int
    #   limit: int
    # returns:
    #   dict | ErrorObject: board_info | ErrorObject
    # --------------------------------------------------
    # DB에서 board_id로 지정된 board의 metadata 반환
    
    # 결과가 없다면
        # return ErrorObject(404)
    
    # DB에서 board_id로 지정된 board의 post 중 ID 역순으로 offset부터 limit개의 게시글 목록 반환
    
    # 게시글 목록이 없다면
        # 게시글 갯수 반환
        
        # offset이 게시글 갯수보다 크다면
            # return ErrorObject(404)
    
    # return 게시판 정보
    pass