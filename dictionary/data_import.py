import json

from .models import Extracted_frequencies,Extracted_Word

def data_import():
    data = json.load(open('../data.json','r'))

    for i in data:
        if(len(i)>30):
            continue
        w = Extracted_Word(word_text=i)
        w.save()
        for j in data[i]:
            word=Extracted_Word.objects.get(word_text=i)
            freq = Extracted_frequencies(word=word, pdf_file=j[0], frequency=j[1])
            freq.save()


