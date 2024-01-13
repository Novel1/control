from uuid import UUID

import pydantic


class MaterialSchema(pydantic.BaseModel):
    title: str
    content: str


class MaterialGetSchema(MaterialSchema):
    id: UUID