import os
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks
from typing import Optional
from image import new_image


mid = [Middleware(CORSMiddleware, allow_origins=["*"],  allow_credentials=True, allow_methods=["*"], allow_headers=["*"])]


app = FastAPI(middleware=mid)


def remove_file(path):
    os.unlink(path)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/img/")
async def img( background_tasks: BackgroundTasks, width: int, name: str, height: Optional[int] = 0):
    n = name.replace(" ", "_")
    n = n.replace("'", "")
    if height == 0:
        a = new_image(width, width, name)
        background_tasks.add_task(remove_file, path=f'temp/{n}.jpeg')
        return FileResponse(a)
    else:
        a = new_image(width, height, name)
        background_tasks.add_task(remove_file, path=f'temp/{n}.jpeg')
        return FileResponse(a)

