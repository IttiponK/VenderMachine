from fastapi import FastAPI
from . import dependency

async def startup(app:FastAPI,db):
    dependency.inject(db)