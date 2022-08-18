"""Модуль обработки запросов.
"""
from datetime import datetime

from fastapi import APIRouter, Request, WebSocket, status
from fastapi.responses import HTMLResponse

from app.messagestore import MessageStore
from app.settings import STORE
from pages.index import index

router = APIRouter()


@router.get('/')
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
        message = message.get('message')
        if not message:
            await websocket.send_json({
                'status': status.HTTP_400_BAD_REQUEST,
                'error': 'No text in the message'
            })
            continue
        number = await message_store.add(message)
        await websocket.send_json({
            'status': status.HTTP_201_CREATED,
            'number': number,
            'message': message
        })
