from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # return "index.html"
    return render_template('index.html')


@app.route('/users/<string:username>')
def users(username):
    # return "<h1>hello %s</h1>" % username
    return render_template('users.html', uname=username)


@app.route('/user')
def user():
    return render_template('users.html')

@app.route('/form')
def form():
    # return "hello harry wang hahahah"
    return render_template('form.html')









if __name__ == '__main__':
    app.run()
