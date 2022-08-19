"""Модуль обработки запросов.
"""
from datetime import datetime

from fastapi import APIRouter, Request, WebSocket
from fastapi.responses import HTMLResponse

from app.messagestore import MessageStore
from app.schemas import ErrorSchema
from app.settings import STORE
from pages.index import index

router = APIRouter()


@router.get(
    path='/',
    summary='Гоавная страница, с которой идут запросы на websocket`ы'
)
async def get(request: Request):
    ws_url = f'ws{str(request.base_url).lstrip("htps")}ws'
    return HTMLResponse(index % ws_url)


@router.websocket('/ws')
async def add_message(
    websocket: WebSocket,
):
    chat_id = str(datetime.now().timestamp()) + '.txt'
    message_store = MessageStore(store=STORE / chat_id)
    await websocket.accept()
    while True:
        message = await websocket.receive_json()
        text = message.get('text')
        if not text:
            await websocket.send_json(ErrorSchema().json())
            continue
        message = await message_store.add(text)
        await websocket.send_json(message.json())
