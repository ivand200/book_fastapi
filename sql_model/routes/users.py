from fastapi import APIRouter, HTTPException, Request, status, Depends

from models.users import NewUser, UserSignIn

user_router = APIRouter(
    tags=["User"],
)

users = {}