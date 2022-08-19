"""Схемы ответов на запросы.
"""
from pydantic import BaseModel, Field, PositiveInt
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class BaseSchema(BaseModel):
    status: int = Field(
        default=HTTP_200_OK,
        title='Статус-код ответа',
        ge=100,
        le=526
    )
    text: str = Field(
        default='Введите текст',
        title='Текст сообщения',
        min_length=1
    )


class MessageSchema(BaseSchema):
    num: PositiveInt

    def __str__(self) -> str:
        return f'{self.num}: {self.text}'


class ErrorSchema(BaseSchema):
    status: int = HTTP_400_BAD_REQUEST
