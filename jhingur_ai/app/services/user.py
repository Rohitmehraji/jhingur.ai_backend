from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserUpdate
from app.core.security import get_password_hash

def update_user(db: Session, *, db_obj: User, obj_in: UserUpdate) -> User:
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)

    if update_data.get("password"):
        hashed_password = get_password_hash(update_data["password"])
        del update_data["password"]
        update_data["hashed_password"] = hashed_password

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
