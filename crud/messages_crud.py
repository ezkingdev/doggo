from sqlmodel import Session, select
from models.models import Message, Reply
from models.schemas import MessageCreate, MessageRead, MessageUpdate


def create_message(db: Session, message: MessageCreate):
    db_message = Message(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def get_messages(db: Session):
    messages = db.exec(select(Message)).all()
    return messages


def get_message(db: Session, message_id: int):
    message = db.get(Message, message_id)
    return message


def update_message(db: Session, message_id: int, message_update: MessageUpdate):
    message = db.get(Message, message_id)
    if not message:
        return None
    for var, value in vars(message_update).items():
        setattr(message, var, value) if value is not None else None
    db.commit()
    db.refresh(message)
    return message


def delete_message(db: Session, message_id: int):
    message = db.get(Message, message_id)
    if message:
        db.delete(message)
        db.commit()
