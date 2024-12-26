# app/crud/crud_notes.py
from sqlmodel import Session, select
from models.models import Note
from models.schemas import NoteCreate, NoteUpdate


def create_note(db: Session, note_create: NoteCreate) -> Note:
    note = Note.from_orm(note_create)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def get_note(db: Session, note_id: int) -> Note:
    note = db.get(Note, note_id)
    return note


def get_notes(db: Session):
    notes = db.exec(select(Note)).all()
    return notes


def update_note(db: Session, note_id: int, note_update: NoteUpdate) -> Note:
    note = db.get(Note, note_id)
    if not note:
        return None
    for var, value in vars(note_update).items():
        setattr(note, var, value) if value is not None else None
    db.commit()
    db.refresh(note)
    return note


def delete_note(db: Session, note_id: int):
    note = db.get(Note, note_id)
    if note:
        db.delete(note)
        db.commit()
