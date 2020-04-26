from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    surename: str

 objects = {
    1: {"field_a": "a", "field_b": "b"},
    2: {"field_a": "a", "field_b": "b"},
    3: {"field_a": "a", "field_b": "b"},
    # .... #
}

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
@app.get("/simple_path_tmpl/{obj_id}/{field}}")
def simple_path_tmpl(obj_id: int, field: str):
    print(f"{obj_id=}")
    print(f"{field=}")
    return {"field": objects.get(obj_id, {}).get(field)}
