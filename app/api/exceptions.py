from fastapi import status
from sqlalchemy.exc import IntegrityError, NoResultFound, SQLAlchemyError


class SQLAlchemyException:
    @staticmethod
    def status_code(exception: SQLAlchemyError) -> int:
        if isinstance(exception, NoResultFound):
            return status.HTTP_404_NOT_FOUND

        if isinstance(exception, IntegrityError):
            return status.HTTP_409_CONFLICT

        return status.HTTP_500_INTERNAL_SERVER_ERROR

