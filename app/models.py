from django.db import models


USERS = [
    {   
        "id": id,
        "avatar": f"img/cool-avatar-{id % 4 + 1}.jpg",
        "name": f"User{id}",
        "rating": 100 * id
    } for id in reversed(range(4))
]

TAGS = [
    {
        "id": id,
        "name": f"Tag {id}"
    } for id in range(10)
]

ANSWERS = [
        {
        "id": id,
        "user": USERS[id % 4],
        "rating": 100 - id,
        "text": f"Great answer #{id} of professional scientist in topic's theme",
        "right_flag": False,
        "time_ago": f"{id} minutes ago"
    } for id in range(0, 100)
]

QUESTIONS = [
    {
        "id": id,
        "user": USERS[id % 4],
        "rating": 100 - id,
        "header": f"Header of question #{id}",
        "description": f"Smart \"complicated\" text of question #{id} which fully reveals the topic of conversation. " +
                        "And just to show truncation I will write here lil more",
        "answers_amount": id + 1,
        "answers": ANSWERS[:id + 1],
        "tags": TAGS[id % 8:id % 8 + 3],
        "time_ago": f"{id} minutes ago"
    } for id in range(0, 100)
]

# Пойдёт в БД
QUESTIONS_SMART = [
    {"id": 1,
    "username": "EgorKreed",
    "avatar": "img/cool-avatar-4.jpg",
    "rating": 157,
    "header": "Егор Крид - лучший!",
    "description": "Обожаю его клипы, знаю наизусть все треки и, кстати, был на сцене на всех его концертах.",
    "answers_amount": 17,
    "tags": ["Музыка", "Фанат"],
    "time_ago": "3 days ago"},

    {"id": 2,
    "username": "CoolVasya",
    "avatar": "img/cool-avatar-1.jpg",
    "rating": 10,
    "header": "Вы тоже \"обожаете\" вёрстку?",
    "description": "Да тут на самом деле и говорить не о чем, лорем ипсум долор сит амет так сказать.",
    "answers_amount": 2,
    "tags": ["HTML", "CSS", "Bootstrap"],
    "time_ago": "5 minutes ago"},

    {"id": 3,
    "username": "LilPeep2007",
    "avatar": "img/cool-avatar-2.jpg",
    "rating": 10,
    "header": "Какие ближайшие забеги в Москве?",
    "description": "5 км, 10 км, полумарафон/марафон - не важно.",
    "answers_amount": 0,
    "tags": ["ЗОЖ"],
    "time_ago": "4 years ago"},

    {"id": 4,
    "username": "Vitek228",
    "avatar": "img/cool-avatar-3.jpg",
    "rating": -28,
    "header": "C++ - лучший язык!",
    "description": "И этим всё сказано.",
    "answers_amount": 54,
    "tags": ["C++", "Unpopular opinion"],
    "time_ago": "2 hours ago"},
]

TAGS_SMART = [
    {"id": 0,
    "name": "C++"},
    {"id": 1,
    "name": "Python"},
    {"id": 2,
    "name": "ЗОЖ"},
    {"id": 3,
    "name": "Django"},
    {"id": 4,
    "name": "МГТУ"},
    {"id": 5,
    "name": "SQL"},
    {"id": 6,
    "name": "Триатлон"},
    {"id": 7,
    "name": "Бег"},
    {"id": 8,
    "name": "Технопарк"},
    {"id": 9,
    "name": "VK"}
]
