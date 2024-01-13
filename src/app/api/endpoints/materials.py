from uuid import UUID

from app.db import repository as repo
import fastapi as fa
from app.material.shemas import MaterialGetSchema, MaterialSchema
from fastapi import APIRouter
from app.exceptions import common as common_exc, http as http_exc

router = APIRouter(prefix='/material', tags=['materials'])
repo = repo.MaterialRepository()


@router.get('')
async def get_material_list(query: MaterialGetSchema = fa.Depends()):
    return await repo.get_list(**query.model_dump())


@router.get('/{id}')
async def get_material(id: UUID):
    try:
        return await repo.get(id)
    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))


@router.post('')
async def create_material(body: MaterialSchema):
    try:
        return await repo.create(**body.model_dump())

    except common_exc.CreateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))


@router.patch('/{id}')
async def update_material(id: UUID, body: MaterialSchema):
    try:
        return await repo.update(id, **body.model_dump())

    except common_exc.UpdateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))

    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))


@router.delete('/{id}')
async def delete_material(id: UUID):
    try:
        return await repo.delete(id)

    except common_exc.DeleteException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))

    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))