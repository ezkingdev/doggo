from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .models import Color


class NoteBase(BaseModel):
    title: str
    content: str
    completed: bool = False
    color: Color = Color.BLUE


class NoteCreate(NoteBase):
    pass


class NoteRead(NoteBase):
    id: int
    created_at: datetime
    updated_at: datetime


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    completed: Optional[bool] = None
    color: Optional[Color] = None


# Message schemas
class MessageRead(BaseModel):
    id: int
    content: str
    created_at: datetime
    updated_at: datetime


class MessageCreate(BaseModel):
    content: str


class MessageUpdate(BaseModel):
    content: Optional[str]

# Reply schemas
class ReplyRead(BaseModel):
    id: int
    content: str
    created_at: datetime
    updated_at: datetime
