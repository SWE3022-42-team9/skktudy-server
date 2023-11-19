from flask import jsonify

import util.db as db
from util.error_object import ErrorObject

# /post/{POST_ID}
def post_get(uid: str, post_id: int) -> dict | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   post_id: int
    # returns:
    #   dict | ErrorObject: post | ErrorObject
    # --------------------------------------------------
    # DB에 post_id가 존재하는지 확인
    exists = db.is_post_exist(post_id)
    if isinstance(exists, db.SQLAlchemyError):
        return ErrorObject(503, "DB Error: " + exists._message())
    
    # post_id가 존재하지 않는다면
    if not exists:
        # return ErrorObject(404)
        return ErrorObject(404, "Post does not exist")
        
    # post_id가 존재한다면
        # return DB에서 post_id로 지정된 post의 정보
    post = db.get_post_comments(post_id)
    if isinstance(post, db.SQLAlchemyError):
        return ErrorObject(503, "DB Error: " + post._message())
    
    return jsonify(post)

# /post/upload
def post_upload(uid: str, title: str, content: str, board_id: int, image: str | None) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   post: str
    #   board_id: int
    #   image: str | None
    # returns:
    #   int | ErrorObject: post_id | ErrorObject
    # --------------------------------------------------
    # DB에 board_id가 존재하는지 확인
    exists = db.is_board_exist(board_id)
    if isinstance(exists, db.SQLAlchemyError):
        return ErrorObject(503, "DB Error: " + exists._message())

    # board_id가 존재하지 않는다면
    if not exists:
        # return ErrorObject(404)
        return ErrorObject(404, "Board does not exist")
        
    # board_id가 존재한다면
        # DB에 post, user_id, board_id+α를 저장
        # return post_id
    try:
        upload_post_sql = f"INSERT INTO post (title, content, image, date, board_id, user_id) VALUES ({title}, {content}, {image}, CURRENT_TIMESTAMP, {board_id}, {uid})"
        result = db._execute_sql(upload_post_sql)
        return result.lastrowid
    
    except SQLAlchemyError as e:
        return ErrorObject(500, str(e))

# /post/like
def post_like(uid: str, post_id: int) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   post_id: int
    # returns:
    #   int | ErrorObject: post_id | ErrorObject
    # --------------------------------------------------
    # DB에서 post_id 존재하는지 확인
    exists = db.is_post_exist(post_id)
    if isinstance(exists, db.SQLAlchemyError):
        return ErrorObject(503, "DB Error: " + exists._message())
    
    # post_id가 존재하지 않는다면
    if exists is False:
        # return ErrorObject(404)
        return ErrorObject(404, "Post does not exist")
    
    # DB에서 post_id, user_id를 통해 좋아요 내역 확인
    dup = db.get_post_like(post_id, uid)
    if isinstance(dup, db.SQLAlchemyError):
        return ErrorObject(503, "DB Error: " + dup._message())
    
    # 좋아요 내역이 없다면
    if dup is False:
        # DB에 좋아요 내역 추가
        success = db.add_post_like(post_id, uid)
        if isinstance(success, db.SQLAlchemyError):
            return ErrorObject(503, "DB Error: " + success._message())
        # return post_id
        return post_id
    
    # 좋아요 내역이 있다면
        # return ErrorObject(403)
    return ErrorObject(403, "Like duplicated")