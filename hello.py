def app(environ, start_response):
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]  
    start_response(status, headers)
    return body