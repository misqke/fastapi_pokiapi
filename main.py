from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import search, random

app = FastAPI()

origins = ["http://localhost:3000", "https://misqke-pokedex.netlify.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["GET", "POST"]
    )

app.include_router(search.router)
app.include_router(random.router)
