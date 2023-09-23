from fastapi import FastAPI

from apis.todo import router as todo_router
from apis import router as main_router
from core.env import Env

app = FastAPI()
app.include_router(main_router)
app.include_router(todo_router)

env = Env()
print(env.get('TEST'))