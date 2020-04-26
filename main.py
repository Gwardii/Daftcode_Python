from fastapi import FastAPI, HTTPException, Response, Request, Cookie
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from hashlib import sha256
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends
import secrets
app=FastAPI()
security = HTTPBasic()
app.secret_key = "very constatn and random secret, best 64 characters, here it is."

session_tokens = []
@app.get("/")
def funkcja():
    return {"message": "Witaj!"}
@app.get("/welcome/")
def funkcja():
    return {"message": "Witaj!"}
@app.post("/login")
def get_current_user(response: Response, credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "trudnY")
    correct_password = secrets.compare_digest(credentials.password, "PaC13Nt")
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    session_token = sha256(bytes(f"{credentials.username}{credentials.password}{app.secret_key}", encoding='utf8')).hexdigest()
    response = RedirectResponse(url='/welcome')
    response.status_code = status.HTTP_302_FOUND
    response.set_cookie(key="session_token", value=session_token)
    session_tokens.append(session_token)
    return response
@app.post("/cookie-and-object/")
def create_cookie(response: Response):
    response.set_cookie(key="session", value="fake-cookie-session-value")
    return {"message": "Come to the dark side, we have cookies"}
@app.post("/welcome/")
def create_cookie():
    return {"a": "a"}
