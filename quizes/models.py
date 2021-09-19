from django.db import models
import uuid
import random
# Create your models here.

DIFICULTY_CHOICES = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
)


class Quiz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=100)
    number_of_questions = models.IntegerField()
    time_to_complete = models.IntegerField()
    pass_mark = models.IntegerField()
    dificulty = models.CharField(max_length=6, choices=DIFICULTY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return str(self.name)

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]
