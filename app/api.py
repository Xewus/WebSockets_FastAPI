"""Модуль обработки запросов.
"""
from fastapi import APIRouter, Request, WebSocket, status
from fastapi.responses import HTMLResponse

from app.messagestore import Message
from pages.index import index

router = APIRouter()


@router.get(
    path='/',
    summary='Главная страница, с которой идут запросы на websocket`ы'
)
async def get(request: Request):
    ws_url = f'ws{str(request.base_url).lstrip("htps")}ws'
    return HTMLResponse(index % ws_url)


@router.websocket('/ws')
async def add_message(
    websocket: WebSocket,
):
    message = Message()
    await websocket.accept()

    while True:
        data = await websocket.receive_json()
        text = data.get('text')

        if text is not None and len(text) > 0:
            message.num += 1
            message.status = status.HTTP_200_OK
            message.text = text
        else:
            message.status = status.HTTP_400_BAD_REQUEST
            message.text = 'Отсутствует текст сообщения'

        await websocket.send_json(message.dict())
