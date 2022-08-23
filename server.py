# Gunicorn

from urls import urlpatterns, static_root
from utils import static_view, static
import os

def app(environ, start_response):
    endpoint = environ.get("PATH_INFO")
    content_type = 'text/html'
    response_404 = "<h3>404 page not found!</h3>"
    data = response_404

    if not endpoint.endswith('/'):
        endpoint += '/'

    if endpoint in static(static_root):
        data = static_view(os.path.basename(endpoint[:-1]), static_root)
        if os.path.splitext(endpoint[:-1])[1] == '.css':
            content_type = 'text/css'
        elif os.path.splitext(endpoint[:-1])[1] == '.js':
            content_type = 'text/javascript'

    header = [
    ("Content-Type", content_type),
    ]

    if endpoint in urlpatterns.keys():
        data = urlpatterns.get(endpoint)(environ)
        
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