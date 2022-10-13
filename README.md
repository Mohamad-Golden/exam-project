# exam-project
## requirements
* python (version 3)
* gunicorn

---------
## Install gunicorn
Run the command below to install gunicorn:
```
pip install gunicorn
```

-------
## Start the server
In the root directory of the project run this command:
```
gunicorn server:app
```
Then open the url "http://127.0.0.1:8000/" in the browser.
