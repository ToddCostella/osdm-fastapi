from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email_address: str
    street: str
    city: str
    province: str
    postal_code: str


class UserCreate(SQLModel):
    name: str
    email_address: str
    street: str
    city: str
    province: str
    postal_code: str


class UserUpdate(SQLModel):
    name: str
    email_address: str
