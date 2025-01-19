from fastapi import APIRouter, Depends, Header
from static_json import stored_data
from auth import get_user

router = APIRouter()

@router.get("/")
async def get_testroute(user: dict = Depends(get_user)):
    return user

@router.get("/settings/metadata")
async def get_metadata(user: dict = Depends(get_user)):
    print(stored_data.output("metadata"))
    return stored_data.output("metadata")

@router.get("/dashboard/lifecycle")
async def get_metadata(user: dict = Depends(get_user)):
    return user

@router.get("devices/views/saved")
async def get_metadata(user: dict = Depends(get_user)):
    return user

@router.get("users/views/saved")
async def get_metadata(user: dict = Depends(get_user)):
    return user