from fastapi import FastAPI
from api.comments import comment_route
from api.hashtags import hashtag_route
from db import Base, engine
from api.users import user_route
from api.photos import photo_router


Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")

app.include_router(user_route)
app.include_router(photo_router)
app.include_router(comment_route)
app.include_router(hashtag_route)