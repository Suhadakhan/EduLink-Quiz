# Generated by Django 4.2.1 on 2024-11-11 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_rename_quiz_template_quiz_quiz_template_display'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='quiz_template_display',
        ),
    ]
