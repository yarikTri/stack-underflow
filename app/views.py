from xml.parsers.expat import model
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import *
from . import models


def resp404(msg):
    return HttpResponseNotFound(f"404 Not Found: {msg}")


def index(request, page_num = 1):
    p = Paginator(models.QUESTIONS, 10)

    if page_num < 1 or page_num > p.num_pages:
        return resp404("No such page")

    questions = p.get_page(page_num)

    first_page = False
    if page_num == 1:
        first_page = True

    context = {"authenticated": True,
               "questions": questions,
               "first_page": first_page,
               "page_num": page_num,
               "tags": models.TAGS,
               "users": models.USERS}

    return render(request, "index.html", context=context)


def question(request, question_id: int, page_num = 1):
    questions = models.QUESTIONS

    if question_id >= len(questions):
        return resp404("No such question")

    question = questions[question_id]

    p = Paginator(question["answers"], 10)

    if page_num < 1 or page_num > p.num_pages:
        return resp404("No such page")

    answers = p.get_page(page_num)

    first_page = False
    if page_num == 1:
        first_page = True

    context = {"authenticated": True,
               "first_page": first_page,
               "question": question,
               "answers": answers,
               "page_num": page_num,
               "tags": models.TAGS,
               "users": models.USERS}

    return render(request, "question.html", context=context)


def ask(request):
    context = {"authenticated": True,
               "tags": models.TAGS,
               "users": models.USERS}

    return render(request, "ask.html", context=context)


def signup(request):
    context = {"tags": models.TAGS,
               "users": models.USERS}
    return render(request, "signup.html", context=context)


def login(request):
    context = {"tags": models.TAGS,
               "users": models.USERS}
    return render(request, "login.html", context=context)


def tag(request, tag_id: int, page_num = 1):
    tags = models.TAGS

    if tag_id >= len(tags):
        return resp404("No such tag")

    tag = tags[tag_id]

    questions_with_tag = []
    for question in models.QUESTIONS:
        for _tag in question["tags"]:
            if _tag["id"] == tag_id:
                questions_with_tag.append(question)

    p = Paginator(questions_with_tag, 10)

    if page_num < 1 or page_num > p.num_pages:
        return resp404("No such page")

    questions = p.get_page(page_num)

    first_page = False
    if page_num == 1:
        first_page = True

    context = {"authenticated": True,
               "tag": tag,
               "questions": questions,
               "first_page": first_page,
               "page_num": page_num,
               "tags": models.TAGS,
               "users": models.USERS}

    return render(request, "tag.html", context=context)


def base(request):
    return render(request, "inc/base.html")
