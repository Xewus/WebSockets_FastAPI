"""Модуль хранения сообщений.
"""
from pydantic import BaseModel


class Message(BaseModel):
    """Класс сообщений.

    Attrs:
      - num (int): Порядковый номер сообщения.
          Defaults to 0.
      - status (int): HTTP-статус сообщения.
          Defaults to 400.
      - text (str): Текст сообщения.
          Defaults to `тсутствует текст сообщения`.
    """
    num: int = 0
    status: int = 0
    text: str = ''
