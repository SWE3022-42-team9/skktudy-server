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
    # --------------------------------------------------
    # DB에 post_id가 존재하는지 확인
    
    # post_id가 존재하지 않는다면
        # return ErrorObject(404)
    
    # post_id가 존재한다면
        # DB에 comment, user_id, post_id+α를 저장
        # return comment_id
    pass

# /comment/delete
def comment_delete(comment_id: int, user_id: str) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   comment_id: int
    #   user_id: str
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
    pass

# /comment/like
def comment_like(comment_id: int, user_id: str) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   comment_id: int
    #   user_id: str
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
    pass