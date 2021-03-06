# Generated by Django 3.2.10 on 2022-02-02 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_topic_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='note',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='status',
            field=models.CharField(default='Not answered', max_length=25),
        ),
    ]
