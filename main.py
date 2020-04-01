from fastapi import FastAPI

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