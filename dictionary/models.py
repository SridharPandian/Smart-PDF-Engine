from django.db import models

class Word(models.Model):
    word_text = models.CharField(max_length=25)
    word_meaning = models.CharField(max_length=150)
    related_words = models.ManyToManyField('self')

    def __str__(self):
        return self.word_text

