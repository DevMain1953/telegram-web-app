from tortoise import fields
from tortoise.models import Model


class Client(Model):
    """
    Model that describes Telegram client with Bio.
    """

    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    username = fields.CharField(max_length=50, unique=True)
    birth_date = fields.DateField()

    class Meta:
        table = "clients"
