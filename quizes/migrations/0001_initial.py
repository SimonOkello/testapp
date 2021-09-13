# Generated by Django 3.2.7 on 2021-09-13 08:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=100)),
                ('number_of_questions', models.IntegerField()),
                ('time_to_complete', models.IntegerField()),
                ('pass_mark', models.IntegerField()),
                ('dificulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
    ]
