from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db
from dao.user import UserDAO
from service.user import UserService


director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)

user_dao = UserDAO(session=db.session)
user_service = UserService(dao=user_dao)