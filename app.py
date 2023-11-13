from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robot():
    return '''User-Agent: *
Disallow: /
'''

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
