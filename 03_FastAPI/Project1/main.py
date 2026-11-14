from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # Create an instance of FastAPI

# The app instance is the main component of our FastAPI application. It is used to configure the application,

class Custom(BaseModel):
    name: str
    age: int

@app.get("/")
async def home():
    return {"message": "Welcome"}

# /ping is the path of the endpoint
@app.get("/ping")
async def root():
    return {"message": "Hello World!"}

@app.get("/blogs/comments")
async def read_blog_comment():
    return {"comments": "no comments yet"}

@app.get("/blogs/{blog_id}")
async def read_blogs(blog_id: int, request_body: Custom, q: str = None, name: str = ''):
    print(q, name)
    return {"blog_id": blog_id}

