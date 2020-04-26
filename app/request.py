from app import app
import urllib.request
import json
from .models import news


News = news.News

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']
source_url = app.config['SOURCE_API_URL_BASE']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None

        if get_sources_response['articles']:
            sources_results_list = get_sources_response['articles']
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

         
        source_object = News(id, name, author, title, description, url, publishedAt, content, urlToImage)
        sources_results.append(source_object)

    return sources_results


def get_source(id):
    '''
    Function that gets the json response to our url request
    '''
    get_source_details_url = base_url.format(id, api_key)
    with urllib.request.urlopen(get_source_details_url) as url:
        get_source_details_data = url.read()
        get_source_details_response = json.loads(get_source_details_data)
        source_results = None

        if get_source-details_response:
            id = get_source_details_response.get('id')
            name = get_source_details_response.get('name')
            author = get_source_details_response.get('author')
            title = get_source_details_response.get('title')
            description =get_source_details_response.get('description')
            url = get_source_details_response.get('url')
            publishedAt = get_source_details_response.get('publishedAt')
            content  = get_source_details_response.get('content')
            urlToImage = get_source_details_response.get('urlToImage')
            sources_results = News(id, name, author, title, description, url, publishedAt, content, urlToImage)

        return source_results


            # sources_results_list = get_sources_response['id']
            # sources_results = process_results(sources_results_list)

    return sources_results



'''Articles source page, 2 Sources url function'''

def get_sources(source):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(source, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None

        if get_sources_response['articles']:
            sources_results_list = get_sources_response['articles']
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

         
        source_object = News(id, name, author, title, description, url, publishedAt, content, urlToImage)
        sources_results.append(source_object)

    return sources_results







