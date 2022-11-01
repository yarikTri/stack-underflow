from tkinter.messagebox import QUESTION
from django.db import models

QUESTIONS = [
    {"id": 1,
    "username": "EgorKreed",
    "avatar": "img/cool-avatar-4.jpg",
    "rating": 157,
    "header": "Егор Крид - лучший!",
    "text": "Обожаю его клипы, знаю наизусть все треки и, кстати, был на сцене на всех его концертах.",
    "answers_amount": 17,
    "tags": ["Музыка", "Фанат"],
    "time_ago": "3 дня назад"},

    {"id": 2,
    "username": "CoolVasya",
    "avatar": "img/cool-avatar-1.jpg",
    "rating": 10,
    "header": "Вы тоже \"обожаете\" вёрстку?",
    "text": "Да тут на самом деле и говорить не о чем, лорем ипсум долор сит амет так сказать.",
    "answers_amount": 2,
    "tags": ["HTML", "CSS", "Bootstrap"],
    "time_ago": "5 минут назад"},
]
