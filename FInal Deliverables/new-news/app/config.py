class Config:
    
    NEWS_BASE_URL_SOURCES = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_BASE_EVERYTHING_URL = 'https://newsapi.org/v2/everything?domains={}&apiKey={}'
    NEWS_BASE_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=in&apiKey={}'
    NEWS_BASE_SOURCE = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    API_KEY = "7d74e79ab06d438a89e5eb6f7a8deb40"

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options= {
    'development': DevConfig,
    'production': ProdConfig
}