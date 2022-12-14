from django.core.management.base import BaseCommand
from django.contrib.auth import hashers
from app.models import *
from time import sleep


class Command(BaseCommand):
    help = '''Set ratio and fill DB
            - ratio tags
            - ratio users
            - ratio*10 questions
            - ratio*100 answers
            - ratio*200 evals (likes)'''

    def add_arguments(self, parser):
        parser.add_argument('ratio', nargs='+', type=int, help='Ratio value')

    def handle(self, *args, **kwargs):
        ratio = kwargs['ratio'][0]

        TAGS_RATIO = ratio
        USERS_RATIO = ratio
        QUESTIONS_RATIO = 10*ratio
        ANSWERS_RATIO = 100*ratio
        EVALS_RATIO = 200*ratio


        first_tag_id = Tag.objects.last().id + 1
        first_user_id = User.objects.last().id + 1
        first_profile_id = Profile.objects.last().id + 1
        first_question_id = Question.objects.last().id + 1
        first_answer_id = Answer.objects.last().id + 1
        first_eval_id = Eval.objects.last().id + 1

        print("First IDs of new instances:\n"
                f"Tag: {first_tag_id}\n"
                f"User: {first_user_id}\n"
                f"Profile: {first_profile_id}\n"
                f"Question: {first_question_id}\n"
                f"Answer: {first_answer_id}\n"
                f"Eval: {first_eval_id}")

        ''' Подписал время заполнения для ratio = 10000 '''

        # 1 секунда
        tags = [Tag(name=f'Tag {tag_id}')
                    for tag_id in range(first_tag_id, first_tag_id + TAGS_RATIO)]
        Tag.objects.bulk_create(tags)

        self.stdout.write('Filling Tags completed with success!')

        # 17 минут !!!
        users = [User(username=f'User{user_id}',
                        first_name=f'fName{user_id}',
                        last_name=f'lName{user_id}',
                        email=f'user{user_id}@gmail.com',
                        password=hashers.make_password(f'pass{user_id}'))
                        for user_id in range(first_user_id, first_user_id + USERS_RATIO)]
        User.objects.bulk_create(users)

        self.stdout.write('Filling Users completed with success!')

        # 3 секунды
        profiles = [Profile(user_id=user_id,
                            avatar='stack-underflow.png')
                            for user_id in range(first_user_id, first_user_id + USERS_RATIO)]
        Profile.objects.bulk_create(profiles)

        self.stdout.write('Filling Profiles completed with success!')

        # ? секунд
        questions = [Question(profile_id=first_profile_id + question_id%USERS_RATIO,
                                title=f'Title of question #{question_id}',
                                text=f'Smart text of question #{question_id}')
                                for question_id in range(first_question_id, first_question_id + QUESTIONS_RATIO)]
        Question.objects.bulk_create(questions)
        for i in range(len(questions)):
            for j in range(3):
                questions[i].tags.add(tags[(i-2)%TAGS_RATIO + j])

        self.stdout.write('Filling Questions completed with success!')

        # 1 минута
        answers = [Answer(profile_id=first_profile_id + answer_id%USERS_RATIO,
                            related_question_id=first_question_id + answer_id%QUESTIONS_RATIO,
                            text=f'Smart answer #{answer_id} by Pro')
                            for answer_id in range(first_answer_id, first_answer_id + ANSWERS_RATIO)]
        Answer.objects.bulk_create(answers)

        self.stdout.write('Filling Answers completed with success!')

        # 2 минуты
        evals = [Eval(profile_id=first_profile_id + eval_id%USERS_RATIO,
                        question_id=first_question_id + eval_id%QUESTIONS_RATIO,
                        eval='+')
                        for eval_id in range(first_eval_id, first_eval_id + EVALS_RATIO)]
        Eval.objects.bulk_create(evals)

        self.stdout.write('Filling Evals completed with success!')
