from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from src import db.py
import s

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

database = Database()


@app.get("/")
async def homepage():
    return FileResponse("static/html/index.html")


@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/images/favicon.ico")


@app.get("/users/{user_id}/")
async def read_user(user_id: int):
    user = await database.get_user(user_id)
    if user is None:
        return JSONResponse(content={}, status_code=404)
    return JSONResponse(content=user.__dict__)


@app.get("/hello/")
async def hello():
    return FileResponse("static/html/hello.html")


@app.post("/users/new/")
async def create_user(user: User):
    user_id = await database.add_user(user)
    return JSONResponse(content={"user_id": user_id}, status_code=200)
    connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Добавляем нового пользователя
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
