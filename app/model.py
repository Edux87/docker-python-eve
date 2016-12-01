SHEMA = {
    'MONGO_HOST': 'mongo',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'eve',
    'X_DOMAINS': '*',
    'X_HEADERS': [
        'Authorization',
        'If-Match',
        'Access-Control-Expose-Headers',
        'Content-Type',
        'Pragma',
        'Cache-Control'
    ],
    'X_EXPOSE_HEADERS': [
        'Origin',
        'X-Requested-With',
        'Content-Type',
        'Accept'
    ],
    'DOMAIN': {
        'people': {}
    }
}
