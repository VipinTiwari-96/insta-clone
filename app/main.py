from fastapi import FastAPI;
# routers
from .routers import user, post, auth, votes;


app= FastAPI()


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(votes.router)

