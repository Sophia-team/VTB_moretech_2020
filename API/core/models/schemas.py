from pydantic import BaseModel, Field, StrictBool
import datetime


class SuccessRequest:
    success: StrictBool


class UserSubmit(BaseModel):
    id: int
    public_score: float
    submit_dt: datetime.datetime
    chosen_flg: int

    class Config:
        orm_mode = True


class SubmitBase(BaseModel):
    public_score: float
    bid: int
    hid: int
    uid: int


class SubmitCreate(SubmitBase):
    pass


class Submit(SubmitBase):
    id: int
    submit_dt: datetime.datetime
    class Config:
        orm_mode = True
