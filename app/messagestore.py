"""Модуль хранения сообщений.
"""
from pathlib import Path

from app.schemas import MessageSchema


class MessageStore:
    def __init__(self, store: str | Path) -> None:
        self.__counter = 0
        self.__messages = {}
        self.store = store

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.__messages}'

    async def add(self, text: str) -> MessageSchema:
        """Добавляет сообщение в хранилище и записывает в файл.
        Возвращает номер последнего сообщения.
        """
        self.__counter += 1
        self.__messages[self.__counter] = text
        message = MessageSchema(num=self.__counter, text=text)
        with open(self.store, 'a') as file_store:
            file_store.write(str(message) + '\n')
        return message
