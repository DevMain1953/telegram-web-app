import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import Client
from structures import ClientCreate, ClientResponse
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()


@app.post("/clients/", response_model=ClientResponse)
async def save_client(client: ClientCreate) -> ClientResponse:
    """
    Saves telegram client bio to database then returns it as response.

    :param client: A set of client data to save to database.
    :type client: ClientCreate

    :return: A set of client data that was saved to database.
    :rtype: ClientResponse
    """
    await Client.create(**client.model_dump())
    days_to_birthday = get_number_of_days_to_birthday(client.birth_date)
    return ClientResponse(
        first_name=client.first_name,
        last_name=client.last_name,
        username=client.username,
        days_to_birthday=days_to_birthday,
    )


def get_number_of_days_to_birthday(birth_date: datetime) -> int:
    """
    Returns number of days to birthday.

    :param birth_date: Date of birth.
    :type birth_date: datetime

    :return: Number of days to birthday.
    :rtype: int
    """
    today = datetime.today()
    next_birthday = birth_date.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    return (next_birthday - today).days


register_tortoise(
    app,
    db_url=f"postgres://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@localhost:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
