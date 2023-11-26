from flask import jsonify

import util.db as db
from util.error_object import ErrorObject

# /board
def board_list(offset: int, limit: int) -> dict | ErrorObject:
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
        return ErrorObject(500, 'DB Error: ' + str(board_list))

    # 게시판 목록이 비었다면
    if len(board_list) == 0:
        # 게시판 갯수 반환
        board_size = db.get_board_list_size()
        if isinstance(board_size, db.SQLAlchemyError):
            return ErrorObject(500, 'DB Error: ' + str(board_size))
        
        # offset이 게시판 갯수보다 크다면
        if offset >= board_size and board_size != 0:
            # ErrorObject 반환(404)
            return ErrorObject(404, 'Out of range')
    
    data = []
    for board in board_list:
        data.append({
            'board_id': board.id,
            'course_name': board.course_name,
            'course_num': board.course_num,
            'professor': board.professor,
            'semester_year': board.semester_year,
            'semester_num': board.semester_num
        })

    # return 게시판 목록
    return jsonify(data=data)

# /board/{BOARD_ID}
def board_get(board_id: int, offset: int, limit: int) -> dict | ErrorObject:
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
        return ErrorObject(500, 'DB Error:' + str(metadata))
    
    # 결과가 없다면
    if metadata == None:
        # return ErrorObject(404)
        return ErrorObject(404, 'Board does not exist')
    
    # DB에서 board_id로 지정된 board의 post 중 ID 역순으로 offset부터 limit개의 게시글 목록 반환
    posts = db.get_board_posts(board_id, offset, limit)
    if isinstance(posts, db.SQLAlchemyError):
        return ErrorObject(500, 'DB Error:' + str(posts))
    
    # 게시글 목록이 없다면
    if len(posts) == 0:
        # 게시글 갯수 반환
        posts_count = db.get_board_posts_count(board_id)
        if isinstance(posts_count, db.SQLAlchemyError):
            return ErrorObject(500, 'DB Error:' + str(posts_count))
        
        # offset이 게시글 갯수보다 크다면
        if offset >= posts_count and posts_count != 0:
            # return ErrorObject(404)
            return ErrorObject(404, 'Out of range')
    
    data = {
        'board_id': metadata.id,
        'course_name': metadata.course_name,
        'course_num': metadata.course_num,
        'professor': metadata.professor,
        'semester_year': metadata.semester_year,
        'semester_num': metadata.semester_num
    }
    
    post_data = []
    for post in posts:
        post = post.tuple()
        post_data.append({
            'post_id': post[0].id,
            'title': post[0].title,
            'content': post[0].content,
            'image': post[0].image,
            'date': post[0].date.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'board_id': post[0].board_id,
            'user': post[1]
        })
    
    post_ids = [post['post_id'] for post in post_data]
    post_likes = db.get_post_like_counts(post_ids)
    if isinstance(post_likes, db.SQLAlchemyError):
        return ErrorObject(500, 'DB Error:' + str(post_likes))
    
    for i in range(len(post_data)):
        post_data[i]['likes'] = 0
    
    for i in range(len(post_likes)):
        like = post_likes[i].tuple()
        for j in range(len(post_data)):
            if post_data[j]['post_id'] == like[0]:
                post_data[j]['likes'] = like[1]

    # return 게시판 정보 및 게시글 목록
    return jsonify(metadata=data, posts=post_data)