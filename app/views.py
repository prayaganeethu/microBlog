from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Neethu'}
    posts = [{'author': {'nickname': 'Garima'}, 'body': 'It is an awesome day!'}, {
        'author': {'nickname': 'Manisha'}, 'body': 'Yaayyy, Whatss uppp!!!'}, {'author': {'nickname': 'Aiswarya'}, 'body': 'But whyyyyy!! :P'}]
    return render_template('index.html', title='Home', user=user, posts=posts)
