## Eitaa channel scraper

#### Run the app:
```
mkdir offsets &&\
    docker-compose up --build -d &&\
    docker-compose logs -f crawler
```
#### Remove app state:
```
rm -rf offsets && docker-compose down -v
```

Mongo Express web at http://localhost:8081/db/eitaa/