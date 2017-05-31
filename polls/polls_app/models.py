from django.db import models
from django.utils.text import slugify
import random

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Poll(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    questions = models.ManyToManyField(Question, blank=True)

    def clean(self):
        self.slug = self.slug or slugify(self.name) + str(random.randint(1, 1000))

    def __str__(self):
        return '{}'.format(self.name)
