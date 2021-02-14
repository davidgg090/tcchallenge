# WebScraper

A django template for the backend technical test

## First Steps
Create and launch a virtualenv
```
virtualenv -p python3 .env
source .env/bin/active
```

Install the project requirements (within the virtualenv) and migrate to create the database.
```
pip install -r requirements.txt
python manage.py migrate
```

## Run Development Server
```
python manage.py runserver
```

## Run Tests
```
python manage.py test
```

## API Endpoints

### `/scrapers/`
### `/asset/{nombre_del_asset}/`