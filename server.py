# Gunicorn

from urllib import response
from urls import urlpatterns


def app(environ, start_response):
    endpoint = environ.get("PATH_INFO")
    
    response_404 = "<h3>404 page not found!</h3>"
    data = response_404
    if not endpoint.endswith('/'):
        endpoint += '/'

    if endpoint in urlpatterns.keys():
        data = urlpatterns.get(endpoint)(environ)
    
    header = [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(data)))
    ]

    if data is None:
        data = "<h3>Request method not supported!</h3>"
        status = "400"
    elif data == response_404:
        status = "404"
    else:
        status = "200 OK"

    data = data.encode('utf-8')
    start_response(status, header)
    return iter([data])