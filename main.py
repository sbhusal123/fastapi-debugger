from pymongo import MongoClient
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

client = MongoClient()
app = FastAPI()
DB = "local"
MSG_COLLECTION = "startup_log"

@app.get("/channels", response_model=List[str])
def get_channels():
    """Get all channels in list form."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        distinct_channel_list = msg_collection.distinct("_id")
        return distinct_channel_list


@app.get("/")
async def root():
    return {"message": "Hello World"}
