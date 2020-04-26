from fastapi import FastAPI, HTTPException, Response, Request, Cookie
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
@app.get("/wel/")
async def get():
    return {"message": Patients}
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
    response.set_cookie(key="session", value="fake-cookie-session-value")
    return {"message": "Come to the dark side, we have cookies"}
@app.post("/login/")
def create_cookie(request: Request, response: Response):
    global Patients
    Patients.append(request.headers['Authorization'])
    response=RedirectResponse(url='/welcome/')
    if(request.headers['Authorization']=="Basic dHJ1ZG5ZOlBhQzEzTnQ="):
        response=RedirectResponse(url='/welcome/')
        response.set_cookie(key="session", value="abcd")
        return response
    return {"message": "Wrong login"}
    return response
@app.post("/welcome/")
def create_cookie(*, response: Response, session: str = Cookie(None)):
    if (session != "abcd"):
        raise HTTPException(status_code=401, detail="Unathorised")
    response.set_cookie(key="session", value=session)
    return {"message": "wow"}
