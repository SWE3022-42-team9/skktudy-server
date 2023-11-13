import util.db as db
from util.error_object import ErrorObject

# /comment/upload
def comment_upload(uid: str, comment: str, post_id: int) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   comment: str
    #   post_id: int
    # returns:
    #   int | ErrorObject: comment_id | ErrorObject
    pass

# /comment/delete
def comment_delete(uid: str, comment_id: int) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   comment_id: int
    # returns:
    #   int | ErrorObject: comment_id | ErrorObject
    pass

# /comment/like
def comment_like(uid: str, comment_id: int) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   comment_id: int
    # returns:
    #   int | ErrorObject: comment_id | ErrorObject
    pass