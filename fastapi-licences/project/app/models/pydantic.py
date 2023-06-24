# project/app/models/pydantic.py


from uuid import UUID
from pydantic import BaseModel


class LicencePayloadSchema(BaseModel):
    user_id : int


class LicenceResponseSchema(LicencePayloadSchema):
    licence_key: UUID