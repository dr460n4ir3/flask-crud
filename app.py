from flask import Flask , render_template
from data import Articles

app = Flask(__name__)
app.debug = True

Articles = Articles()

@app.route('/', methods=['GET'])
def login():
    #return "Hello Mack!!!!"
    return render_template('login.html')

@app.route('/home', methods=['GET'])
def homepage():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/articles', methods=['GET'])
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>', methods=['GET'])
def article(id):
    return render_template('article.html', id = id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)

