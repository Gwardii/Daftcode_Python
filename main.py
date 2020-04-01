from fastapi import FastAPI

class Item(BaseModel):
    name: str
    surename: str
class N(BaseModel):
    N: int = 0

app = FastAPI()


@app.get("/")
async def read_main():
    return {"message": "Hello World during the coronavirus pandemic!"}
@app.get("/method/")
async def get():
    return {"method": "GET"}
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
    n.N += 1
    return {"id": n.N, "patient": item}
