

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import create_engine, Session

from models import UserCreate, User
from user_service import UserService

app = FastAPI()
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session


def get_user_service(session: Session = Depends(get_session)):
    return UserService(session)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/user")
async def read_user():
    class User(BaseModel):
        id: int
        name: str
        email: str

    user = User(id=1, name='John Doe', email='john.doe@example.com')
    return user


@app.post("/users/", response_model=User)
def create_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    return user_service.add_user(user)


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate, user_service: UserService = Depends(get_user_service)):
    updated_user = user_service.update_user(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    deleted_user = user_service.delete_user(user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user


@app.get("/users/", response_model=list[User])
def get_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_all_users()


@app.get("/users/filter/", response_model=list[User])
def filter_users(name: str | None = None, email_address: str | None = None, user_service: UserService = Depends(get_user_service)):
    return user_service.filter_users(name=name, email_address=email_address)


# Start the FastAPI server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

