from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional
from enum import Enum


# Define a Color enum if you want to restrict to specific choices
class Color(str, Enum):
    RED = '#ffe5ec'
    GREEN = '#c7f9cc'
    BLUE = '#ade8f4'
    YELLOW = '#efefd0'
    PURPLE = '#c8b6ff'
    ORANGE = '#ffe5b4'


class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    content: str
    color: Color = Field(default=Color.BLUE)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Automatically update the `updated_at` field on modification
    def before_update(self, **kwargs):
        self.updated_at = datetime.utcnow()


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def before_update(self, **kwargs):
        self.updated_at = datetime.utcnow()


class Reply(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    message_id: int
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def before_update(self, **kwargs):
        self.updated_at = datetime.utcnow()
