# Задание SQLite + Flask с хранилищем во внешнем файле

## Образ билдится командой 

```
docker build --tag test-flask-app:1.0 .
```

## Для запуска используйте команду

```
docker run -d --publish 8080:80 --mount type=bind,src=/your/path/to/example.db,dst=/app/example.db test-flask-app:1.0
```
