from typing import Optional

from sqlalchemy import desc
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre

class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director

class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    # def get_all_order_by(self, page: Optional[int] = None, filter=None) -> List[T]:
    #     stmt = self._db_session.query(self.__model__)
    #     if filter:
    #         stmt = stmt.order_by(desc(self.__model__.year))
    #     if page:
    #         try:
    #             return stmt.paginate(page, self._items_per_page).items
    #         except NotFound:
    #             return []
    #     return stmt.all()

class UsersDAO(BaseDAO[User]):
    __model__ = User

    def create(self, login, password):
        try:
            self._db_session.add(
                User(
                    email=login,
                    password=password
                )
            )
            self._db_session.commit()
            print("Пользователь добавлен")
        except Exception as e:
            print(e)
            self._db_session.rollback()

    def get_user_by_login(self, login):
        return self._db_session.query(User).filter(User.email == login).one()

    def partial_update(self, user_d):
        self._db_session.add(user_d)
        self._db_session.commit()

        return user_d
