from fastapi import APIRouter, Depends, Header
from static_json import stored_data
from auth import get_user

router = APIRouter()

@router.get("/")
async def get_testroute(user: dict = Depends(get_user)):
    return user

@router.get("/dashboard/lifecycle")
async def get_lifecycle(user: dict = Depends(get_user)):
    return stored_data.output("lifecycle")

@router.get("/settings/metadata")
async def get_metadata(user: dict = Depends(get_user)):
    return stored_data.output("metadata")

@router.post("/devices")
async def get_devices(user: dict = Depends(get_user)):
    return stored_data.output("queryresults_cves")

@router.get("/devices/views/saved")
async def get_saved_queries(user: dict = Depends(get_user)):
    return stored_data.output("savedqueries")