from app.db import repository as repo
import fastapi as fa
from app.user import schemas
from fastapi import APIRouter

router = APIRouter(tags=['user'])
repo = repo.UserRepository()


@router.get('/users')
async def get_users(params: schemas.UserAllOptionalSchema = fa.Depends()):
    return await repo.get_list(**params.dict(exclude_none=True))


@router.get('/users/{id}')
async def get_users(id: int):
    return await repo.get(id=id)


@router.post('/users')
async def create_user(data: schemas.CreateUserSchema):
    return await repo.create(**data.dict(exclude_none=True))