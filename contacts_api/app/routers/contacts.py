from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud import (
    create_contact,
    get_contacts,
    get_contact,
    update_contact,
    delete_contact
)
from app.schemas import ContactCreate, ContactUpdate, ContactOut
from app.deps import get_db

router = APIRouter()

@router.post("/contacts/", response_model=ContactOut)
async def create(contact: ContactCreate, db: Session = Depends(get_db)):
    return await create_contact(db, contact)

@router.get("/contacts/", response_model=List[ContactOut])
async def read_contacts(db: Session = Depends(get_db)):
    return await get_contacts(db)

@router.get("/contacts/{contact_id}", response_model=ContactOut)
async def read_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = await get_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@router.put("/contacts/{contact_id}", response_model=ContactOut)
async def update(contact_id: int, contact: ContactUpdate, db: Session = Depends(get_db)):
    db_contact = await update_contact(db, contact_id, contact)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@router.delete("/contacts/{contact_id}")
async def delete(contact_id: int, db: Session = Depends(get_db)):
    db_contact = await delete_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"detail": "Contact deleted"}
