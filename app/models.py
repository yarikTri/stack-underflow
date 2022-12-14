from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.db.models import Sum
from django.contrib.auth.models import User

class TagManager(models.Manager):
    def get_tags_of_question(self, question):
        return self.filter(questions=question)
    
    def get_top(self):
        return self.annotate(cnt=Count('questions')).order_by('-cnt')[:10]

class Tag(models.Model):
    name = models.CharField(max_length=16)

    objects = TagManager()

    def __str__(self):
        return f'({self.id}) {self.name}'


class ProfileManager(models.Manager):
    def get_top_by_rating(self):
        return self.order_by('-rating')[:5]

    def get_user_by_username(self, username):
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            user = None

        return user

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True, default='stack-underflow.png')
    rating = models.IntegerField(default=0)

    objects = ProfileManager()

    def __str__(self):
        return f'({self.id}) {self.user.username}'


class QuestionManager(models.Manager):
    def get_new(self):
        return self.order_by('-created_at')

    def get_hot(self):
        return self.order_by('-rating')

    def get_questions_with_tag(self, tag):
        return self.filter(tags=tag).order_by('-rating')

class Question(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=64)
    text = models.TextField(max_length=2000)
    tags = models.ManyToManyField(Tag, blank=True, related_name='questions')
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = QuestionManager()

    def __str__(self):
        return f'({self.id}) {self.profile.user.username}: {self.title}'


class AnswerManager(models.Manager):
    def get_top_answers(self, question):
        return self.filter(related_question=question).order_by('-rating')

class Answer(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='answers')
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    objects = AnswerManager()

    def __str__(self):
        return f'({self.id}) {self.profile.user.username} on {self.related_question.title}'


class Eval(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='rated_by')

    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True, related_name='evals')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True, related_name='evals')

    LIKE = '+'
    DISLIKE = '-'
    EVALS = [
        (LIKE, "like"),
        (DISLIKE, "dislike"),
    ]
    eval = models.CharField(max_length=1, choices=EVALS)

    def __str__(self):
        return f'({self.id}) {self.eval}: {self.profile.user.username} -> {self.question}'
