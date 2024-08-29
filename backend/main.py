import os
from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise
from models import Client
from structures import ClientCreate, ClientResponse
from datetime import datetime, time
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
    existing_client = await Client.get_or_none(username=client.username)
    if existing_client:
        existing_client.first_name = client.first_name
        existing_client.last_name = client.last_name
        existing_client.birth_date = client.birth_date
        await existing_client.save()
    else:
        existing_client = await Client.create(**client.model_dump())

    days_to_birthday = get_number_of_days_to_birthday(client.birth_date)
    return ClientResponse(
        first_name=client.first_name,
        last_name=client.last_name,
        username=client.username,
        days_to_birthday=days_to_birthday,
    )


@app.get("/clients/{username}", response_model=ClientResponse)
async def get_client(username: str) -> ClientResponse:
    """
    Returns client bio from the database by username.

    :param username: The username of the client to return.
    :type username: str

    :return: A set of client bio if found, else raises an HTTP 404 exception.
    :rtype: ClientResponse
    """
    client = await Client.get_or_none(username=username)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    days_to_birthday = get_number_of_days_to_birthday(
        datetime.combine(client.birth_date, time.min)
    )
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
