from fastapi import FastAPI

from fasthtml.common import *
from collections import namedtuple

from apps.todo import app

apps = FastAPI()

todo = app


apps.mount("/", todo)



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:apps", host="0.0.0.0", port=8000, reload=True, access_log=True)
