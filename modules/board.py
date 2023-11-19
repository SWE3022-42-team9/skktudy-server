from flask import jsonify

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
    board_list = db.get_board_list(offset, limit)
    if isinstance(board_list, db.SQLAlchemyError):
        return ErrorObject(503, 'DB Error: ' + board_list._message())

    # 게시판 목록이 비었다면
    if len(board_list) == 0:
        # 게시판 갯수 반환
        board_size = db.get_board_list_size()
        if isinstance(board_size, db.SQLAlchemyError):
            return ErrorObject(503, 'DB Error: ' + board_size._message())
        
        # offset이 게시판 갯수보다 크다면
        if offset >= board_size:
            # ErrorObject 반환(404)
            return ErrorObject(404, 'Out of range')

    # return 게시판 목록
    return jsonify(data=board_list)

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
    metadata = db.get_board_metadata(board_id)
    if isinstance(metadata, db.SQLAlchemyError):
        return ErrorObject(503, 'DB Error:' + metadata._message())
    
    # 결과가 없다면
    if metadata == None:
        # return ErrorObject(404)
        return ErrorObject(404, 'Board does not exist')
    
    # DB에서 board_id로 지정된 board의 post 중 ID 역순으로 offset부터 limit개의 게시글 목록 반환
    posts = db.get_board_posts(board_id, offset, limit)
    if isinstance(posts, db.SQLAlchemyError):
        return ErrorObject(503, 'DB Error:' + posts._message())
    
    # 게시글 목록이 없다면
    if len(posts) == 0:
        # 게시글 갯수 반환
        posts_count = db.get_board_posts_count(board_id)
        if isinstance(posts_count, db.SQLAlchemyError):
            return ErrorObject(503, 'DB Error:' + posts_count._message())
        
        # offset이 게시글 갯수보다 크다면
        if offset >= posts_count:
            # return ErrorObject(404)
            return ErrorObject(404, 'Out of range')
    
    # return 게시판 정보 및 게시글 목록
    return jsonify(metadata=metadata, posts=posts)