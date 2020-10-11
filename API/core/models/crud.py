import sqlalchemy
from sqlalchemy.orm import Session
from . import models, schemas
import datetime
import pytz

from typing import Optional


# Создание сабмита
def create_submit(
        db: Session,
        public_score: float,
        private_score: float,
        file_location: str,
        hid: int,
        uid: int,
        bid: int
):
    db_submit = models.Submit(
        bid=bid,
        hid=hid,
        submit_dt=datetime.datetime.now(pytz.timezone('Europe/Moscow')),
        uid=uid,
        private_score=private_score,
        public_score=public_score,
        comment=file_location
    )
    db.add(db_submit)
    db.commit()
    db.refresh(db_submit)

    return db_submit


# get submits
def get_submits(
        db: Session,
        hid: int = None,
        bid: int = None,
        uid: Optional[int] = None,
):
    submits = db.query(models.Submit) \
        .filter(models.Submit.hid == hid) \
        .filter(models.Submit.bid == bid)

    if uid is not None:
        # Get last two stars submits
        choices = db.query(models.ChosenSubmits) \
            .with_entities(
            models.ChosenSubmits.sid,
            sqlalchemy.sql.expression.literal_column('1').label('chosen_flg')
        ).filter(models.ChosenSubmits.hid == hid) \
            .filter(models.ChosenSubmits.uid == uid) \
            .filter(models.ChosenSubmits.bid == bid) \
            .order_by(models.ChosenSubmits.choice_dt.desc()) \
            .distinct() \
            .limit(2).subquery()

        # Mark stared submits and get user submits
        submits = submits \
            .filter(models.Submit.uid == uid) \
            .outerjoin(choices, models.Submit.id == choices.c.sid) \
            .with_entities(
                models.Submit.id,
                models.Submit.public_score,
                models.Submit.submit_dt,
                models.Submit.uid,
                sqlalchemy.sql.expression.case([(choices.c.chosen_flg == '1', 1)], else_=0).label("chosen_flg")) \
            .order_by(models.Submit.submit_dt.desc()) \
            .all()
    else:
        # Get all submits
        submits = submits \
            .with_entities(
                models.Submit.id,
                models.Submit.public_score,
                models.Submit.submit_dt,
                models.Submit.uid, ) \
            .order_by(models.Submit.public_score.desc()) \
            .all()

    return submits


def choose_submit(db: Session, hid: int, uid: int, bid: int, sid: int):

    submit = models.ChosenSubmits(
        bid=bid,
        hid=hid,
        uid=uid,
        sid=sid,
        choice_dt=datetime.datetime.now(pytz.timezone('Europe/Moscow')))
    db.add(submit)
    db.commit()
    db.refresh(submit)
    return submit




