from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI AI Service Running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
