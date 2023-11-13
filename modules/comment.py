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
    pass

# /comment/delete
def comment_delete(comment_id: int, user_id: str) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   comment_id: int
    #   user_id: str
    # returns:
    #   int | ErrorObject: comment_id | ErrorObject
    pass

# /comment/like
def comment_like(comment_id: int, user_id: str) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   comment_id: int
    #   user_id: str
    # returns:
    #   int | ErrorObject: comment_id | ErrorObject
    pass