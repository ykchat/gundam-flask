# gundam-flask

Flask example

## Run on local

```
$ python server.py
```

## Run on docker

```
$ docker build -t gundam-flask .
$ docker run -it -d --name gundam-flask --link mongo:mongo -p 8080:8080 gundam-flask
```

## Run on cloud foundry

```
$ cf push
```
