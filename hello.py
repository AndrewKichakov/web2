def app(environ, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    body = []
    for k, v in environ.items():
        body.append(f"{k}={v}")    
    start_response(status, headers)
    return body