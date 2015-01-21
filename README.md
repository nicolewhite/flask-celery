```
brew install rabbitmq
PATH=$PATH:/usr/local/sbin
rabbitmq-server
```

```
mkvirtualenv flask-celery
pip install -r requirements.txt
celery -A webapp.celery worker
```

```
make
```