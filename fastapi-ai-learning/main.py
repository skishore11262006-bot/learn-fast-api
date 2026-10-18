from fastapi import FastAPI

app = FastAPI(title="AI Learning API", description="My first API while learning AI Engineering")


@app.get("/")
def home():
    return {"message": "Hello! I am learning FastAPI as part of my AI Engineering journey."}


@app.get("/learn/{topic}")
def learn(topic: str):
    return {"topic": topic, "status": "learning in progress"}
