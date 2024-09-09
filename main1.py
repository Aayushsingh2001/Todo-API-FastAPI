from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # Create an instance of FastApi

# The app instance is the main component of our FastAPI application. It is used to configure the application.

# /ping is the path of the endpoint.
# The @app.get() decorator i used to define an endpoint.

class Custom(BaseModel):
    name: str
    age: int

@app.get("/ping")
async def root():
    return{"message": "Hello World!!!!...."}

@app.get("/")
async def root():
    return{"message": "Welcome.."}

@app.get("/blogs/comments")
async def read_blog_comments():
    return {"comments": "No comments yet!"}

@app.post("/blogs/{blog_id}")
async def read_blogs(blog_id: int, request_body: Custom, q: str = None, name: str = ''):
    print(request_body.age)
    print(q, name)
    return{"blog_id": blog_id}
