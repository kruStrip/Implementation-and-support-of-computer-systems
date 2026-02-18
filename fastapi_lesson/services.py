from .models import NoteOut
from .repositories import NoteRepository


class NoteService:
    def __init__(self, repository: NoteRepository):
        self.repo = repository

    def create_note(self, title: str, body: str | None):
        if not title or not title.strip():
            raise ValueError("Title empty")

        return self.repo.create(title=title, body=body)

    def get_note(self, note_id: int) -> NoteOut | None:
        return self.repo.get(note_id)
