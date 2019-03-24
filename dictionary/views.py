from django.shortcuts import get_object_or_404, render

from django.http import Http404

from .models import *

def search(request):
    return render(request, 'dictionary/search.html', {})

def word_detail(request, word):
    if(request.GET.get('input_word',False)):
        word1 = request.GET.get('input_word',False)
        word2 = word1.lower()
        word_data = get_object_or_404(Extracted_Word, word_text=word2)
        pdf_files = word_data.extracted_frequencies_set.all()
        pdf_files = list(pdf_files)
        for i in range (0,len(pdf_files)):
            for j in range (0,len(pdf_files)):
                if pdf_files[i].frequency > pdf_files[j].frequency:
                    temp = pdf_files[i]
                    pdf_files[i] = pdf_files[j]
                    pdf_files[j] = temp
    else:
        word3 = word.lower()
        word_data = get_object_or_404(Extracted_Word, word_text=word3)
        pdf_files = word_data.extracted_frequencies_set.all()
        pdf_files = list(pdf_files)
        for i in range (0,len(pdf_files)):
            for j in range (0,len(pdf_files)):
                if pdf_files[i].frequency > pdf_files[j].frequency:
                    temp = pdf_files[i]
                    pdf_files[i] = pdf_files[j]
                    pdf_files[j] = temp
    return render(request, 'dictionary/word.html', {'word_data': word_data, 'pdf_files': pdf_files})
