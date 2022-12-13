from datetime import datetime
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

class User(BaseModel):
    name: str
    friends: list[int] = []
    created_date: datetime | None = None

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data
    
