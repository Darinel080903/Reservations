import uvicorn
from fastapi import FastAPI

from web.controller import routes

app = FastAPI()


app.include_router(routes.controller)


if __name__ == "__main__":
    uvicorn.run(app, port=3001)
