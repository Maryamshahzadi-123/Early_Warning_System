from fastapi import APIRouter, HTTPException
from schemas.auth_schema import LoginRequest, LoginResponse
from services.auth_service import AuthService
from data_layer.db_context import DbContext

router = APIRouter()

db_context = DbContext()
auth_service = AuthService(db_context)

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    try:
        auth_service.login(request.email, request.password)
        return LoginResponse(success=True, message="Login successful")
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))






