# basic-django

## Reason

The purpose of this project is learn how to build a webserver using django.

## Objective

The objective of this project is to calculate area and permieters of shapes.

## Usage

##### User

User registration: `POST /register`
User login: `POST /login`

##### Shapes

To list all shapes of one type `GET /<type>/` <br/>
To retrieve one specific city: `GET /<type>/<pk>` <br/>
where type is rectangle, square, diamond or triangle
where pk is the primary key

##### Area

To perform the compute action on specified shape: `GET /area/<type>/<pk>/`<br/>
where type is rectangle, square, diamond or triangle
where pk is the primary key

##### Perimter

To perform the compute action on specified shape: `GET /perimeter/<type>/<pk>/`<br/>
where type is rectangle, square, diamond or triangle
where pk is the primary key

## Technologies

Django>=3.2.5, <3.3.0
djangorestframework>=3.12.4, <3.13.0
gunicorn==20.1.0
django-heroku==0.3.1
python-dotenv==0.17.1
