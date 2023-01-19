from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def hallo():
    return {"message": "Hallo Oma"}

@app.get("/hallo")
async def hallo2():
    return {"message": "Hallo Opa"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)