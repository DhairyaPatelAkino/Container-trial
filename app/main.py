from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI in Docker!"}

@app.get("/health")
def health():
    return {"message": "First class health"}