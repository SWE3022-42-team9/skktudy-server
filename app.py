from flask import Flask, render_template, request

from modules.auth import auth
from modules.board import *
from modules.post import *
from modules.comment import *
from modules.chatbot import *

from util.error_object import ErrorObject

def get_uid() -> str | ErrorObject:
    token = request.headers.get('Authorization') # Bearer xxx
    if token is None: # Token이 없음
        return ErrorObject(401, 'No authorization token')
    
    try:
        token = token.split(' ')[1]
    except: # Token 형태 이상
        return ErrorObject(401, 'Invalid token format')
    
    return auth(token)

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
def board():
  pass

@app.route('/board/<board_id>')
def board_id(board_id: str):
  pass

@app.route('/post/<post_id>')
def post_id(post_id: str):
  pass

@app.route('/post/upload')
def post_upload():
  pass

@app.route('/post/like')
def post_like():
  pass

@app.route('/comment/upload')
def comment_upload():
  pass

@app.route('/comment/delete')
def comment_delete():
  pass

@app.route('/comment/like')
def comment_like():
  pass

@app.route('/chatbot/send')
def chatbot_send():
  pass

@app.route('/chatbot/log')
def chatbot_log():
  pass

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
