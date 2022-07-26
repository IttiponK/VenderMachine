from fastapi import FastAPI
from .import endpoint
from .eventhandler import startup
from functools import partial
from fastapi.middleware.cors import CORSMiddleware
origins = [
    # "http://domainname.com",
    "https://test.ittiponk.com",
    # "http://localhost",
    "http://localhost:3000",
]

def create_app():
    fastApp = FastAPI(title='Ordering Service')
    fastApp.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    fastApp.add_event_handler('startup',func=partial(startup,app=fastApp))
    fastApp.include_router(endpoint.router)
    return fastApp
