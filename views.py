from utils import render
from urllib.parse import parse_qs, urlsplit
import json


def home(environ):
    method = environ.get('REQUEST_METHOD')
    if method == 'GET':
        return render('index.html')


def exam(environ):
    method = environ.get('REQUEST_METHOD')
    with open('data/data.json') as f:
        data_context = json.load(f)
        
    if method == 'GET':
        return render('exam.html', context={'questions':data_context})
    
    elif method == 'POST':
        raw = '?' + environ.get('wsgi.input').read().decode()
        data = dict(parse_qs(urlsplit(raw).query))
        data = {int(k): int(v[0]) for k, v in data.items()}

        score = 0
        for question, answer in data.items():
            if data_context[question-1].get('answer') == answer:
                score += 1
        return render('result.html', context={'score':score})

