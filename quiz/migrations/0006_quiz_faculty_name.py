# Generated by Django 4.2.1 on 2024-11-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_userrank_quizsubmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='faculty_name',
            field=models.TextField(null=True),
        ),
    ]
