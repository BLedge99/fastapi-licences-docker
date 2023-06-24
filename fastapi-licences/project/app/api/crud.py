# project/app/api/crud.py

from typing import Union, List

from app.models.pydantic import LicencePayloadSchema
from app.models.tortoise import UserLicence


async def post(payload: LicencePayloadSchema) -> tuple:
    licence = UserLicence(user_id = payload.user_id)
    await licence.save()
    return (licence.user_id, licence.licence_key)
    

async def get(id: int) -> Union[dict, None]:
    licence = await UserLicence.filter(user_id=id).first().values()
    if licence:
        return licence
    return None


async def get_all() -> List:
    licences = await UserLicence.all().values()
    return licences 