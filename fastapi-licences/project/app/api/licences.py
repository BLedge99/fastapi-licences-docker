# project/app/api/licences.py

from fastapi import APIRouter, HTTPException
from typing import List

from app.api import crud
from app.models.pydantic import LicencePayloadSchema, LicenceResponseSchema
from app.models.tortoise import LicenceSchema


router = APIRouter()


@router.get("/{user_id}/", response_model=LicenceSchema)
async def get_licences(user_id: int) -> LicenceSchema:
    licence = await crud.get(user_id)
    if not licence:
         raise HTTPException(status_code=404, detail="Licence not found")
    
    return licence


@router.get("/", response_model=List[LicenceSchema])
async def read_all_licences() -> List[LicenceSchema]:
    return await crud.get_all()


@router.post("/", response_model=LicenceResponseSchema, status_code=201)
async def create_licence(payload: LicencePayloadSchema) -> LicenceResponseSchema:
    licence_data = await crud.post(payload)
    user_id = licence_data[0]
    licence_key = licence_data[1]

    response_object = {
        "user_id": user_id,
        "licence_key": licence_key
    }
    return response_object