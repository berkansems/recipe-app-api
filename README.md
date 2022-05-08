# recipe-app-api
The source code for recipe app

docker build .
docker-compose build

#start project
docker-compose run appi sh -c 'django-admin startproject appi'
#to test and run flake8 to see errors
docker-compose run appi sh -c 'python manage.py test && flake8'
#start app
docker-compose run appi sh -c 'python manage.py startapp core'

