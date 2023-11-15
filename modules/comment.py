import util.db as db
from util.error_object import ErrorObject
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

# /comment/upload
def comment_upload(uid: str, comment: str, post_id: int) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   comment: str
    #   post_id: int
    # returns:
    #   int | ErrorObject: comment_id | ErrorObject
    # --------------------------------------------------
    # DB에 post_id가 존재하는지 확인
    
    # post_id가 존재하지 않는다면
        # return ErrorObject(404)
    
    # post_id가 존재한다면
        # DB에 comment, user_id, post_id+α를 저장
        # return comment_id
    check_post_sql = f"SELECT 1 FROM comment WHERE id = {post_id}"
    
    try:
        post_exists = db._execute_sql(check_post_sql)
        
        if not post_exists:
            return ErrorObject(404, "Post does not exist")
        
        upload_comment_sql = f"INSERT INTO comment (content, date, post_id, user_id) VALUES ({comment}, {uid}, {post_id}, CURRENT_TIMESTAMP)"
        result = db._execute_sql(upload_comment_sql)
        return result.lastrowid
    
    except SQLAlchemyError as e:
        return ErrorObject(500, str(e))
        
    

# /comment/delete
def comment_delete(uid: str, comment_id: int) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   comment_id: int
    # returns:
    #   int | ErrorObject: comment_id | ErrorObject
    # --------------------------------------------------
    # DB에서 comment_id, user_id를 통해 comment 존재 확인
    
    # comment가 존재하지 않는다면
        # ErrorObject 반환(404)
        
    # comment가 존재한다면
        # 작성자와 user_id가 같다면
            # DB에서 comment 삭제
            # comment_id 반환
            
        # 작성자와 user_id가 다르다면
            # ErrorObject 반환(403)
    check_comment_sql = f"SELECT user_id FROM comment WHERE id = {comment_id}"
    
    try:
        comment = db._execute_sql(check_comment_sql)

        if not comment:
            return ErrorObject(404, "Comment does not exist")

        else:
            if comment['user_id'] == uid:
                delete_comment_sql = f"DELETE FROM comment WHERE id = {comment_id}"
                db._execute_sql(delete_comment_sql)
                return comment_id
            
            else:
                return ErrorObject(403, "User is not the author")
    
    except SQLAlchemyError as e:
        return ErrorObject(500, str(e))
    

# /comment/like
def comment_like(uid: str, comment_id: int) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   comment_id: int
    # returns:
    #   int | ErrorObject: comment_id | ErrorObject
    
    # --------------------------------------------------
    # comment_id가 존재하는지 확인
    
    # comment_id가 존재하지 않는다면
        # return ErrorObject(404)
    
    # DB에서 comment_id, user_id를 통해 좋아요 내역 확인
    
    # 좋아요 내역이 없다면
        # DB에 좋아요 내역 추가
        # return comment_id
    
    # 좋아요 내역이 있다면
        # return ErrorObject(403)



    # 해당하는 comment_id가 있는지 체크
    comment_exist_chk_sql = f"SELECT 1 FROM comment WHERE id = {comment_id}"
    
    try:
        comment_exists = db._execute_sql(comment_exist_chk_sql)
        
        if not comment_exists:
            return ErrorObject(404, "Comment does not exist")
        
    except SQLAlchemyError as e:
        return ErrorObject(500, "Internal Server Error")
    
    add_like_sql = f"INSERT INTO comment_like (comment_id, user_id) VALUES ({comment_id}, {uid})"
    
    try:
        comment_add = db._execute_sql(add_like_sql)
        return comment_id # 성공시 comment_id 반환
    
    except IntegrityError: # Composite key 조건 위배(like duplication)
        return ErrorObject(403, "Like duplicated")
    
    except SQLAlchemyError as e:
        return ErrorObject(500, str(e))
   