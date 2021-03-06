

class Config:
    NEWS_API_BASE_URL = 'http://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    SOURCE_API_URL_BASE = 'http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    '''
    General configuration parent class
    '''
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

