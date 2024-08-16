from sqlalchemy.orm import Session
from app.models import Contact
from app.schemas import ContactCreate, ContactUpdate

async def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    await db.commit()
    await db.refresh(db_contact)
    return db_contact

async def get_contacts(db: Session):
    return await db.execute(Contact.select()).scalars().all()

async def get_contact(db: Session, contact_id: int):
    return await db.get(Contact, contact_id)

async def update_contact(db: Session, contact_id: int, contact: ContactUpdate):
    db_contact = await db.get(Contact, contact_id)
    if db_contact is None:
        return None
    for key, value in contact.dict().items():
        setattr(db_contact, key, value)
    await db.commit()
    await db.refresh(db_contact)
    return db_contact

async def delete_contact(db: Session, contact_id: int):
    db_contact = await db.get(Contact, contact_id)
    if db_contact:
        await db.delete(db_contact)
        await db.commit()
    return db_contact
