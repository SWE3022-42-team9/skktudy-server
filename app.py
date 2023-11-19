from flask import Flask, render_template, request

from modules.auth import auth
from modules.board import *
from modules.post import *
from modules.comment import *
from modules.chatbot import *

from util.error_object import ErrorObject

def get_uid(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization') # Bearer xxx
        if token is None: # Token이 없음
            return {"message": "No authorization token"}, 401
        
        try:
            token = token.split(' ')[1]
        except: # Token 형태 이상
            return {"message": "Invalid token format"}, 401
        
        uid = auth(token)
        if isinstance(uid, ErrorObject):
            return uid.get_response()
        
        return func(uid, *args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robot():
    return '''User-Agent: *
Disallow: /
'''

@app.route('/board', methods=['GET'])
@get_uid
def board(uid: str):
    pass

@app.route('/board/<board_id>', methods=['GET'])
@get_uid
def board_id(uid: str, board_id: str):
    try:
        if not board_id.isnumeric(): # 숫자가 아닌 board_id
            return {"message": "Board does not exist"}, 404
        
        board_id = int(board_id)
        
        offset = request.args.get('offset', -1, type=int)
        limit = request.args.get('limit', -1, type=int)
        
        if offset < 0 or limit < 0: # offset 또는 limit이 없거나 음수임
            return {"message": "Invalid range"}, 404
        
        result = board_get(uid, board_id, offset, limit)
        if isinstance(result, ErrorObject):
            return result.get_response()
        
        return result, 200
    except: # offset 또는 limit이 숫자가 아님
        return {"message": "Invalid range"}, 404

@app.route('/post/<post_id>', methods=['GET'])
@get_uid
def post_id(uid: str, post_id: str):
    try:
        if not post_id.isnumeric(): # 숫자가 아닌 post_id
            return {"message": "Post does not exist"}, 404
        
        post_id = int(post_id)
        
        result = post_get(uid, post_id)
        if isinstance(result, ErrorObject):
            return result.get_response()
        
        return result, 200
    except:
        return {"message": "Post does not exist"}, 404

@app.route('/post/upload', methods=['POST'])
@get_uid
def post_upload_(uid: str):
    title = request.args.get('title', '', type=str)
    content = request.args.get('content', '', type=str)
    board_id = request.args.get('board_id', type=int)
    image = request.args.get('image', None, type=str)
    
    if board_id is None:
        return {"message": "No board specified"}, 404
    
    if len(title) == 0 or len(content) == 0:
        return {"message": "Empty content"}, 404
    
    if image is not None and len(image) == 0:
        image = None
    
    result = post_upload(uid, title, content, board_id, image)
    if isinstance(result, ErrorObject):
        return result.get_response()
    
    return {"id": result}, 200

@app.route('/post/like', methods=['POST'])
@get_uid
def post_like_(uid: str):
    post_id = request.args.get('post_id', type=int)
    
    if post_id is None: # post_id가 없음
        return {"message": "No post specified"}, 404
    
    result = post_like(uid, post_id)
    if isinstance(result, ErrorObject):
        return result.get_response()
    
    return {"post_id": result}, 200

@app.route('/comment/upload', methods=['POST'])
@get_uid
def comment_upload_(uid: str):
    content = request.args.get('content', '', type=str)
    post_id = request.args.get('post_id', type=int)
    
    if post_id is None: # post_id가 없음
        return {"message": "No post specified"}, 404
    if len(content) == 0: # content가 없음
        return {"message": "Empty comment"}, 404
    
    result = comment_upload(uid, content, post_id)
    
    if isinstance(result, ErrorObject):
        return result.get_response()
    
    return {"id": result}, 200

@app.route('/comment/delete', methods=['POST'])
@get_uid
def comment_delete_(uid: str):
    comment_id = request.args.get('id', type=int)
    
    if comment_id is None: # comment_id가 없음
        return {"message": "No comment specified"}, 404
    
    result = comment_delete(uid, comment_id)
    if isinstance(result, ErrorObject):
        return result.get_response()
    
    return {}, 200

@app.route('/comment/like', methods=['POST'])
@get_uid
def comment_like_(uid: str):
    comment_id = request.args.get('id', type=int)
    
    if comment_id is None: # comment_id가 없음
        return {"message": "No comment specified"}, 404
    
    result = comment_like(uid, comment_id)
    if isinstance(result, ErrorObject):
        return result.get_response()
    
    return {}, 200

@app.route('/chatbot/send', methods=['POST'])
@get_uid
def chatbot_send(uid: str):
    pass

@app.route('/chatbot/log', methods=['GET'])
@get_uid
def chatbot_log(uid: str):
    pass

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
