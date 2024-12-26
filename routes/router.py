# app/api/notes_router.py
from fastapi import APIRouter, HTTPException, Depends, responses, templating, Request
from sqlmodel import Session
from db.database import get_session
from crud.notes_crud import create_note, get_note, get_notes, update_note, delete_note
from crud.messages_crud import get_messages, get_message, update_message, delete_message
from models.schemas import NoteCreate, NoteRead, NoteUpdate, MessageCreate, MessageRead, MessageUpdate
from models.models import Note, Message

router = APIRouter()
templates = templating.Jinja2Templates(directory="html_templates")


@router.get("/", response_class=responses.HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.post("/notes/", response_model=NoteRead)
def create_note(note: NoteCreate, session: Session = Depends(get_session)):
    db_note = Note.from_orm(note)
    print(f"Created at: {db_note.created_at}, Type: {type(db_note.created_at)}")
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note


@router.get("/notes/", response_model=list[NoteRead])
def read_notes_endpoint(session: Session = Depends(get_session)):
    try:
        return get_notes(session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/notes/{note_id}", response_model=NoteRead)
def read_note_endpoint(note_id: int, session: Session = Depends(get_session)):
    note = get_note(session, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.patch("/notes/{note_id}", response_model=NoteRead)
def update_note_endpoint(note_id: int, note: NoteUpdate, session: Session = Depends(get_session)):
    updated_note = update_note(session, note_id, note)
    if updated_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note


@router.delete("/notes/{note_id}")
def delete_note_endpoint(note_id: int, session: Session = Depends(get_session)):
    delete_note(session, note_id)
    return {"ok": True}


@router.post("/messages/", response_model=MessageRead)
def create_message(message: MessageCreate, session: Session = Depends(get_session)):
    db_message = Message.from_orm(message)
    session.add(db_message)
    session.commit()
    session.refresh(db_message)
    return db_message


@router.get("/messages/", response_model=list[MessageRead])
def read_messages_endpoint(session: Session = Depends(get_session)):
    try:
        return get_messages(session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/messages/{message_id}", response_model=MessageRead)
def read_message_endpoint(message_id: int, session: Session = Depends(get_session)):
    message = get_message(session, message_id)
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return message


@router.patch("/messages/{message_id}", response_model=MessageRead)
def update_message_endpoint(message_id: int, message: MessageUpdate, session: Session = Depends(get_session)):
    updated_message = update_message(session, message_id, message)
    if updated_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return updated_message


@router.delete("/messages/{message_id}")
def delete_message_endpoint(message_id: int, session: Session = Depends(get_session)):
    delete_message(session, message_id)
    return {"ok": True}


@router.get("/globe_data")
def get_globe_data_endpoint():
    return {"ok": True}
