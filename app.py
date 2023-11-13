from flask import Flask, render_template

from modules.board import *
from modules.post import *
from modules.comment import *
from modules.chatbot import *

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
