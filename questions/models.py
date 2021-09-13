from django.db import models
import uuid

# Create your models here.
from quizes.models import Quiz

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=225)
    quiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"Question:{self.question}=>Answer:{self.name}=>Correct:{self.correct}"
