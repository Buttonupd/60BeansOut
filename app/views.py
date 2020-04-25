from flask import render_template
from app import app
from .request import get_sources
from .models import news
News = news.News

@app.route('/')
def index():
    technology_sources = get_sources('technology')
    business = get_sources('business')
    entertainment = get_sources('entertainment')

    print(technology_sources)
    title = '60BeansMade'


    return render_template('index.html', title=title, technology=technology_sources, business=business, entertainment=entertainment)

@app.route('/articles')
def article():
   

    title = 'www.60BeansNows'
    return render_template('article.html', title=title)
    