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
    exists = db.is_post_exist(post_id)
    if isinstance(exists, db.SQLAlchemyError):
        return ErrorObject(500, "DB Error: " + str(exists))
    
    # post_id가 존재하지 않는다면
    if not exists:
        # return ErrorObject(404)
        return ErrorObject(404, "Post does not exist")
    
    # post_id가 존재한다면
    comment_id = db.upload_comment(uid, comment, post_id)
    if isinstance(comment_id, db.SQLAlchemyError):
        return ErrorObject(500, "DB Error: " + str(comment_id))
    
    return comment_id
        # DB에 comment, user_id, post_id+α를 저장
        # return comment_id
        
        
    # check_post_sql = f"SELECT 1 FROM post WHERE id = {post_id}"
    
    # try:
    #     post_exists = db._execute_sql(check_post_sql)
        
    #     if not post_exists:
    #         return ErrorObject(404, "Post does not exist") #해당 댓글을 달기 위한 post가 주어지지 않음
        
    #     upload_comment_sql = f"INSERT INTO comment (content, date, post_id, user_id) VALUES ({comment},  CURRENT_TIMESTAMP, {post_id}, {uid})"
    #     result = db._execute_sql(upload_comment_sql)
    #     return result.lastrowid
    
    # except SQLAlchemyError as e:
    #     return ErrorObject(500, str(e))
        
    

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
    comment = db.get_comment(comment_id)
    if isinstance(comment, db.SQLAlchemyError):
        return ErrorObject(500, "DB Error: " + str(comment))
    
    # comment가 존재하지 않는다면
    if not comment:
        # ErrorObject 반환(404)
        return ErrorObject(404, "Comment does not exist")
    
    if comment.user_id != uid:
        return ErrorObject(403, "User is not the author")
    
    result = db.delete_comment(comment_id)
    if isinstance(result, db.SQLAlchemyError):
        return ErrorObject(500, "DB Error: " + str(result))
    # comment가 존재한다면
        # 작성자와 user_id가 같다면
            # DB에서 comment 삭제
            # comment_id 반환
            
        # 작성자와 user_id가 다르다면
            # ErrorObject 반환(403)
    
    return comment_id
    
    # check_comment_sql = f"SELECT user_id FROM comment WHERE id = {comment_id}"
    
    # try:
    #     comment = db._execute_sql(check_comment_sql)

    #     if not comment:
    #         return ErrorObject(404, "Comment does not exist") #ID로 지정된 댓글이 존재하지 않음

    #     else:
    #         if comment['user_id'] == uid:
    #             delete_comment_sql = f"DELETE FROM comment WHERE id = {comment_id}"
    #             db._execute_sql(delete_comment_sql)
    #             return comment_id
            
    #         else:
    #             return ErrorObject(403, "User is not the author") #삭제를 요청한 유저와 댓글의 작성자가 다름
    
    # except SQLAlchemyError as e:
    #     return ErrorObject(500, str(e))
    

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
    exist = db.is_comment_exist(comment_id)
    if isinstance(exist, db.SQLAlchemyError):
        return ErrorObject(500, "DB Error: " + str(exist))
    
    # comment_id가 존재하지 않는다면
    if not exist:
        # return ErrorObject(404)
        return ErrorObject(404, "Comment does not exist")
    
    # DB에서 comment_id, user_id를 통해 좋아요 내역 확인
    exist2 = db.get_comment_like(uid, comment_id)
    
    # 좋아요 내역이 없다면
    if not exist2:
        # DB에 좋아요 내역 추가
        db.add_comment_like(uid, comment_id)
        # return comment_id
        return comment_id
    
    return ErrorObject(403, "Like duplicated")
    
    # 좋아요 내역이 있다면
        # return ErrorObject(403)


    # 해당하는 comment_id가 있는지 체크
    # comment_exist_chk_sql = f"SELECT 1 FROM comment WHERE id = {comment_id}"
    
    # try:
    #     comment_exists = db._execute_sql(comment_exist_chk_sql)
        
    #     if not comment_exists:
    #         return ErrorObject(404, "Comment does not exist") #ID로 지정된 댓글이 존재하지 않음
        
    # except SQLAlchemyError as e:
    #     return ErrorObject(500, str(e))
    
    # add_like_sql = f"INSERT INTO comment_like (comment_id, user_id) VALUES ({comment_id}, {uid})"
    
    # try:
    #     comment_add = db._execute_sql(add_like_sql)
    #     return comment_id # 성공시 comment_id 반환
    
    # except IntegrityError: # Composite key 조건 위배(like duplication)
    #     return ErrorObject(403, "Like duplicated") # 이미 좋아요를 누른 댓글에 중복으로 좋아요를 시도
    
    # except SQLAlchemyError as e:
    #     return ErrorObject(500, str(e))
   