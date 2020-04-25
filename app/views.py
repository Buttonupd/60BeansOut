from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles')
def article():

    title = 'www.60BeansNows'
    return render_template('article.html', title=title)
    