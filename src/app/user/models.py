from tortoise import models, fields


class User(models.Model):
    id = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=100)
    password = fields.CharField(max_length=200)

    class Meta:
        table = 'user'

    def __str__(self):
        return self.username
