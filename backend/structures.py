from pydantic import BaseModel
from datetime import datetime


class ClientCreate(BaseModel):
    """
    Data structure that describes the set of data used to save telegram client bio to database.
    """

    first_name: str
    last_name: str
    username: str
    birth_date: datetime


class ClientResponse(BaseModel):
    """
    Data structure that describes the set of data used to return telegram client bio from database.
    """

    first_name: str
    last_name: str
    username: str
    days_to_birthday: int
