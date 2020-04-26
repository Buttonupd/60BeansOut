from flask import render_template
from app import app
from .request import get_sources
from .models import news
from .request import get_source


@app.route('/')
def index():
   business = get_sources('business')
   entertainment = get_sources('entertainment')
   general = get_sources('general')
   health = get_sources('health')
   science= get_sources('science')
   sports = get_sources('sports')
   technology_sources = get_sources('technology') 
   title = 'www.60BeansOunce'

   return render_template('index.html', title = title, technology=technology_sources,
   entertainment = entertainment, general=general, health=health, science=science,sports=sports,business=business)
   



   

@app.route('/articles')
def article():
   title = 'www.60BeansNows'
   business = get_sources('business')
   entertainment = get_sources('entertainment')
   general = get_sources('general')
   health = get_sources('health')
   science= get_sources('science')
   sports = get_sources('sports')
   technology_sources = get_sources('technology') 
   title = 'www.60BeansOunce'

   return render_template('index.html', title = title, technology=technology_sources,
   entertainment = entertainment, general=general, health=health, science=science,sports=sports,business=business)

@app.route('/articles')
def read_articles_id(id):
   news = get_source(id)
   title = f'{news.title}'

   return render_template('articles.html', title=title, news=news)
   
    
    