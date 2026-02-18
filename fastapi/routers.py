from fastapi import APIRouter, Depends, HTTPException, status

from .models import NoteCreate, NoteOut
from .repositories import NoteRepository
from .services import NoteService

router = APIRouter(prefix="/notes", tags=["Notes"])


def get_service():
    repo = NoteRepository()
    return NoteService(repo)


@router.post("/", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate, service: NoteService = Depends(get_service)):  # noqa: B008
    try:
        return service.create_note(payload.title, payload.body)
    except ValueError as e:
        raise HTTPException(status_code=442, detail=str(e)) from e


@router.get("/{note_id}", response_model=NoteOut)
def get_note(note_id: int, service: NoteService = Depends(get_service)):  # noqa: B008
    note = service.get_note(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
