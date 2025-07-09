from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/hello/{name}/{age}")
async def say_hello(name: str, age: int):
    return {"message": f"Hello {name}, you are {age} years old"}

@app.get("/hello/{name}/{age}/{height}")
async def say_hello(name: str, age: int, height: float):
    return {"message": f"Hello {name}, you are {age} years old and {height} meters tall"}

