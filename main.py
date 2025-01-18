#!/usr/bin/env python3

from typing import Optional


from fastapi import FastAPI, Depends
from routers import secure, public
from auth import get_user

app = FastAPI()

app.include_router(
    public.router,
    prefix="/api/v1/public"
)
app.include_router(
    secure.router,
    prefix="/api/v1/secure",
    dependencies=[Depends(get_user)]
)

# # From Browser: https://code-debug.scheun.us
# # From terminal: curl -X 'GET' -H 'accept: application/json' 'https://code-debug.scheun.us'
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# # From Browser: https://code-debug.scheun.us/items/5?q=something
# # From terminal: curl -X 'GET' -H 'accept: application/json' 'https://code-debug.scheun.us/items/5?q=somequery'
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}