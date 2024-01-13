from tortoise import models, fields


class MaterialBlock(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=300)
    content = fields.CharField(max_length=400)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, {self.content}'