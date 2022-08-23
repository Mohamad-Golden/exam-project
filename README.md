# exam-project
## requirements
* python (version 3)
* gunicorn

---------
## Insatll gunicorn
run the comment below to install gunicorn:
```
pip install gunicorn
```

-------
## Start the server
In the root directory of the project run this commend:
```
gunicorn server:app
```
Then open the url "http://127.0.0.1:8000/" in the browser.
