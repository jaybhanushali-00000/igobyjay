from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "http://localhost:3000",
    "https://igobyjay.pages.dev"

    ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



@app.get("/")
async def root():
    return{
        "messgae" : " server running fine "
    }

@app.get("/auth/{user_id}_{password}")
async def auth(user_id:str,password:str):
    return{
        "value" : 1
    }