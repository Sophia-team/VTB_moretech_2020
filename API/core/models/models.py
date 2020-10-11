from dsbattle_api_app.core.database import Base
from sqlalchemy import Column, Integer, Float, VARCHAR, DateTime


class Submit(Base):
    __tablename__ = "dsbt_submits"

    id = Column(Integer, primary_key=True, index=True)
    bid = Column(Integer, nullable=False, index=True)
    hid = Column(Integer, nullable=False, index=True)
    submit_dt = Column(DateTime, nullable=False)
    uid = Column(Integer, nullable=False, index=True)

    precission = Column(Float, nullable=False, default=0)
    private_score = Column(Float, nullable=False, default=0)
    public_score = Column(Float, nullable=False, default=0)
    recall = Column(Float, nullable=False, default=0)
    comment = Column(VARCHAR(100), nullable=False, default=0)
    f_measure = Column(Float, nullable=False, default=0)


class ChosenSubmits(Base):
    __tablename__ = "dsbt_chosen_submits"

    id = Column(Integer, primary_key=True, index=True)
    bid = Column(Integer, nullable=False, index=True)
    hid = Column(Integer, nullable=False, index=True)
    uid = Column(Integer, nullable=False, index=True)
    sid = Column(Integer, nullable=False, index=True)
    choice_dt = Column(DateTime, nullable=False)

