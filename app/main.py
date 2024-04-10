from fastapi import FastAPI;
# routers
from .routers import user, post;


app= FastAPI()


app.include_router(user.router)
app.include_router(post.router)

