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

@app.route('/board')
@get_uid
def board(uid: str):
    try:
        offset = request.args.get('offset', -1, type=int)
        limit = request.args.get('limit', -1, type=int)
    
        if offset < 0 or limit < 0: # offset 또는 limit이 없거나 음수임
            return {"message": "Invalid range"}, 404
        
        result = board_list(uid, offset, limit)
        if isinstance(result, ErrorObject):
            return result.get_response()
        
        return result, 200
    except: # offset 또는 limit이 숫자가 아님
        return {"message": "Invalid range"}, 404

@app.route('/board/<board_id>')
@get_uid
def board_id(uid: str, board_id: str):
    pass

@app.route('/post/<post_id>')
@get_uid
def post_id(uid: str, post_id: str):
    pass

@app.route('/post/upload')
@get_uid
def post_upload(uid: str):
    pass

@app.route('/post/like')
@get_uid
def post_like(uid: str):
    pass

@app.route('/comment/upload')
@get_uid
def comment_upload(uid: str):
    pass

@app.route('/comment/delete')
@get_uid
def comment_delete(uid: str):
    pass

@app.route('/comment/like')
@get_uid
def comment_like(uid: str):
    pass

@app.route('/chatbot/send')
@get_uid
def chatbot_send(uid: str):
    pass

@app.route('/chatbot/log')
@get_uid
def chatbot_log(uid: str):
    pass

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
