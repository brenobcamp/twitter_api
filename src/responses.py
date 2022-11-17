from pydantic import BaseModel

class Timeline(BaseModel):
    _id: str
    next_token: str
    result_count: int
    newest_id: str
    oldest_id: str