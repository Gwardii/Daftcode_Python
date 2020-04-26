from fastapi import FastAPI, HTTPException, Response
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
@app.get("/login/")
def create_cookie(login: str, password: str, response: Response):
    if(login=='trudnY' and password=='PaC13Nt'):
        response.set_cookie(key="session_token", value="fake-cookie-session-value")
        return RedirectResponse(url='/welcome/')
    return {"message": "Wrong login"}
@app.get("/welcome/")
def create_cookie(*, response: Response, session_token: str = "nic"):
    if session_token != "fake-cookie-session-value":
        raise HTTPException(status_code=403, detail="Unathorised")
    response.set_cookie(key="session_token", value=session_token)
