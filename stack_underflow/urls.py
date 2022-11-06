"""stack_underflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from app import views


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),

    path("",                                               views.index,    name="index"),
    path("page/<int:page_num>",                            views.index,    name="index_page"),
    path("question/<int:question_id>",                     views.question, name="question"),
    path("question/<int:question_id>/page/<int:page_num>", views.question, name="question_page"),
    path("ask/",                                           views.ask,      name="ask"),
    path("signup/",                                        views.signup,   name="signup"),
    path("login/",                                         views.login,    name="login"),
    path("tag/<int:tag_id>",                               views.tag,      name="tag"),
    path("tag/<int:tag_id>/page/<int:page_num>",           views.tag,      name="tag_page"),
    path("base/",                                          views.base,     name="base")
]