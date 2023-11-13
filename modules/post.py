import util.db as db
from util.error_object import ErrorObject

# /post/{POST_ID}
def post_get(uid: str, board_id: int, post_id: int) -> dict | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   board_id: int
    #   post_id: int
    # returns:
    #   dict | ErrorObject: post | ErrorObject
    pass

# /post/upload
def post_upload(uid: str, post: str, board_id: int, image: str | None) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   post: str
    #   board_id: int
    #   image: str | None
    # returns:
    #   int | ErrorObject: post_id | ErrorObject
    pass

# /post/like
def post_like(uid: str, post_id: int) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    #   post_id: int
    # returns:
    #   int | ErrorObject: post_id | ErrorObject
    pass