from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Петров'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Омерзительная восьмерка'),
    'description': fields.String(required=True, max_length=100, example='Сша после гражданской войны'),
    'trailer': fields.String(required=True, max_length=100, example='www/'),
    'year': fields.Integer(required=True, example=2015),
    'rating': fields.Float(required=True, example=7.8),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(),
    'email': fields.String(required=True, max_length=100, example='edsd@mail.ru'),
    'password': fields.String(required=True, max_length=100, example='1234'),
    'name': fields.String(required=True, max_length=100, example='Vasya'),
    'surname': fields.String(required=False, max_length=100, example='Ivanov'),
    'favorite_genre': fields.Nested(genre)
})