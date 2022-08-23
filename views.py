from utils import render
from urllib.parse import parse_qs, urlsplit


CONTEXT = [
    {
        'id':1,
        'question': 'question1',
        'choices':[
            'choice1',
            'choice2',
            'choice3',
            'choice4'
        ],
        'answer':4
    },
    {
        'id':2,
        'question': 'question2',
        'choices':[
            'choice1',
            'choice2',
            'choice3',
            'choice4'
        ],
        'answer':1
    },
    {
        'id':3,
        'question': 'question3',
        'choices':[
            'choice1',
            'choice2',
            'choice3',
            'choice4'
        ],
        'answer':3
    },
    {
        'id':4,
        'question': 'question4',
        'choices':[
            'choice1',
            'choice2',
            'choice3',
            'choice4'
        ],
        'answer':2
    }
]

def home(environ):
    method = environ.get('REQUEST_METHOD')
    if method == 'GET':
        return render('index.html')


def exam(environ):
    method = environ.get('REQUEST_METHOD')
    if method == 'GET':
        return render('exam.html', context={'questions':CONTEXT})
    
    elif method == 'POST':
        raw = '?' + environ.get('wsgi.input').read().decode()
        data = dict(parse_qs(urlsplit(raw).query))
        data = {int(k): int(v[0]) for k, v in data.items()}

        score = 0
        for question, answer in data.items():
            if CONTEXT[question-1].get('answer') == answer:
                score += 1
    
        return render('result.html', context={'score':score})