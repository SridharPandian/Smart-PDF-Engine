import PyPDF2 as pdf
import os
import json

from pathlib import Path
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from collections import Counter

pdf_files = os.listdir("Unlocked search documents")

read_pdfs = []
for i in pdf_files:
    file = open("Unlocked search documents/"+i, 'rb')
    pdf_file = pdf.PdfFileReader(file)
    read_pdfs.append(pdf_file)

page_count = []
for i in read_pdfs:
    page_count.append(i.getNumPages())

pdf_text = []
for i in read_pdfs:
    count = 0
    text = ""
    while count<i.getNumPages():
        pageObj = i.getPage(count)
        count+=1
        text += pageObj.extractText()
    pdf_text.append(text)

tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
pdf_tokens = []
for i in pdf_text:
    pdf_tokens.append(tokenizer.tokenize(i))

punctuations = ['(',')','.','.,','-',';',':','[',']',',','\n','?']
stop_words = stopwords.words('english')

pdf_keywords = []
for i in pdf_tokens:
    pdf_keywords.append([word for word in i if not word in stop_words and not word in punctuations])

cased_pdf_keywords = []
    
for i in pdf_keywords:
    temp = []
    for x in i:
        temp.append(str(x).lower())
    cased_pdf_keywords.append(temp)

pdf_counter = []
for i in cased_pdf_keywords:
    pdf_counter.append(Counter(i))

word_ranking = {}
temp = []
for i in range (0,len(pdf_counter)):
#     print(pdf_files[i])
    for j in pdf_counter[i]:
        if temp.count(j)==0:
            temp.append(j)
            word_ranking[j] = [[pdf_files[i],pdf_counter[i][j]]]
        else:
            word_ranking[j].append([pdf_files[i],pdf_counter[i][j]])

for i in word_ranking:
    for j in range (0,len(word_ranking[i])):
        for k in range (0,len(word_ranking[i])):
            if word_ranking[i][j][1]>word_ranking[i][k][1]:
                temp = word_ranking[i][j]
                word_ranking[i][j] = word_ranking[i][k]
                word_ranking[i][k] = temp

with open('data.json', 'w') as fp:
    json.dump(word_ranking,fp)