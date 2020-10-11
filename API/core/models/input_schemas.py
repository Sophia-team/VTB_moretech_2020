from pydantic import BaseModel, Field
from typing import Optional


class ChooseSubmitInput(BaseModel):
    user_sender_id: Optional[int] = Field(None, example="User id of query sender")
    hid: int
    uid: int
    bid: int
    sid: int
    token: Optional[str] = Field('', example="token key for api access")