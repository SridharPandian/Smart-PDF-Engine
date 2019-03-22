from django.db import models

class Word(models.Model):
    word_text = models.CharField(max_length=25)
    word_meaning = models.CharField(max_length=150)
    related_words = models.ManyToManyField('self')

    def __str__(self):
        return self.word_text

class Extracted_Word(models.Model):
    word_text = models.CharField(max_length=100)

    def __str__(self):
        return self.word_text

class Extracted_frequencies(models.Model):
    word = models.ForeignKey(Extracted_Word, db_index=True,on_delete=models.CASCADE)
    pdf_file = models.CharField(max_length=150)
    frequency = models.IntegerField(default=1)  

    def __str__(self):
        return self.pdf_file