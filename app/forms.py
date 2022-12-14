from django import forms
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib.auth import hashers
from . import models


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=4)
    password = forms.CharField(min_length=8)
    password_check = forms.CharField(min_length=8)
    email = forms.EmailField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    avatar = forms.ImageField(required=False)

    def clean(self):
        username = self.cleaned_data.get('username')
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_check')

        if models.Profile.objects.get_user_by_username(username):
            self.add_error('username', IntegrityError("User already exists"))

        if password_1 != password_2:
            self.add_error(None, ValidationError("Passwords don't match", code='invalid'))

        return self.cleaned_data

    def save(self):
        super().clean()
        new_user = models.User(username=self.cleaned_data['username'],
                    email=self.cleaned_data['email'],
                    first_name=self.cleaned_data['first_name'],
                    last_name=self.cleaned_data['last_name'],
                    password=hashers.make_password(self.cleaned_data['password']))
        new_user.save()

        new_user_id = new_user.id

        new_profile = models.Profile(user_id=new_user_id)
        avatar = self.files.get('avatar')
        if avatar:
            new_profile.avatar=avatar

        new_profile.save()


class QuestionForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
    tags = forms.CharField(required=False)

    def save(self, profile_id) -> int:
        super().clean()
        new_question = models.Question(profile_id=profile_id,
                                        title=self.cleaned_data['title'],
                                        text=self.cleaned_data['text'])
        new_question.save()

        return new_question.id

class AnswerForm(forms.Form):
    text = forms.CharField()

    def save(self, profile_id, q_id) -> id:
        super().clean()
        new_answer = models.Answer(profile_id=profile_id,
                                    related_question_id=q_id,
                                    text=self.cleaned_data['text'])
        new_answer.save()

        return new_answer.id

