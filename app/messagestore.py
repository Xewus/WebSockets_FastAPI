"""Модуль хранения сообщений.
"""
from pathlib import Path


class MessageStore:
    def __init__(self, store: str | Path) -> None:
        self.__counter = 0
        self.__messages = {}
        self.store = store

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.__messages}'

    async def add(self, message: str) -> int:
        """Добавляет сообщение в хранилище и записывает в файл.
        Возвращает номер последнего собщения.
        """
        self.__counter += 1
        self.__messages[self.__counter] = message
        with open(self.store, 'a') as file_store:
            file_store.write(f'{self.__counter}: {message}\n')
        return self.__counter
