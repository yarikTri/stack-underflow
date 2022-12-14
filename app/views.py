from django.http import *
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth import hashers
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models


def Response404(msg):
    return HttpResponseNotFound(f"404 Not Found: {msg}")

def paginate(objects_list, page_num, per_page=10):
    p = Paginator(objects_list, per_page)

    if page_num < 1 or page_num > p.num_pages:
        return None

    page = p.get_page(page_num)

    return page



def index(request, page_num = 1):
    questions = paginate(models.Question.objects.get_hot(), page_num)
    if questions == None:
        return Response404("No such page")

    context = {"questions": questions,
               "page_num": page_num,
               "title": "Hot Questions 🔥"}

    return render(request, "index.html", context=context)

def new(request, page_num = 1):
    questions = paginate(models.Question.objects.get_new(), page_num)
    if questions == None:
        return Response404("No such page")

    context = {"questions": questions,
               "page_num": page_num,
               "title": "New Questions"}

    return render(request, "index.html", context=context)


def question(request, question_id: int, page_num = 1):
    question = get_object_or_404(models.Question, id=question_id)

    if request.method == 'POST':
        answer_form = forms.AnswerForm(request.POST)
        if answer_form.is_valid():
            id = answer_form.save(request.user.profile.id, question_id)
            answers = paginate(models.Answer.objects.get_top_answers(question), page_num)

            return redirect(reverse('question_page',
                                    kwargs={'question_id':question_id,
                                            'page_num':answers.paginator.num_pages}) + f'#{id}')

    answers = paginate(models.Answer.objects.get_top_answers(question), page_num)
    if answers == None:
        return Response404("No such page")

    context = {"page_num": page_num,
               "question": question,
               "answers": answers}

    return render(request, "question.html", context=context)


def ask(request):
    if request.method == 'GET':
        question_form = forms.QuestionForm()

    if request.method == 'POST':
        question_form = forms.QuestionForm(request.POST)
        if question_form.is_valid():
            q_id = question_form.save(request.user.profile.id)
            return redirect('question', q_id)

    return render(request, "ask.html", {'form': question_form})


def signup(request):
    if request.method == 'GET':
        user_form = forms.RegistrationForm()
    
    if request.method == 'POST':
        user_form = forms.RegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request=request, **user_form.cleaned_data)
            if user:
                auth.login(request, user)
                return redirect(reverse('index'))
            else:
                user_form.add_error(field=None, error="Error while creating user")

    return render(request, "signup.html", {'form': user_form})


def login(request):
    if request.method == 'GET':
        user_form = forms.LoginForm()

    if request.method == 'POST':
        user_form = forms.LoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request=request, **user_form.cleaned_data)
            if user:
                auth.login(request, user)
                return redirect(reverse('index'))
            else:
                user_form.add_error(field=None, error="Wrong username or password")

    return render(request, "login.html", {'form': user_form})

def logout(request):
    auth.logout(request)
    return redirect(request.META.get('HTTP_REFERER'))

def tag(request, tag_id: int, page_num = 1):
    tag = get_object_or_404(models.Tag, id=tag_id)

    questions_with_tag = models.Question.objects.get_questions_with_tag(tag)

    questions = paginate(questions_with_tag, page_num)
    if questions == None:
        return Response404("No such page")

    context = {"authenticated": True,
               "tag": tag,
               "questions": questions,
               "page_num": page_num}

    return render(request, "tag.html", context=context)


def base(request):
    return render(request, "inc/base.html")
