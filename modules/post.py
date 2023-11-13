import util.db as db
from util.error_object import ErrorObject

# /post/{POST_ID}
def post_get(board_id: int, post_id: int) -> dict | ErrorObject:
    # TODO: Implement
    # parameters:
    #   board_id: int
    #   post_id: int
    # returns:
    #   dict | ErrorObject: post | ErrorObject
    pass

# /post/upload
def post_upload(post: str, user_id: str, board_id: int, image: str | None) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   post: str
    #   user_id: str
    #   board_id: int
    #   image: str | None
    # returns:
    #   int | ErrorObject: post_id | ErrorObject
    pass

# /post/like
def post_like(post_id: int, user_id: str) -> int | ErrorObject:
    # TODO: Implement
    # parameters:
    #   post_id: int
    #   user_id: str
    # returns:
    #   int | ErrorObject: post_id | ErrorObject
    pass