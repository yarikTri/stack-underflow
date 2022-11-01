from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"authorized": True}
    return render(request, "index.html", context=context)

def question(request, question_id: int):
    context = {"authorized": True}
    return render(request, "question.html", context=context)

def ask(request):
    context = {"authorized": True}
    return render(request, "ask.html", context=context)

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")

# Необязательно
def tag(request, tag_id: int):
    context = {"authorized": True}
    return render(request, "tag.html", context=context)

def base(request):
    return render(request, "inc/base.html")