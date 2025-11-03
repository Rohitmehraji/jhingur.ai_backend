from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.services import user as user_service
from app.models import user as user_model
from app.database import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.get("/me", response_model=user_schema.User)
def read_users_me(current_user: user_model.User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=user_schema.User)
def update_user_me(user_update: user_schema.UserUpdate, db: Session = Depends(get_db), current_user: user_model.User = Depends(get_current_user)):
    return user_service.update_user(db, db_obj=current_user, obj_in=user_update)
