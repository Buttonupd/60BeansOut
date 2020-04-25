from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():
    sports_sources = get_sources('sports')
    print(sports_sources)
    title = '60BeansMade'


    return render_template('index.html', title=title, sports=sports_sources)

@app.route('/articles')
def article():
   

    title = 'www.60BeansNows'
    return render_template('article.html', title=title)
    