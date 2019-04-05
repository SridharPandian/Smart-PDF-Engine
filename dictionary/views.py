from django.shortcuts import get_object_or_404, render

from django.http import Http404, FileResponse
from reportlab.pdfgen import canvas
from .models import *
import requests
import json

def search(request):
    return render(request, 'dictionary/search.html', {})

def word_detail(request, word):
    app_id = '982812a1'
    app_key = '75cbf611efa97cd128b405705647add4'
    if(request.GET.get('input_word',False)):
        # To get the requested word
        word1 = request.GET.get('input_word',False)
        word2 = word1.lower()
        word_pass = str(word2)
        # To extract word data from database
        word_data = get_object_or_404(Extracted_Word, word_text=word2)

        # To get all related words using Oxford dictionary
        language = 'en'
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_pass + '/synonyms;antonyms'
        response = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        
        synonyms = response.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
        related_word_list = []

        for i in synonyms:
            if(Extracted_Word.objects.filter(word_text=i['text']).count()>0):
                related_word_list.append(i['text'])

        # To extract pdf files based on word data
        pdf_files = word_data.extracted_frequencies_set.all()
        pdf_files = list(pdf_files)

        # Ordering all word data
        for i in range (0,len(pdf_files)):
            for j in range (0,len(pdf_files)):
                if pdf_files[i].frequency > pdf_files[j].frequency:
                    temp = pdf_files[i]
                    pdf_files[i] = pdf_files[j]
                    pdf_files[j] = temp
    else:
        word3 = word.lower()
        word_pass = str(word3)
        # To extract word data from database
        word_data = get_object_or_404(Extracted_Word, word_text=word3)

        # To get all related words using Oxford dictionary
        language = 'en'
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_pass + '/synonyms;antonyms'
        response = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

        synonyms = response.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
        related_word_list = []

        for i in synonyms:
            if(Extracted_Word.objects.filter(word_text=i['text']).count()>0):
                related_word_list.append(i['text'])
        
        # To extract pdf files based on word data
        pdf_files = word_data.extracted_frequencies_set.all()
        pdf_files = list(pdf_files)
        for i in range (0,len(pdf_files)):
            for j in range (0,len(pdf_files)):
                if pdf_files[i].frequency > pdf_files[j].frequency:
                    temp = pdf_files[i]
                    pdf_files[i] = pdf_files[j]
                    pdf_files[j] = temp

    return render(request, 'dictionary/word.html', {'word_data': word_data, 'pdf_files': pdf_files, 'dict_response': related_word_list})

def pdf_openner(request, document):
    try:
        return FileResponse(open('D:/Semantics/Unlocked search documents/' + document, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()