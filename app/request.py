from app import app
import urllib.request
import json
from .models import news

News = news.News

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None

        if get_sources_response['totalResults']:
            sources_results_list = get_sources_response['totalResults']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    sources_results = []
    for source_item in news_list:
         id = source_item.get('id')
         name = source_item.get('name')
         author = source_item.get('author')
         title = source_item.get('title')
         description = source_item.get('description')
         url = source_item.get('url')
         publishedAt = source_item.get('publishedAt')
         content  = source_item.get('content')
         urlToImage = source_item.get('urlToImage')

         if urlToImage:
             source_object = News(id, name, author, title, description, url, publishedAt, content, urlToImage)
             sources_results.append(source_object)

    return sources_results





