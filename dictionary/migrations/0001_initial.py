# Generated by Django 2.1.7 on 2019-03-09 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(max_length=25)),
                ('word_meaning', models.CharField(max_length=150)),
                ('related_words', models.ManyToManyField(related_name='_word_related_words_+', to='dictionary.Word')),
            ],
        ),
    ]
