import util.db as db
from util.error_object import ErrorObject

# /comment/upload
def comment_upload(comment: str, user_id: str, post_id: int) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   comment: str
    #   user_id: str
    #   post_id: int
    # returns:
    #   int | ErrorObject: comment_id | ErrorObject
    

# /comment/delete
def comment_delete(comment_id: int, user_id: str) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   comment_id: int
    #   user_id: str
    # returns:
    #   int | ErrorObject: comment_id | ErrorObject
    

# /comment/like
def comment_like(comment_id: int, user_id: str) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   comment_id: int
    #   user_id: str
    # returns:
    #   int | ErrorObject: comment_id | ErrorObject

    # 해당하는 comment_id가 있는지 체크
    comment_exist_chk_sql = f"SELECT 1 FROM comment WHERE id = {comment_id}"
    
    try:
        comment_exists = db._execute_sql(comment_exist_chk_sql)
        
        if not comment_exists:
            return ErrorObject(404, "Comment does not exist")
        
    except SQLAlchemyError as e:
        return ErrorObject(500, "Internal Server Error")
    
    add_like_sql = f"INSERT INTO comment_like (comment_id, user_id) VALUES ({comment_id}, {user_id})"
    
    try:
        comment_add = db._execute_sql(add_like_sql)
        return comment_id # 성공시 comment_id 반환
    
    except IntegrityError: # Composite key 조건 위배(like duplication)
        return ErrorObject(403, "Like duplicated")
    
    except SQLAlchemyError as e: # 서버 내부 오류
        return ErrorObject(500, "Internal Server Error")   