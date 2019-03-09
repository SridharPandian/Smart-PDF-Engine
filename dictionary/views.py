from django.shortcuts import get_object_or_404, render

from django.http import Http404

from .models import Word

def search(request):
    return render(request, 'dictionary/search.html', {})

def word_detail(request, word):
    if(request.GET.get('input_word',False)):
        word1 = request.GET.get('input_word',False)
        word2 = word1[0].upper() + word1[1:].lower()
        word_data = get_object_or_404(Word, word_text=word2)
    else:
        word3 = word[0].upper() + word[1:].lower()
        word_data = get_object_or_404(Word, word_text=word3)
    return render(request, 'dictionary/word.html', {'word_data': word_data})
