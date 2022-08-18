"""Настройки приложения.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STORE = BASE_DIR / 'chats_story'

STORE.mkdir(exist_ok=True)
