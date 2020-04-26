from fastapi import FastAPI, HTTPException, Response, Cookie
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    surename: str


app = FastAPI()

N=0
Patients=[]
@app.get("/")
async def read_main():
    return {"message": "Hello World during the coronavirus pandemic!"}
@app.get("/welcome/")
async def get():
    return {"message": "Witaj"}
@app.post("/method/")
async def get():
    return {"method": "POST"}
@app.put("/method/")
async def get():
    return {"method": "PUT"}
@app.delete("/method/")
async def get():
    return {"method": "DELETE"}
@app.post("/patient/")
async def fun(item: Item):
    global Patients
    global N
    N+=1
    Patients += [item]
    return {"id": N, "patient": item}
@app.get("/patient/{pk}")
async def fun(pk: int):
    global Patients
    if pk > len(Patients):
        raise HTTPException(status_code=204)
    patient=Patients[pk-1]
    return patient
@app.post("/cookie-and-object/")
def create_cookie(response: Response):
    response.set_cookie(key="fake_session", value="fake-cookie-session-value")
    return {"message": "Come to the dark side, we have cookies"}
@app.post("/login/")
def create_cookie(login: str, password: str, response: Response):
    response.set_cookie(key="fake_session", value=f"{user}{password}")
    if(login=='a' and password=='a'):
        return RedirectResponse(url='/welcome/')
    return {"message": "Wrong login"}
@app.post("/welcome/")
def create_cookie(*, response: Response, fake_session: str = Cookie(None)):
    if (fake_session != "aa"):
        raise HTTPException(status_code=403, detail="Unathorised")
    response.set_cookie(key="session_token", value=fake_session)
    
