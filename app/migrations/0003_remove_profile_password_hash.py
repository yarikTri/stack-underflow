# Generated by Django 4.1.3 on 2022-11-28 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_user_answer_profile_rename_user_eval_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password_hash',
        ),
    ]