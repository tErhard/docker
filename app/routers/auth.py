from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str
    role: str

fake_users_db = {
    "user1": {
        "username": "user1",
        "password": "password1",
        "role": "admin"
    },
    "user2": {
        "username": "user2",
        "password": "password2",
        "role": "user"
    }
}

def fake_decode_token(token):
    username = token
    user = fake_users_db.get(username)
    return user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied"
        )
    return current_user

@app.get("/admin", dependencies=[Depends(get_current_active_user)])
async def admin_route():
    return {"message": "Welcome, Admin!"}
