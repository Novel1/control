from uuid import UUID

import tortoise

from app.exceptions import common as common_exc
from passlib.context import CryptContext

from app.user.models import User
from app.material.models import MaterialBlock


class BaseRepo:
    model: tortoise.Model

    async def get_list(self, **kwargs) -> list[tortoise.Model]:
        return await self.model.filter(**kwargs)

    async def get(self, id: UUID) -> tortoise.Model:
        try:
            return await self.model.get(id=id)
        except tortoise.exceptions.DoesNotExist as e:
            raise common_exc.NotFoundException(str(e))

    async def create(self, **kwargs) -> tortoise.Model:
        try:
            return await self.model.create(**kwargs)
        except tortoise.exceptions.IntegrityError as e:
            raise common_exc.CreateException(str(e))

    async def update(self, id: UUID, **kwargs) -> tortoise.Model:
        try:
            instance = await self.get(id=id)
            await instance.update_from_dict(kwargs).save()

            return instance

        except tortoise.exceptions.IntegrityError as e:
            raise common_exc.UpdateException(str(e))

    async def delete(self, id: UUID) -> None:
        try:
            instance = await self.get(id=id)
            await instance.delete()

        except tortoise.exceptions.IntegrityError as e:
            raise common_exc.DeleteException(str(e))


class MaterialRepository(BaseRepo):
    model = MaterialBlock


class UserRepository(BaseRepo):
    model = User

    @staticmethod
    def get_password_hash(password):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.hash(password)

    async def create(self, **kwargs):
        kwargs['password'] = self.get_password_hash(kwargs['password'])
        return await super().create(**kwargs)

