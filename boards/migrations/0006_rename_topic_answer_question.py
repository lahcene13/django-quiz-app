# Generated by Django 3.2.10 on 2022-02-02 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20220202_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='topic',
            new_name='question',
        ),
    ]
